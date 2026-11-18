#!/usr/bin/env python3
"""Draws entry.png: a one-page newspaper front page summing up
Wednesday 18 November 2026. All artwork is vector-drawn with PIL;
no photos, no copied assets. 1024x1024, deterministic output.
Revision 2: strip extended to the bottom edge with the source credit on
the label line; summit flag labels backed so the skyline never covers them;
Gulf label right-aligned so it is never clipped."""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1024, 1024
PAPER = (247, 243, 234)
NAVY = (20, 33, 61)
GOLD = (214, 164, 65)
RED = (178, 34, 34)
INK = (24, 24, 24)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def center(draw, cx, y, text, fnt, fill):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text, font=fnt, fill=fill)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 148], fill=NAVY)
d.rectangle([0, 148, W, 152], fill=GOLD)
center(d, W // 2, 14, "THE WORLD IN ONE DAY", font(SERIF_B, 58), WHITE)
center(d, W // 2, 84, "WEDNESDAY  ·  18 NOVEMBER 2026", font(SANS_B, 30), GOLD)
center(d, W // 2, 122, "One day. One picture. Every story that mattered.",
       font(SERIF, 20), (200, 205, 215))

# ---------- panels ----------
PANELS = [
    dict(kicker="UKRAINE  ·  RUSSIA", tag="WAR",
         head="Kerch Bridge falls into the sea",
         body="Ukraine's drones and missiles collapse the road arch of the 19-km bridge to Crimea. Two killed; road traffic halted days before Putin meets Trump and Xi.",
         art="bridge"),
    dict(kicker="GULF  ·  IRAN  ·  U.S.", tag="ESCALATION",
         head="U.S. jets hit Iran; Gulf on alert",
         body="American jets strike a Revolutionary Guard missile site on Qeshm Island after Iranian drones target a U.S. radar in Bahrain. Kuwait's defences fire overnight.",
         art="gulf"),
    dict(kicker="CHINA  ·  APEC", tag="SUMMIT",
         head="Shenzhen hosts the world",
         body="APEC opens in Shenzhen as Xi denounces protectionism. The first-ever Trump–Xi–Putin trilateral summit is set for Thursday.",
         art="summit"),
    dict(kicker="HEALTH  ·  AFRICA", tag="OUTBREAK",
         head="Ebola passes 11,000 cases",
         body="DR Congo's outbreak tops 11,100 cases and 5,400 deaths — the second-largest Ebola outbreak on record. No licensed vaccine exists for this strain.",
         art="ebola"),
]

PX, PY, PW, PH, GAP = 16, 164, 496, 352, 16
ART_H = 128

def art_bridge(x0, y0, w, h):
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=(176, 196, 214))
    d.rectangle([x0, y0 + 88, x0 + w, y0 + h], fill=(64, 110, 140))  # sea
    # deck left + right, gap in middle where arch fell
    d.rectangle([x0, y0 + 78, x0 + 190, y0 + 88], fill=(60, 60, 66))
    d.rectangle([x0 + 306, y0 + 78, x0 + w, y0 + 88], fill=(60, 60, 66))
    # fallen segment tilted into water
    d.polygon([(x0 + 205, y0 + 92), (x0 + 300, y0 + 104), (x0 + 292, y0 + 116), (x0 + 200, y0 + 104)], fill=(80, 80, 86))
    # towers
    d.rectangle([x0 + 60, y0 + 18, x0 + 72, y0 + 80], fill=(50, 50, 56))
    d.rectangle([x0 + 420, y0 + 18, x0 + 432, y0 + 80], fill=(50, 50, 56))
    # cables
    for tx in (66, 426):
        d.line([x0 + tx, y0 + 20, x0 + 190, y0 + 78], fill=(50, 50, 56), width=2)
        d.line([x0 + tx, y0 + 20, x0 + 306, y0 + 78], fill=(50, 50, 56), width=2)
    # smoke + blast
    for cx, cy, r in ((248, 66, 16), (262, 52, 12), (236, 50, 10)):
        d.ellipse([x0 + cx - r, y0 + cy - r, x0 + cx + r, y0 + cy + r], fill=(120, 120, 122))
    d.ellipse([x0 + 238, y0 + 74, x0 + 258, y0 + 94], fill=(232, 120, 40))
    d.ellipse([x0 + 243, y0 + 79, x0 + 253, y0 + 89], fill=(255, 200, 60))

def art_gulf(x0, y0, w, h):
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=(16, 68, 92))
    # island
    d.polygon([(x0 + 150, y0 + 96), (x0 + 210, y0 + 62), (x0 + 300, y0 + 58),
               (x0 + 350, y0 + 92), (x0 + 320, y0 + 118), (x0 + 190, y0 + 120)],
              fill=(196, 164, 110))
    d.text((x0 + 218, y0 + 82), "QESHM", font=font(SANS_B, 15), fill=(90, 60, 20))
    # jet silhouette
    d.polygon([(x0 + 60, y0 + 30), (x0 + 110, y0 + 22), (x0 + 118, y0 + 28),
               (x0 + 96, y0 + 34), (x0 + 70, y0 + 38)], fill=(230, 230, 230))
    # missile streaks to island
    for i, yy in enumerate((34, 44, 54)):
        d.line([x0 + 118, y0 + yy, x0 + 205, y0 + 66 + i * 6], fill=(255, 200, 60), width=3)
    # bursts on island
    for cx, cy in ((230, 70), (270, 66), (300, 78)):
        d.ellipse([x0 + cx - 9, y0 + cy - 9, x0 + cx + 9, y0 + cy + 9], fill=(255, 140, 30))
        d.ellipse([x0 + cx - 4, y0 + cy - 4, x0 + cx + 4, y0 + cy + 4], fill=(255, 220, 90))
    # drone dots + radar arcs over Bahrain (right)
    d.ellipse([x0 + 420, y0 + 30, x0 + 430, y0 + 40], fill=(255, 255, 255))
    d.ellipse([x0 + 448, y0 + 44, x0 + 458, y0 + 54], fill=(255, 255, 255))
    d.arc([x0 + 400, y0 + 20, x0 + 470, y0 + 90], 200, 340, fill=(255, 255, 255), width=2)
    lab = "BAHRAIN · KUWAIT"
    d.text((x0 + PW - 16 - d.textlength(lab, font=font(SANS_B, 13)), y0 + 98), lab,
           font=font(SANS_B, 13), fill=(220, 230, 235))

