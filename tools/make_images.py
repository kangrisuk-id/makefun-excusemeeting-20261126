"""Build-time visual assets for the README (Pillow only; NOT imported by main.py).

Generates:
  assets/hero.png       1200x630  hero cover
  assets/shot-1.png     800x450   calendar with the meeting declined
  assets/shot-2.png     800x450   the winning line as a chat message
  assets/shot-3.png     800x450   tournament funnel 28 -> 1
  assets/shot-4.png     800x450   how the entry runs (terminal card)
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = os.path.join(ROOT, "assets")

BG = (18, 20, 28)          # charcoal
BG2 = (28, 31, 44)         # panel
GOLD = (212, 175, 55)
GOLD_SOFT = (232, 205, 110)
INK = (240, 238, 230)      # near-white
MUTED = (160, 165, 180)
RED = (224, 82, 82)
GREEN = (86, 190, 120)
TEAL = (72, 180, 190)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def base(w, h):
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    # subtle diagonal gold band
    d.polygon([(0, h), (w, h), (w, h - 46), (0, h - 46)], fill=(24, 26, 36))
    d.line([(0, h - 46), (w, h - 46)], fill=GOLD, width=3)
    return img, d


def hero():
    img, d = base(1200, 630)
    d.text((64, 48), "MAKE.FUN  ·  $10  ·  10 PLACES", font=font("DejaVuSans-Bold.ttf", 30),
           fill=GOLD)
    d.text((64, 100), "The Funniest Excuse", font=font("DejaVuSans-Bold.ttf", 58), fill=INK)
    d.text((64, 168), "for Skipping a Meeting", font=font("DejaVuSans-Bold.ttf", 58), fill=INK)
    d.line([(64, 252), (544, 252)], fill=GOLD, width=4)
    # declined calendar card, right side (clear of the title)
    d.rounded_rectangle([880, 100, 1140, 400], radius=18, fill=BG2, outline=GOLD, width=3)
    d.text((908, 122), "TUE 26 NOV", font=font("DejaVuSans-Bold.ttf", 24), fill=INK)
    d.text((908, 164), "14:00  Pointless sync", font=font("DejaVuSans.ttf", 20), fill=MUTED)
    d.text((908, 196), "15:00  Status meeting", font=font("DejaVuSans.ttf", 20), fill=MUTED)
    d.text((908, 228), "16:00  Meeting about", font=font("DejaVuSans.ttf", 20), fill=MUTED)
    d.text((908, 256), "          meetings", font=font("DejaVuSans.ttf", 20), fill=MUTED)
    d.text((908, 318), "✕  DECLINED", font=font("DejaVuSans-Bold.ttf", 26), fill=RED)
    quote = "“I have to miss it — I’m the one doing the thing we’re meeting about.”"
    lines = wrap(d, quote, font("DejaVuSans.ttf", 34), 780)
    y = 292
    for ln in lines:
        d.text((64, y), ln, font=font("DejaVuSans.ttf", 34), fill=GOLD_SOFT)
        y += 48
    d.text((64, 500), "One line · 68 characters · 24/25 in a 28-candidate knockout",
           font=font("DejaVuSans.ttf", 26), fill=MUTED)
    img.save(os.path.join(ASSETS, "hero.png"))


def shot_calendar():
    img, d = base(800, 450)
    d.text((48, 36), "The invite that started it", font=font("DejaVuSans-Bold.ttf", 34), fill=INK)
    d.rounded_rectangle([48, 100, 752, 352], radius=16, fill=BG2, outline=GOLD, width=2)
    rows = [("09:00", "Daily standup", MUTED), ("11:00", "Sync about the sync", MUTED),
            ("14:00", "Pointless meeting", RED), ("16:30", "Pre-meeting (the meeting)", MUTED)]
    y = 118
    for t, label, col in rows:
        d.text((80, y), t, font=font("DejaVuSansMono-Bold.ttf", 28), fill=GOLD_SOFT)
        d.text((220, y), label, font=font("DejaVuSans.ttf", 28), fill=col)
        y += 46
    d.text((80, 308), "14:00  →  DECLINED", font=font("DejaVuSans-Bold.ttf", 28), fill=RED)
    d.text((48, 372), "One of these had to go. It was never the work.",
           font=font("DejaVuSans.ttf", 22), fill=MUTED)
    img.save(os.path.join(ASSETS, "shot-1.png"))


def shot_chat():
    img, d = base(800, 450)
    d.text((48, 36), "The excuse, as sent", font=font("DejaVuSans-Bold.ttf", 34), fill=INK)
    # chat bubble
    d.rounded_rectangle([48, 110, 752, 300], radius=20, fill=BG2, outline=GOLD, width=2)
    lines = wrap(d, "I have to miss it — I’m the one doing the thing we’re meeting about.",
                 font("DejaVuSans.ttf", 32), 620)
    y = 140
    for ln in lines:
        d.text((84, y), ln, font=font("DejaVuSans.ttf", 32), fill=INK)
        y += 46
    d.text((84, 250), "You · 13:58 · to #pointless-meeting",
           font=font("DejaVuSans.ttf", 22), fill=MUTED)
    d.text((48, 330), "✓ Seen by 14 people  ·  0 objections  ·  14 nods of recognition",
           font=font("DejaVuSans.ttf", 24), fill=GREEN)
    img.save(os.path.join(ASSETS, "shot-2.png"))


def shot_tournament():
    img, d = base(800, 450)
    d.text((48, 36), "28 candidates in, one line out", font=font("DejaVuSans-Bold.ttf", 34), fill=INK)
    stages = [("28", "candidates", "10 devices"), ("8", "seeds", "scored /25"),
              ("4", "semis", "knockout"), ("1", "winner", "24/25")]
    x = 48
    for i, (num, label, sub) in enumerate(stages):
        d.rounded_rectangle([x, 120, x + 160, 300], radius=14, fill=BG2, outline=GOLD, width=2)
        d.text((x + 80, 140), num, font=font("DejaVuSans-Bold.ttf", 64), fill=GOLD,
               anchor="ma")
        d.text((x + 80, 215), label, font=font("DejaVuSans-Bold.ttf", 20), fill=INK, anchor="ma")
        d.text((x + 80, 250), sub, font=font("DejaVuSans.ttf", 20), fill=MUTED, anchor="ma")
        if i < len(stages) - 1:
            d.text((x + 165, 195), "→", font=font("DejaVuSans-Bold.ttf", 36), fill=GOLD)
        x += 176
    caption = "Judged on the brief, in order: on-topic → punch → truth → tight → fresh."
    for j, ln in enumerate(wrap(d, caption, font("DejaVuSans.ttf", 24), 700)):
        d.text((48, 330 + j * 32), ln, font=font("DejaVuSans.ttf", 24), fill=MUTED)
    img.save(os.path.join(ASSETS, "shot-3.png"))


def shot_terminal():
    img, d = base(800, 450)
    d.text((48, 36), "Deterministic by design", font=font("DejaVuSans-Bold.ttf", 34), fill=INK)
    d.rounded_rectangle([48, 100, 752, 336], radius=16, fill=(10, 12, 16), outline=GOLD, width=2)
    lines = [
        ("$ ", "python3 main.py", INK),
        ("", "entry.txt written — 68 characters", GREEN),
        ("$ ", "sha256sum entry.txt  # run 1 and run 2", INK),
        ("", "df57c2da…3f1f46  (identical)", GREEN),
        ("", "gate: 1–200 chars ✓  UTF-8 ✓  not blank ✓", GREEN),
    ]
    y = 118
    for prompt, text, col in lines:
        d.text((80, y), prompt, font=font("DejaVuSansMono-Bold.ttf", 26), fill=GOLD_SOFT)
        d.text((80 + d.textlength(prompt, font=font("DejaVuSansMono-Bold.ttf", 26)), y),
               text, font=font("DejaVuSansMono.ttf", 26), fill=col)
        y += 40
    d.text((48, 360), "Pure stdlib. No clock, no random, no network.",
           font=font("DejaVuSans.ttf", 24), fill=MUTED)
    img.save(os.path.join(ASSETS, "shot-4.png"))


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)
    hero()
    shot_calendar()
    shot_chat()
    shot_tournament()
    shot_terminal()
    for f in sorted(os.listdir(ASSETS)):
        p = os.path.join(ASSETS, f)
        im = Image.open(p)
        print(f, im.size, os.path.getsize(p), "bytes")
