#!/usr/bin/env python3
"""
Validierungs-Gate fuer hildegard/*.html (Mockup).
Prueft je HTML-Datei:
  1. Balance von <div>/</div>
  2. JS-Syntax jedes <script>-Blocks (node --check)
  3. keine woertliche 'undefined' in gerendertem Text-Kontext (Heuristik: >undefined<)
Exit-Code != 0 => Deploy wird geblockt.
"""
import re, glob, subprocess, sys, os, tempfile

fail = False

def check_file(f):
    global fail
    print(f"\n== {f} ==")
    t = open(f, encoding="utf-8").read()

    # 1) div-Balance
    o, c = t.count("<div"), t.count("</div>")
    if o != c:
        print(f"  ✗ div-Balance: {o} offen / {c} geschlossen"); fail = True
    else:
        print(f"  ✓ div-Balance {o}/{c}")

    # 2) JS-Syntax je <script>-Block
    blocks = re.findall(r"<script>(.*?)</script>", t, re.S)
    for i, b in enumerate(blocks):
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tmp:
            tmp.write(b); path = tmp.name
        r = subprocess.run(["node", "--check", path], capture_output=True, text=True)
        os.unlink(path)
        if r.returncode != 0:
            msg = (r.stderr.strip().splitlines() or ["Syntaxfehler"])[0]
            print(f"  ✗ JS-Block {i}: {msg}"); fail = True
        else:
            print(f"  ✓ JS-Block {i}")
    if not blocks:
        print("  · keine <script>-Bloecke")

    # 3) Heuristik: sichtbares 'undefined' (>undefined<) deutet auf Render-Bug
    if re.search(r">\s*undefined\s*<", t):
        print("  ✗ woertliches 'undefined' im HTML gefunden"); fail = True

files = sorted(glob.glob("hildegard/*.html"))
if not files:
    print("Keine hildegard/*.html gefunden."); sys.exit(1)
for f in files:
    check_file(f)

print("\n" + ("✗ VALIDIERUNG FEHLGESCHLAGEN — Deploy wird geblockt." if fail else "✓ Validierung bestanden."))
sys.exit(1 if fail else 0)