def art_summit(x0, y0, w, h):
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=(238, 214, 160))
    d.ellipse([x0 + 400, y0 + 8, x0 + 452, y0 + 60], fill=(232, 150, 60))  # sun
    # skyline (kept short so flag labels stay on open sky)
    base = y0 + h
    for bx, bw, bh in ((0, 46, 40), (52, 34, 56), (92, 52, 46), (150, 30, 62),
                       (186, 44, 42), (236, 36, 58), (278, 50, 48), (334, 40, 64),
                       (380, 44, 44), (430, 66, 60)):
        d.rectangle([x0 + bx, base - bh, x0 + bx + bw, base], fill=(52, 58, 74))
    # three flag bars
    flags = [((178, 34, 34), "U.S."), ((200, 30, 30), "CHINA"), ((30, 70, 160), "RUSSIA")]
    for i, (col, lab) in enumerate(flags):
        fx = x0 + 96 + i * 106
        d.rectangle([fx, y0 + 14, fx + 86, y0 + 44], fill=col)
        d.rectangle([fx, y0 + 14, fx + 86, y0 + 24], fill=(255, 255, 255)) if i in (0, 2) else None
        lw = d.textlength(lab, font=font(SANS_B, 14))
        d.rectangle([fx + 43 - lw / 2 - 4, y0 + 48, fx + 43 + lw / 2 + 4, y0 + 68], fill=(238, 214, 160))
        center(d, fx + 43, y0 + 49, lab, font(SANS_B, 14), NAVY)
    d.text((x0 + 12, y0 + 8), "APEC · SHENZHEN", font=font(SANS_B, 14), fill=(90, 60, 20))

