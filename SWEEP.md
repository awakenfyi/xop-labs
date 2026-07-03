# Governed Sweep Checklist

Execute in this exact order. The org profile goes live last — it links to
`hold-release/studies/ponytail`, so that repo must exist before the profile
points to it or the front door 404s.

---

## Step 1 — Create `awakenfyi/hold-release` and move the study

**On GitHub:**
1. Create new repo: `awakenfyi/hold-release` (public, MIT, no auto-init)
2. Clone locally: `git clone https://github.com/awakenfyi/hold-release`
3. Copy content out of xop-labs:
   ```
   cp -r xop-labs/in-the-wild/hold-release/. hold-release/
   ```
4. Push to new repo:
   ```
   cd hold-release && git init && git add -A
   git commit -m "Initial commit — Hold & Release field study family"
   git remote add origin https://github.com/awakenfyi/hold-release
   git push -u origin main
   ```
5. In xop-labs, replace `in-the-wild/hold-release/` content with a pointer:
   - Delete `in-the-wild/hold-release/studies/` and `in-the-wild/hold-release/methodology/`
   - Update `in-the-wild/hold-release/README.md` to redirect:
     > *This study has moved to [awakenfyi/hold-release](https://github.com/awakenfyi/hold-release).*
   - Update `in-the-wild/README.md` link target from local path to `https://github.com/awakenfyi/hold-release/tree/main/studies/ponytail/`
   - Update `xop-labs/README.md` link target similarly

**Files whose links need updating in xop-labs after move:**

| File | Line | Old target | New target |
|---|---|---|---|
| `README.md` | In the Wild bullet | `in-the-wild/hold-release/studies/ponytail/` | `https://github.com/awakenfyi/hold-release/tree/main/studies/ponytail/` |
| `in-the-wild/README.md` | Hold & Release row | `hold-release/studies/ponytail/` | `https://github.com/awakenfyi/hold-release/tree/main/studies/ponytail/` |
| `in-the-wild/README.md` | Section header | `hold-release/` | `https://github.com/awakenfyi/hold-release` |
| `.github-profile-README.md` | hold-release bullet | already absolute URL — verify it resolves |

**Files whose links need updating in xop (awakenfyi/xop) after move:**

| File | What to add |
|---|---|
| `README.md` | Add "In the Wild" pointer row: `[Does It Let Go? — Hold & Release: Ponytail](https://github.com/awakenfyi/hold-release/tree/main/studies/ponytail/) — preregistered field study` |

**Files whose links need updating in xop-kit after move:**

| File | What to add |
|---|---|
| `README.md` | Add hold-release to family table if not already present |

---

## Step 2 — Rename `lyra` → `lyra-research`

**On GitHub:**
1. Go to `awakenfyi/lyra` → Settings → Repository name → rename to `lyra-research`
2. GitHub will auto-redirect old URLs for 1 year. Do not rely on this permanently.

**Files whose links need updating after rename:**

| Repo | File | Update |
|---|---|---|
| xop-labs | `README.md` — family table | lyra → lyra-research URL (already written correctly as `lyra-research`) |
| xop-labs | `.github-profile-README.md` | lyra-research URL (already written correctly) |
| xop-kit | `README.md` | Any lyra references → lyra-research |
| xop | `README.md` | Any lyra references → lyra-research |
| xhat | `README.md`, `setup.py` | Any lyra references → lyra-research |
| lyra-research | Internal docs | Update any self-referential URLs from lyra → lyra-research |

---

## Step 3 — Apply org profile README

**Prerequisite:** Steps 1 and 2 must be complete. All linked repos must exist at their final URLs.

**On GitHub:**
1. Open (or create) repo `awakenfyi/.github`
2. Create or update `profile/README.md` with contents of `xop-labs/.github-profile-README.md`
3. Verify all six links resolve:
   - `awakenfyi/xop` ✓ (exists)
   - `awakenfyi/xop-kit` ✓ (exists)
   - `awakenfyi/hold-release` ← must exist (Step 1)
   - `awakenfyi/xhat` ✓ (exists)
   - `awakenfyi/xop-labs` ✓ (exists)
   - `awakenfyi/lyra-research` ← must be renamed (Step 2)
4. Verify the deep link resolves: `https://github.com/awakenfyi/hold-release/tree/main/studies/ponytail`
5. Publish.

---

## Verification checklist (run after all three steps)

- [ ] `github.com/awakenfyi` shows the new org profile
- [ ] All six repo links in the profile resolve without redirect
- [ ] `hold-release/studies/ponytail/` exists in the new repo
- [ ] `hold-release/studies/ponytail/README.md` renders correctly
- [ ] xop-labs `in-the-wild/hold-release/` shows the redirect notice
- [ ] `lyra-research` resolves (old `lyra` URL still redirects — note the expiry)
- [ ] xop-kit README family table is current
- [ ] xop README "In the Wild" pointer exists

---

*This file lives in xop-labs as a record of the planned sweep. Archive or delete after the sweep completes.*
