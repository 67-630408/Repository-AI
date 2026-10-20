# Personal Likeness Profile

A reusable description ("likeness code") of the repo owner's appearance, for generating
consistent photos, avatars, and avatar-style videos.

**Status: DRAFT v0.1 — not locked. Waiting for the owner's approval or edits.**

## Files
- `likeness-profile.json` — the source of truth: face, skin, hair, glasses, body, wardrobe, gestures, and things to avoid.
- `build_prompt.py` — turns the profile plus a scene into a ready-to-paste prompt.

## How to use
```bash
python3 avatar/build_prompt.py "speaking at a conference podium" --framing half --outfit 2
python3 avatar/build_prompt.py "relaxing on a lanai at sunset" --framing full --outfit 3 --glasses alternate
```
- `--framing`: `head`, `half`, or `full`
- `--outfit`: 0 oxford + khakis, 1 khakis + belt, 2 black suit + teal tie, 3 green t-shirt
- `--glasses`: `primary` (black rectangular) or `alternate` (tortoiseshell)

## Best results
Text alone gets close but can't capture an exact face. For the strongest likeness,
use a tool that accepts reference photos (Canva, Gamma, Higgsfield, HeyGen, etc.) and attach
the owner's front-facing selfie, studio headshot, full-body photo, and profile shot
together with the prompt from `build_prompt.py`.

## Rule for future images
Every generated image or video of the owner should start from `build_prompt.py`
(or the profile) so the look stays consistent.
