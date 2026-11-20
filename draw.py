#!/usr/bin/env python3
"""Draw the news-image-20261120 entry: a one-page newspaper front page
summing up Friday 20 November 2026. Writes entry.png (1024x1024, PNG)
next to this file. Run: python3 draw.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 229)
INK = (22, 32, 54)
RED = (176, 42, 28)
GOLD = (197, 148, 52)
BODY = (58, 58, 58)
RULE = (198, 188, 164)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def center(draw, cx, y, text, fnt, fill):
    draw.text((cx, y), text, font=fnt, fill=fill, anchor="ma")


def draw_us_flag(d, x, y, w, h):
    stripe = h / 13.0
    for i in range(13):
        if i % 2 == 0:
            d.rectangle([x, y + i * stripe, x + w, y + (i + 1) * stripe],
                        fill=(178, 34, 52))
    d.rectangle([x, y, x + w * 0.4, y + stripe * 7], fill=(28, 48, 94))
    for r in range(4):
        for c in range(5):
            sx = x + 6 + c * (w * 0.4 - 12) / 4
            sy = y + 5 + r * (stripe * 7 - 10) / 3
            d.ellipse([sx, sy, sx + 3, sy + 3], fill=WHITE)


def draw_cn_flag(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    cx, cy = x + w * 0.22, y + h * 0.28
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(255, 222, 0))
    for dx, dy in [(0.42, 0.12), (0.52, 0.28), (0.48, 0.48), (0.32, 0.52)]:
        sx, sy = x + w * dx, y + h * dy
        d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 222, 0))


def draw_ru_flag(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 3], fill=(240, 240, 240))
    d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(0, 57, 166))
    d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(213, 0, 50))


def draw_globe(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(214, 230, 240),
              outline=INK, width=4)
    d.ellipse([cx - r * 0.55, cy - r, cx + r * 0.55, cy + r],
              outline=(90, 130, 160), width=2)
    d.line([cx - r, cy, cx + r, cy], fill=(90, 130, 160), width=2)
    d.arc([cx - r, cy - r * 0.45, cx + r, cy + r * 0.45],
          start=0, end=180, fill=(90, 130, 160), width=2)
    d.arc([cx - r, cy - r * 0.45, cx + r, cy + r * 0.45],
          start=180, end=360, fill=(90, 130, 160), width=2)


def draw_chart(d, cx, cy, s):
    x, y, w, h = cx - s, cy - s * 0.6, 2 * s, s * 1.2
    pts = [(x, y + h * 0.8), (x + w * 0.3, y + h * 0.55),
           (x + w * 0.5, y + h * 0.65), (x + w * 0.75, y + h * 0.25),
           (x + w, y + h * 0.1)]
    d.line(pts, fill=(27, 120, 60), width=5, joint="curve")
    hx, hy = x + w, y + h * 0.1
    d.polygon([(hx, hy), (hx - 16, hy + 2), (hx - 4, hy + 16)],
              fill=(27, 120, 60))


def draw_drone(d, cx, cy, s):
    d.rounded_rectangle([cx - s * 0.5, cy - s * 0.18, cx + s * 0.5,
                         cy + s * 0.18], radius=8, fill=INK)
    for sx in (-1, 1):
        for sy in (-1, 1):
            ax, ay = cx + sx * s * 0.75, cy + sy * s * 0.4
            d.ellipse([ax - 5, ay - 5, ax + 5, ay + 5], fill=INK)
            d.line([cx + sx * s * 0.4, cy + sy * s * 0.15, ax, ay],
                   fill=INK, width=3)
            d.line([ax - s * 0.35, ay, ax + s * 0.35, ay], fill=INK, width=3)


def draw_dome(d, cx, cy, s):
    d.arc([cx - s, cy - s * 0.7, cx + s, cy + s * 0.7], start=180, end=360,
          fill=INK, width=4)
    d.line([cx - s, cy, cx + s, cy], fill=INK, width=4)
    for i in range(5):
        px = cx - s * 0.8 + i * s * 0.4
        d.line([px, cy, px, cy + s * 0.55], fill=INK, width=3)
    d.line([cx - s, cy + s * 0.55, cx + s, cy + s * 0.55], fill=INK, width=4)


def draw_frame(d, cx, cy, s):
    d.rectangle([cx - s, cy - s * 0.75, cx + s, cy + s * 0.75],
                outline=GOLD, width=5)
    d.rectangle([cx - s + 8, cy - s * 0.75 + 8, cx + s - 8, cy + s * 0.75 - 8],
                fill=(252, 212, 90))
    d.ellipse([cx - s * 0.35, cy - s * 0.4, cx + s * 0.35, cy + s * 0.3],
              fill=(232, 120, 40))
    d.arc([cx - s * 0.6, cy - s * 0.1, cx + s * 0.6, cy + s * 0.6],
          start=200, end=340, fill=(176, 42, 28), width=4)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    d.rectangle([0, 0, W, 122], fill=INK)
    center(d, W // 2, 14, "THE WORLD IN ONE IMAGE", SERIF_B(62), WHITE)
    center(d, W // 2, 86, "F R I D A Y  ·  2 0  N O V E M B E R  2 0 2 6",
           SANS_B(22), GOLD)
    d.line([0, 122, W, 122], fill=GOLD, width=4)

    # ---- Lead story: trilateral summit ----
    d.text((48, 142), "SUMMIT IN CHINA", font=SANS_B(24), fill=RED)
    headline = "TRUMP, PUTIN AND XI SIGN 'PEACE DECLARATION'"
    y = 176
    for ln in wrap(d, headline, SERIF_B(52), 600):
        d.text((48, y), ln, font=SERIF_B(52), fill=INK)
        y += 62
    summary = ("The three leaders hold the first-ever trilateral summit "
               "in China and issue a joint peace declaration. European "
               "leaders watch warily as the three powers talk peace.")
    y = 372
    for ln in wrap(d, summary, SANS(23), 600):
        d.text((48, y), ln, font=SANS(23), fill=BODY)
        y += 31

    # Globe + three flags on the right
    draw_globe(d, 830, 235, 85)
    d.text((700, 330), "First trilateral summit", font=SANS(19),
           fill=(120, 110, 90))
    fy = 360
    for fn, label in ((draw_us_flag, "USA"), (draw_cn_flag, "CHINA"),
                      (draw_ru_flag, "RUSSIA")):
        fn(d, 700, fy, 66, 40)
        d.text((778, fy + 6), label, font=SANS_B(20), fill=INK)
        fy += 48

    d.line([48, 496, W - 48, 496], fill=RULE, width=2)

    # ---- Middle band: two stories ----
    d.text((48, 516), "THE HAGUE", font=SANS_B(22), fill=RED)
    y = 550
    for ln in wrap(d, "WORLD COURT: MYANMAR GUILTY OF GENOCIDE",
                   SERIF_B(28), 420):
        d.text((48, y), ln, font=SERIF_B(28), fill=INK)
        y += 36
    y += 6
    for ln in wrap(d, "The International Court of Justice rules 9-6 that "
                      "Myanmar committed genocide against the Rohingya in "
                      "Rakhine state.", SANS(20), 420):
        d.text((48, y), ln, font=SANS(20), fill=BODY)
        y += 26

    d.text((536, 516), "COP31 CLIMATE TALKS", font=SANS_B(22), fill=RED)
    y = 550
    for ln in wrap(d, "FOSSIL FUELS CUT FROM DRAFT DEAL", SERIF_B(28), 420):
        d.text((536, y), ln, font=SERIF_B(28), fill=INK)
        y += 36
    y += 6
    for ln in wrap(d, "Near-final climate texts drop any mention of a "
                      "fossil-fuel transition, drawing outrage as the "
                      "talks enter crunch time.", SANS(20), 420):
        d.text((536, y), ln, font=SANS(20), fill=BODY)
        y += 26

    d.line([48, 752, W - 48, 752], fill=RULE, width=2)
    d.line([512, 516, 512, 732], fill=RULE, width=2)

    # ---- Bottom band: four stories ----
    cols = [
        ("MARKETS", "ANTHROPIC SOARS 34% ON DEBUT",
         "First pure-AI listing; valued near $2 trillion.", draw_chart),
        ("UKRAINE", "UK SENDS 1,000 DRONES TO UKRAINE",
         "Britain pledges drones in a GBP 260m package.", draw_drone),
        ("WASHINGTON", "SENATE REJECTS IRAN VOTE, 51-48",
         "War-powers vote fails; war cost tops $48bn.", draw_dome),
        ("ART", "VAN GOGH SELLS FOR $190.4M",
         "Record price after a dispute over the work.", draw_frame),
    ]
    col_w = 232
    for i, (kick, head, summ, icon) in enumerate(cols):
        x = 48 + i * (col_w + 10)
        d.text((x, 766), kick, font=SANS_B(19), fill=RED)
        icon(d, x + 36, 806, 28)
        y = 834
        for ln in wrap(d, head, SERIF_B(22), col_w):
            d.text((x, y), ln, font=SERIF_B(22), fill=INK)
            y += 26
        y += 4
        for ln in wrap(d, summ, SANS(16), col_w):
            d.text((x, y), ln, font=SANS(16), fill=BODY)
            y += 20

    # ---- Footer strip ----
    d.rectangle([0, 952, W, H], fill=INK)
    ticker = ("ALSO:  Pete Rose pardoned  ·  Potatoes grown in moon soil  ·  "
              "65,000 Gaza tents wait  ·  Meta rethinks net-zero")
    y = 960
    for ln in wrap(d, ticker, SANS(19), W - 96):
        d.text((48, y), ln, font=SANS(19), fill=WHITE)
        y += 24
    center(d, W // 2, 1004, "All stories as reported on Friday 20 November 2026",
           SANS(13), (170, 165, 150))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
