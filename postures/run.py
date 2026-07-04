#!/usr/bin/env python3
"""postures — reasoning postures with measured costs.

Runs a fixed prompt set under each posture, counts tokens from real API
responses, and grades quality with an external grader call. No model ever
grades itself: the grader never sees which posture produced an answer.

Usage:
    python run.py                      # all postures vs baseline
    python run.py --posture verse      # one posture (baseline always runs)
    python run.py --prompts my.json    # custom prompt set
    python run.py --model claude-opus-4-8
"""

import argparse
import json
import re
import sys
from pathlib import Path

import anthropic

HERE = Path(__file__).parent
POSTURES_DIR = HERE / "postures"
DEFAULT_MODEL = "claude-opus-4-8"

GRADER_SCHEMA = {
    "type": "object",
    "properties": {
        "accuracy": {"type": "integer", "description": "0-10: is the answer correct/sound?"},
        "completeness": {"type": "integer", "description": "0-10: does it cover what the task needs?"},
        "clarity": {"type": "integer", "description": "0-10: is it clear to the intended reader?"},
        "one_line_verdict": {"type": "string"},
    },
    "required": ["accuracy", "completeness", "clarity", "one_line_verdict"],
    "additionalProperties": False,
}

GRADER_PROMPT = """You are grading an answer to a task. You did not write the answer.
Grade only what is on the page. Length is NOT a virtue: do not reward padding,
and do not penalize brevity unless something the task needed is missing.

<task>
{task}
</task>

<answer>
{answer}
</answer>

Score accuracy, completeness, and clarity (0-10 each) and give a one-line verdict."""


def load_posture(name: str) -> str | None:
    """Extract the posture prompt block from a spec file. Baseline returns None."""
    path = POSTURES_DIR / f"{name}.xop.md"
    if not path.exists():
        sys.exit(f"error: no spec at {path}")
    text = path.read_text()
    m = re.search(r"## Posture prompt\s*\n+```\n(.*?)```", text, re.DOTALL)
    return m.group(1).strip() if m else None  # baseline has no prompt block


def run_prompt(client, model: str, posture_prompt: str | None, task: str):
    """One task under one posture. Returns (answer_text, output_tokens)."""
    kwargs = dict(
        model=model,
        max_tokens=16000,
        thinking={"type": "adaptive"},
        messages=[{"role": "user", "content": task}],
    )
    if posture_prompt:
        kwargs["system"] = posture_prompt
    resp = client.messages.create(**kwargs)
    answer = "".join(b.text for b in resp.content if b.type == "text")
    return answer, resp.usage.output_tokens


def grade(client, model: str, task: str, answer: str) -> dict:
    """External grader: separate call, blind to posture. Structured output."""
    resp = client.messages.create(
        model=model,
        max_tokens=1024,
        output_config={"format": {"type": "json_schema", "schema": GRADER_SCHEMA}},
        messages=[{"role": "user", "content": GRADER_PROMPT.format(task=task, answer=answer)}],
    )
    text = next(b.text for b in resp.content if b.type == "text")
    return json.loads(text)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--posture", help="single posture to test (baseline always runs)")
    ap.add_argument("--prompts", default=str(HERE / "prompts.json"))
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--out", default=str(HERE / "results.json"), help="raw results JSON")
    args = ap.parse_args()

    prompts = json.loads(Path(args.prompts).read_text())["prompts"]
    all_specs = sorted(p.stem.replace(".xop", "") for p in POSTURES_DIR.glob("*.xop.md"))
    if args.posture:
        if args.posture not in all_specs:
            sys.exit(f"error: unknown posture '{args.posture}' (have: {', '.join(all_specs)})")
        postures = ["baseline", args.posture]
    else:
        postures = ["baseline"] + [s for s in all_specs if s != "baseline"]

    client = anthropic.Anthropic()
    results = {p: {"tokens": 0, "quality": [], "runs": []} for p in postures}

    total = len(postures) * len(prompts)
    done = 0
    for posture in postures:
        posture_prompt = load_posture(posture)
        for prompt in prompts:
            done += 1
            print(f"[{done}/{total}] {posture} · {prompt['id']}", file=sys.stderr)
            answer, out_tokens = run_prompt(client, args.model, posture_prompt, prompt["text"])
            scores = grade(client, args.model, prompt["text"], answer)
            q = (scores["accuracy"] + scores["completeness"] + scores["clarity"]) / 3
            results[posture]["tokens"] += out_tokens
            results[posture]["quality"].append(q)
            results[posture]["runs"].append({
                "prompt_id": prompt["id"],
                "output_tokens": out_tokens,
                "scores": scores,
                "quality": round(q, 2),
                "answer": answer,
            })

    # ---- table ----
    base_tok = results["baseline"]["tokens"]
    base_q = sum(results["baseline"]["quality"]) / len(results["baseline"]["quality"])

    print(f"\nmodel: {args.model} · prompts: {len(prompts)} · tokens = API usage.output_tokens · grader = external, blind\n")
    print(f"{'posture':<10} {'tokens':>8} {'Δ tokens':>10} {'quality':>8} {'Δ quality':>10}")
    print("-" * 50)
    for posture in postures:
        tok = results[posture]["tokens"]
        q = sum(results[posture]["quality"]) / len(results[posture]["quality"])
        if posture == "baseline":
            print(f"{posture:<10} {tok:>8} {'—':>10} {q:>8.1f} {'—':>10}")
        else:
            dt = (tok - base_tok) / base_tok * 100
            print(f"{posture:<10} {tok:>8} {dt:>+9.1f}% {q:>8.1f} {q - base_q:>+10.1f}")

    Path(args.out).write_text(json.dumps(
        {"model": args.model, "prompt_set": args.prompts, "results": results}, indent=2))
    print(f"\nraw results → {args.out}")


if __name__ == "__main__":
    main()
