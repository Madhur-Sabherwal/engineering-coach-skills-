#!/usr/bin/env python3
"""Check every generated skill: frontmatter, name matches folder, description length, no private strings."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FORBIDDEN = ["curtin", "bitbucket", "madhur", "sabherwal", "@curtin", "kiro", "OneDrive", "C:\\Users"]
errors = []

skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if not skills:
    sys.exit("No skills found. Run: python scripts/build.py")

for f in skills:
    text = f.read_text(encoding="utf-8")
    folder = f.parent.name
    m = re.match(r"---\nname: (.+)\ndescription: (.+)\n---\n", text)
    if not m:
        errors.append(f"{folder}: bad frontmatter")
        continue
    name, desc = m.group(1), m.group(2)
    if name != folder:
        errors.append(f"{folder}: name '{name}' != folder")
    if len(desc) > 1024:
        errors.append(f"{folder}: description {len(desc)} chars (max 1024)")
    if re.search(r"__[A-Z]+__", text):
        errors.append(f"{folder}: unreplaced placeholder")
    low = text.lower()
    for bad in FORBIDDEN:
        if bad.lower() in low:
            errors.append(f"{folder}: contains private/forbidden string '{bad}'")

for p in ROOT.rglob("*"):
    if p.is_file() and ".git" not in p.parts and p.suffix in {".md", ".py", ".sh", ".ps1", ".txt"} and p.name != "validate.py":
        low = p.read_text(encoding="utf-8", errors="ignore").lower()
        for bad in FORBIDDEN:
            if bad.lower() in low:
                errors.append(f"{p.relative_to(ROOT)}: contains '{bad}'")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(skills)} skills valid, no private strings found.")
