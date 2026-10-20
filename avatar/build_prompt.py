#!/usr/bin/env python3
"""Build an image/video prompt from the likeness profile.

Usage:
  python3 build_prompt.py "standing at a conference podium" [--framing full|half|head] [--outfit 0-3] [--glasses primary|alternate]
"""
import argparse, json, pathlib

P = json.loads((pathlib.Path(__file__).parent / "likeness-profile.json").read_text())
S = P["subject"]

def build(scene, framing="half", outfit=0, glasses="primary"):
    f, h, fh = S["face"], S["hair"], S["facial_hair"]
    framing_txt = {
        "head": "close-up head-and-shoulders portrait",
        "half": "waist-up portrait",
        "full": "full-body photo, head to shoes",
    }[framing]
    parts = [
        f"{P['render_defaults']['style']}. {framing_txt} of a {S['body']['build']} man, {S['age_appearance']}",
        f"{S['skin']['tone']} skin, {S['skin']['undertone']}, {S['skin']['texture']}",
        f"{h['color']} hair, {h['style']}",
        f"{fh['mustache']}; {fh['chin']}",
        f"{f['shape']}, {f['chin_neck']}, {f['eyes']} eyes, {f['nose']}, {f['ears']} ears, {f['default_expression']}",
        f"wearing {S['eyewear'][glasses]}",
        f"{S['body']['torso']}, {S['body']['lower_body']}, {S['body']['arms']}",
        f"wearing {S['wardrobe_defaults'][outfit]}",
        f"Scene: {scene}",
    ]
    prompt = ". ".join(parts) + "."
    negative = ", ".join(P["negative"])
    return prompt, negative

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("scene")
    ap.add_argument("--framing", default="half", choices=["head", "half", "full"])
    ap.add_argument("--outfit", type=int, default=0)
    ap.add_argument("--glasses", default="primary", choices=["primary", "alternate"])
    a = ap.parse_args()
    p, n = build(a.scene, a.framing, a.outfit, a.glasses)
    print("PROMPT:\n" + p + "\n\nAVOID:\n" + n)
