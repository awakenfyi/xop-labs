"""
xop_harness.py — the single authoring authority for xOPs.

Build an xOP with these methods only, then call .build(). A malformed xOP is
unreachable by construction, and validate() raises XopError on the mechanical
rules in XOP_HARNESS.md. The harness is a GUARD: it enforces shape and raises.
It does NOT judge the semantic parts (is the anchor observable-not-taste? is the
opposite error legitimate? does it pass the Admission Test?) — those are returned
as human-review FLAGS, never asserted. Flags hand off to the Menders (/xop evolve)
and, ultimately, to the human pilot. The harness proves the shape; it never claims
the xOP is right.

Destined for xop-kit. Pure standard library; PyYAML optional (only for from_yaml).
"""

import re

API_VERSION = "xop.dev/v1alpha1"
KIND = "XOP"

LADDER = ["DESIGNED", "EVALUATION-READY", "RULE-TESTED", "HUMAN-EVALUATED", "FIELD-VALIDATED"]
SEMANTIC_RUNGS = {"HUMAN-EVALUATED", "FIELD-VALIDATED"}   # require evidence to claim
METRIC_KINDS = {"primary", "opposite", "forced", "abstain", "agreement"}
BLENDED_NAMES = {"score", "overall", "gate", "composite", "quality_score",
                 "fidelity_score", "pass_threshold", "total"}
ABSTAIN_BRANCHES = {"ask", "abstain", "defer", "hold"}
ID_RE = re.compile(r"^xop\.[a-z0-9]+\.[a-z0-9\-]+$")

# Standing semantic prompts — always handed to a human; the harness can't decide them.
SEMANTIC_FLAGS = [
    "Confirm the anchor is OBSERVABLE, not taste (check it against the anchor table).",
    "Confirm the opposite error is a LEGITIMATE failure, not a strawman.",
    "Confirm it passes the Admission Test: a fixed check can't resolve the branch.",
]


class XopError(Exception):
    pass


class XOP:
    """Builder. Each method returns self so calls chain; build() validates."""

    def __init__(self, id, title, domain, profile=None):
        self.d = {
            "api_version": API_VERSION,
            "kind": KIND,
            "metadata": {"id": id, "title": title, "domain": domain, "status": "DESIGNED"},
            "spec": {
                "decisions": {},
                "observable_signals": {},
                "evaluation": {"metrics": {}},
            },
        }
        if profile:
            self.d["metadata"]["profile"] = profile

    # ---- spec parts ----
    def purpose(self, text):
        self.d["spec"]["purpose"] = text
        return self

    def applies_when(self, *conds):
        self.d["spec"].setdefault("scope", {})["applies_when"] = list(conds)
        return self

    def does_not_apply_when(self, *conds):
        self.d["spec"].setdefault("scope", {})["does_not_apply_when"] = list(conds)
        return self

    def required_context(self, *items):
        self.d["spec"]["required_context"] = list(items)
        return self

    def observable_signal(self, name, desc):
        self.d["spec"]["observable_signals"][name] = desc
        return self

    def decision(self, branch, when, action):
        self.d["spec"]["decisions"][branch] = {"when": when, "action": action}
        return self

    def opposite_error(self, text):
        self.d["spec"]["opposite_error"] = text
        return self

    def never_break(self, text):
        self.d["spec"]["never_break"] = text
        return self

    def on_abstain(self, artifact_action, release_action, route):
        self.d["spec"]["on_abstain"] = {
            "artifact_action": artifact_action,
            "release_action": release_action,
            "route": route,
        }
        return self

    def metric(self, name, kind, desc):
        # Wrong combinations refused at construction time.
        if kind not in METRIC_KINDS:
            raise XopError(f"unknown metric kind {kind!r}; use {sorted(METRIC_KINDS)}")
        if name.lower() in BLENDED_NAMES:
            raise XopError(f"blended/gate metric {name!r} forbidden — "
                           "report the primary and opposite errors on separate axes")
        self.d["spec"]["evaluation"]["metrics"][name] = {"kind": kind, "desc": desc}
        return self

    def evaluation(self, sample, labelers=None, labels=None):
        ev = self.d["spec"]["evaluation"]
        ev["sample"] = sample
        if labelers:
            ev["labelers"] = labelers
        if labels:
            ev["labels"] = labels
        return self

    def set_status(self, rung):
        if rung not in LADDER:
            raise XopError(f"unknown status {rung!r}; use one of {LADDER}")
        self.d["metadata"]["status"] = rung
        return self

    def build(self):
        problems, flags = validate(self.d)
        if problems:
            raise XopError("XOP VALIDATION FAILED:\n  " + "\n  ".join(problems))
        return self.d, flags