def art_ebola(x0, y0, w, h):
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=(112, 22, 28))
    # virions
    import math
    for cx, cy, r in ((90, 62, 26), (250, 48, 20), (400, 70, 30), (170, 96, 16), (330, 104, 14)):
        for k in range(10):
            a = math.pi * 2 * k / 10
            d.line([x0 + cx + math.cos(a) * r, y0 + cy + math.sin(a) * r,
                    x0 + cx + math.cos(a) * (r + 12), y0 + cy + math.sin(a) * (r + 12)],
                   fill=(232, 120, 110), width=3)
        d.ellipse([x0 + cx - r, y0 + cy - r, x0 + cx + r, y0 + cy + r], fill=(196, 60, 52))
        d.ellipse([x0 + cx - r // 2, y0 + cy - r // 2, x0 + cx + r // 2, y0 + cy + r // 2], fill=(150, 40, 38))
    # white cross badge
    d.rectangle([x0 + 448, y0 + 8, x0 + 488, y0 + 48], fill=WHITE)
    d.rectangle([x0 + 462, y0 + 14, x0 + 474, y0 + 42], fill=(178, 34, 34))
    d.rectangle([x0 + 454, y0 + 22, x0 + 482, y0 + 34], fill=(178, 34, 34))

ART = {"bridge": art_bridge, "gulf": art_gulf, "summit": art_summit, "ebola": art_ebola}

for i, p in enumerate(PANELS):
    x0 = PX + (i % 2) * (PW + GAP)
    y0 = PY + (i // 2) * (PH + GAP)
    d.rectangle([x0, y0, x0 + PW, y0 + PH], fill=WHITE, outline=(200, 196, 186), width=2)
    ART[p["art"]](x0 + 2, y0 + 2, PW - 4, ART_H)
    ty = y0 + ART_H + 12
    d.text((x0 + 14, ty), p["kicker"], font=font(SANS_B, 17), fill=RED)
    tw = d.textlength(p["tag"], font=font(SANS_B, 15))
    d.rectangle([x0 + PW - tw - 26, ty - 2, x0 + PW - 12, ty + 20], fill=NAVY)
    d.text((x0 + PW - tw - 19, ty), p["tag"], font=font(SANS_B, 15), fill=GOLD)
    hy = ty + 28
    for ln in wrap(d, p["head"], font(SERIF_B, 27), PW - 28):
        d.text((x0 + 14, hy), ln, font=font(SERIF_B, 27), fill=INK)
        hy += 33
    by = hy + 6
    for ln in wrap(d, p["body"], font(SANS, 19), PW - 28):
        d.text((x0 + 14, by), ln, font=font(SANS, 19), fill=(60, 60, 60))
        by += 25

# ---------- bottom strip ----------
SY = 896
d.rectangle([0, SY, W, H], fill=NAVY)
d.text((16, SY + 10), "ALSO TODAY", font=font(SANS_B, 20), fill=GOLD)
src = "Sources: Reuters · WHO · Africa CDC · PAHO"
d.text((W - 16 - d.textlength(src, font=font(SANS, 15)), SY + 13), src,
       font=font(SANS, 15), fill=(170, 176, 186))
strip = ("U.S. loses measles-free status after 26 years — 5,412 cases  •  "
         "Peltola wins Alaska; Democrats take 56 Senate seats  •  "
         "Russian An-12 crashes in Siberia, 19 dead  •  "
         "Cyclone Xavier, Cat 5, hits the Cook Islands  •  "
         "6.0 quake strikes Papua New Guinea  •  "
         "Gaza camps flooded as cold sets in")
sy = SY + 40
for ln in wrap(d, strip, font(SANS, 19), W - 32):
    d.text((16, sy), ln, font=font(SANS, 19), fill=(225, 228, 232))
    sy += 26

img.save("/root/makefun-work/news-image-20261118-gc22/entry.png", optimize=True)
print("saved")