def validate(xop):
    """Return (problems, flags). problems => mechanical failures (build raises).
    flags => standing semantic prompts for a human (never block)."""
    problems = []
    md = xop.get("metadata", {})
    spec = xop.get("spec", {})

    if xop.get("api_version") != API_VERSION:
        problems.append(f"api_version must be {API_VERSION!r}")
    if xop.get("kind") != KIND:
        problems.append(f"kind must be {KIND!r}")

    xid = md.get("id", "")
    if not ID_RE.match(xid):
        problems.append(f"metadata.id {xid!r} must match xop.<domain>.<slug> (namespace, no family letter)")

    status = md.get("status")
    if status not in LADDER:
        problems.append(f"metadata.status {status!r} must be one rung of {LADDER}")

    # decisions: >= 2 branches, one of them an abstain/ask path
    decisions = spec.get("decisions", {})
    if len(decisions) < 2:
        problems.append("spec.decisions needs >= 2 branches")
    if not any(b.lower() in ABSTAIN_BRANCHES or "ask" in b.lower() or "abstain" in b.lower()
               for b in decisions):
        problems.append("spec.decisions must include an abstain/ask branch (never force the default)")

    for field in ("opposite_error", "never_break"):
        if not str(spec.get(field, "")).strip():
            problems.append(f"spec.{field} is required and non-empty")

    if not spec.get("on_abstain"):
        problems.append("spec.on_abstain is required (the route when unsure)")
    elif not spec["on_abstain"].get("route"):
        problems.append("spec.on_abstain.route is required")

    if not spec.get("observable_signals"):
        problems.append("spec.observable_signals is required (the observable anchor)")

    # metrics: >= 1 primary and >= 1 opposite; no blended gate
    ev = spec.get("evaluation", {})
    metrics = ev.get("metrics", {})
    kinds = {m.get("kind") for m in metrics.values() if isinstance(m, dict)}
    if "primary" not in kinds:
        problems.append("spec.evaluation.metrics needs >= 1 'primary' error metric")
    if "opposite" not in kinds:
        problems.append("spec.evaluation.metrics needs >= 1 'opposite' error metric")
    for name in metrics:
        if name.lower() in BLENDED_NAMES:
            problems.append(f"blended/gate metric {name!r} present — split into separate axes")
    if "pass_threshold" in ev or "score" in ev or "gate" in ev:
        problems.append("no universal gate: remove blended evaluation keys (pass_threshold/score/gate)")

    # semantic rung requires evidence
    if status in SEMANTIC_RUNGS:
        for need in ("sample", "labelers", "labels"):
            if not ev.get(need):
                problems.append(f"status {status} requires evaluation.{need} (rung claimed without evidence)")

    return problems, list(SEMANTIC_FLAGS)


def from_yaml(path):
    """Load and validate an existing xOP yaml. Returns (xop, problems, flags)."""
    import yaml
    with open(path, encoding="utf-8") as f:
        xop = yaml.safe_load(f)
    problems, flags = validate(xop)
    return xop, problems, flags


# ---------------------------------------------------------------- self-test
if __name__ == "__main__":
    print("== good xOP ==")
    good = (
        XOP("xop.marketing.urgency-evidence", "No Made-Up Urgency", "marketing")
        .purpose("Block invented urgency; keep real, verified deadlines.")
        .observable_signal("deadline_field", "A verified deadline, capacity, inventory, or expiry.")
        .decision("state_urgency", "A verified deadline exists.", "State it and cite the source.")
        .decision("withhold", "No verified deadline.", "Remove the urgency language.")
        .decision("ask", "Existence of a deadline is unclear.", "Surface it; request confirmation.")
        .opposite_error("Removing a real, current deadline (over-hedging).")
        .never_break("Never manufacture scarcity that isn't verified.")
        .on_abstain("preserve_current_copy", "hold_urgency_claim", "brand_marketing_owner")
        .metric("fabricated_urgency", "primary", "Urgency stated with no verified basis.")
        .metric("removed_real_urgency", "opposite", "A real deadline was stripped.")
        .metric("abstain_rate", "abstain", "Deferred because the basis was unclear.")
        .evaluation("40-60 real urgency decisions")
    )
    xop, flags = good.build()
    print("  PASS — built", xop["metadata"]["id"])
    print("  human-review flags:")
    for f in flags:
        print("   -", f)

    print("\n== malformed xOPs (each should raise) ==")
    # 1. no opposite error, no abstain branch
    try:
        (XOP("xop.x.bad", "Bad", "x")
         .observable_signal("s", "d")
         .decision("do", "always", "do it")
         .never_break("x")
         .on_abstain("p", "h", "r")
         .metric("err", "primary", "d")
         .build())
    except XopError as e:
        print("  raised as expected:\n   ", str(e).replace("\n", "\n    "))

    # 2. blended metric refused at construction
    try:
        XOP("xop.x.bad2", "Bad2", "x").metric("score", "primary", "blended")
    except XopError as e:
        print("  raised at construction:", e)

    # 3. validate the flagship if present
    import os
    flagship = os.path.join(os.path.dirname(__file__), "..", "..",
                            "catalog", "profiles", "design", "layout-fit.yaml")
    if os.path.exists(flagship):
        try:
            _, probs, _ = from_yaml(flagship)
            print(f"\n== flagship layout-fit.yaml: {'CLEAN' if not probs else 'PROBLEMS'} ==")
            for p in probs:
                print("   -", p)
        except Exception as e:
            print("  (skipped flagship check:", e, ")")
