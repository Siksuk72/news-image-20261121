#!/usr/bin/env python3
"""Render the front page for news-image-20261121.

Saturday 21 November 2026, summed up on one page: "THE WORLD TODAY",
a newspaper front page painted with Pillow. The lead is the Russian
missiles that landed in Poland during the overnight barrage on Ukraine;
a "by the numbers" strip, six continent sections and an also-today
strip carry the other 27 stories -- thirty in all.

The dawn-scramble photo is an AI-made illustration (hero.png, shipped
in this repo). It is cropped into its panel here, so rendering is
deterministic: run this file twice and entry.png comes out
byte-identical.

Run:  python3 draw.py    (writes entry.png next to this file)
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (250, 243, 227)
INK = (20, 20, 20)
MUTE = (74, 74, 74)
PALE = (104, 100, 88)
RULE = (120, 110, 88)
NAVY = (24, 48, 84)
CRIMSON = (150, 28, 28)
TEAL = (32, 84, 110)
GOLD = (176, 128, 20)
WHITE = (255, 255, 255)
BAND = (238, 230, 208)

FONTS = "/usr/share/fonts/truetype/dejavu/"
FACES = {
    "serif_b": "DejaVuSerif-Bold.ttf",
    "serif": "DejaVuSerif.ttf",
    "sans_b": "DejaVuSans-Bold.ttf",
    "sans": "DejaVuSans.ttf",
}
_fonts = {}


def face(name, size):
    key = (name, size)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(FONTS + FACES[name], size)
    return _fonts[key]


def wrap(draw, text, font, width, max_lines=None):
    """Greedy word wrap; optionally cap the line count with an ellipsis."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines and draw.textlength(lines[-1] + " ...", font=font) > width:
            lines[-1] = lines[-1].rsplit(" ", 1)[0] if " " in lines[-1] else ""
        lines[-1] = (lines[-1] + " ...").strip()
    return lines


def para(draw, x, y, text, font, width, leading, color, max_lines=None):
    """Draw a wrapped paragraph; return the y just below it."""
    for line in wrap(draw, text, font, width, max_lines):
        draw.text((x, y), line, font=font, fill=color)
        y += leading
    return y


class Page:
    def __init__(self):
        self.img = Image.new("RGB", (W, H), PAPER)
        self.d = ImageDraw.Draw(self.img)

    def hline(self, y, x0=24, x1=1000, color=RULE, width=1):
        self.d.line([(x0, y), (x1, y)], fill=color, width=width)

    def vline(self, x, y0, y1, color=RULE):
        self.d.line([(x, y0), (x, y1)], fill=color, width=1)

    def masthead(self):
        d = self.d
        title = "THE WORLD TODAY"
        f = face("serif_b", 60)
        tw = d.textlength(title, font=f)
        d.text(((W - tw) / 2, 12), title, font=f, fill=INK)
        self.hline(88, width=2)
        self.hline(92)
        tag = "SATURDAY, 21 NOVEMBER 2026   \u2022   30 STORIES   \u2022   6 CONTINENTS   \u2022   ONE IMAGE"
        tf = face("sans_b", 13)
        tw = d.textlength(tag, font=tf)
        d.text(((W - tw) / 2, 98), tag, font=tf, fill=MUTE)

    def lead(self):
        d = self.d
        # Photo panel, left.
        hero = Image.open(os.path.join(os.path.dirname(__file__), "hero.png"))
        hero = hero.convert("RGB")
        pw, ph = 486, 240
        iw, ih = hero.size
        scale = max(pw / iw, ph / ih)
        hero = hero.resize((int(iw * scale) + 1, int(ih * scale) + 1), Image.LANCZOS)
        ox = (hero.size[0] - pw) // 2
        oy = (hero.size[1] - ph) // 2
        self.img.paste(hero.crop((ox, oy, ox + pw, oy + ph)), (24, 122))
        d.rectangle([24, 122, 24 + pw, 122 + ph], outline=INK, width=1)
        cap = "NATO jets scramble as Russian weapons cross into Poland.  Illustration: AI-made."
        para(d, 24, 368, cap, face("serif", 10), pw, 13, PALE, max_lines=1)

        # Lead text, right of the photo.
        x = 534
        d.text((x, 122), "LEAD  \u2014  POLAND / NATO", font=face("sans_b", 12), fill=CRIMSON)
        y = para(d, x, 144, "RUSSIAN MISSILES LAND IN POLAND",
                 face("serif_b", 30), 466, 35, INK, max_lines=2)
        y = para(d, x, y + 4,
                 "Two cruise missiles and a suspected jet drone come down "
                 "in south-east Poland during a huge overnight barrage on "
                 "Ukraine. PM Donald Tusk calls it a deliberate provocation; "
                 "NATO chief Mark Rutte calls it a grave violation.",
                 face("serif", 13), 466, 17, INK, max_lines=5)
        y = para(d, x, y + 8,
                 "400+ drones and 110 missiles fired at Ukraine overnight; "
                 "at least 8 killed. Jets scrambled, Patriots armed \u2014 "
                 "but no shots fired in three minutes of doubt.",
                 face("sans", 11), 466, 15, MUTE, max_lines=3)
        self.hline(392)

        # Second and third leads, full width under the photo.
        y = 402
        d.text((24, y), "MARKETS", font=face("sans_b", 12), fill=NAVY)
        para(d, 24, y + 17, "Wall Street slumps: the S&P 500 and the Dow enter "
             "correction; the Nasdaq falls 5.28% and Nvidia drops 14%.",
             face("serif_b", 13), 470, 17, INK, max_lines=2)
        d.text((530, y), "CLIMATE", font=face("sans_b", 12), fill=TEAL)
        para(d, 530, y + 17, "COP31 spills into overtime: fossil fuels stripped "
             "from the draft deal; activists warn of the \u201cworst COP ever\u201d.",
             face("serif_b", 13), 470, 17, INK, max_lines=2)
        self.hline(462)

    def numbers(self):
        d = self.d
        d.text((24, 472), "BY THE NUMBERS", font=face("sans_b", 12), fill=GOLD)
        stats = [
            ("400+", "drones fired at Ukraine in one night"),
            ("110", "missiles in the same barrage"),
            ("-5.28%", "Nasdaq fall on Friday"),
            ("323,000", "people fled South Kivu in 4 days"),
        ]
        x = 170
        for value, label in stats:
            d.text((x, 470), value, font=face("serif_b", 17), fill=CRIMSON)
            d.text((x, 494), label, font=face("sans", 10), fill=MUTE)
            x += 215
        self.hline(516)

    def continent(self, x, y, w, name, color, stories):
        d = self.d
        d.text((x, y), name, font=face("sans_b", 13), fill=color)
        self.hline(y + 20, x0=x, x1=x + w, color=color, width=2)
        yy = y + 27
        for head, body in stories:
            head_lines = wrap(d, head, face("sans_b", 11), w, max_lines=2)
            for line in head_lines:
                d.text((x, yy), line, font=face("sans_b", 11), fill=INK)
                yy += 14
            # A one-line headline earns the summary a second line.
            body_max = 2 if len(head_lines) == 1 else 1
            yy = para(d, x, yy + 1, body, face("sans", 10), w, 12, MUTE,
                      max_lines=body_max)
            yy += 6
        return yy

    def grid(self):
        cols = [
            ("NORTH AMERICA", NAVY, [
                ("Trump urges Nvidia to bring back Jensen Huang",
                 "The board says it has no plans to reinstate its former chief."),
                ("SEC probing Nvidia's accounting, Reuters reports",
                 "Two sources say the regulator is examining the books."),
                ("US wants a Ukraine peace deal by early January",
                 "The FT says Washington set the target for Kyiv and allies."),
                ("Banks hit by cyberattack on third-party vendors",
                 "JPMorgan, Visa and Mastercard say core payment networks are safe."),
            ]),
            ("EUROPE", CRIMSON, [
                ("Denmark foils Russian plot to kill rapper Kyivstoner",
                 "Two men charged; Russia's defence attache expelled."),
                ("UK and EU sign food, carbon and youth-mobility deals",
                 "Three deals sealed at a Brussels summit on Friday."),
                ("Paris shuts 16 metro stations for cost-of-living march",
                 "Act VI of the cost-of-living protests marches on Saturday."),
                ("EU adopts \u20ac1bn in military aid for Ukraine",
                 "Joint equipment buys through the European Peace Facility."),
            ]),
            ("ASIA", TEAL, [
                ("Cyclone Akvan crosses the Odisha coast",
                 "The storm comes ashore near Gopalpur with strong winds and rain."),
                ("World Court: Myanmar committed genocide",
                 "The ICJ finds the state responsible over the Rohingya in Rakhine."),
                ("India fight back in the Wellington Test",
                 "KL Rahul closes on a century; India reach 239-1 on day three."),
                ("India A crush Nepal by 306 runs",
                 "Nepal bowled out for 26 \u2014 among the lowest List A totals ever."),
            ]),
            ("AFRICA", GOLD, [
                ("Somalia orders the UAE ambassador out",
                 "Mogadishu gives the envoy 72 hours, citing a sovereignty breach."),
                ("Drones caused most civilian deaths in Sudan",
                 "The UN says over 80% of 1,390 civilian deaths in early 2026."),
                ("Congo offensive displaces 323,000 in four days",
                 "Families flee South Kivu after fighting that began on 6 November."),
                ("Tunisian rights defender jailed for five years",
                 "Sihem Ben Sedrine is sentenced in a case rights groups condemn."),
            ]),
            ("SOUTH AMERICA", NAVY, [
                ("Haiti police kill at least 34 suspected gang members",
                 "A raid on the capital targets gangs blamed for killings."),
                ("Bukele expected to formalise a third-term bid",
                 "El Salvador's president moves to extend his rule."),
                ("US backs Colombia resuming aerial coca spraying",
                 "Washington supports the plan despite lawmakers' concerns."),
                ("Argentina's Senate backs disability framework",
                 "The permanent framework passes unanimously, 71 senators in favour."),
            ]),
            ("OCEANIA", CRIMSON, [
                ("Webb finds the oldest close quasar pair",
                 "Two monster black holes seen 900 million years after the Big Bang."),
                ("Voyager 1 reaches one light-day from Earth",
                 "NASA's probe is 26 billion km out, 49 years after launch."),
                ("Potatoes grow a full life cycle in lunar soil",
                 "Oregon State trials point to food grown on the Moon."),
                ("Sandpapergate row engulfs Australian cricket",
                 "Hazlewood breaks his silence as Cummins' captaincy is questioned."),
            ]),
        ]
        col_w, gap = 310, 18
        row_y = [526, 740]
        for i, (name, color, stories) in enumerate(cols):
            row = i // 3
            col = i % 3
            x = 24 + col * (col_w + gap)
            self.continent(x, row_y[row], col_w, name, color, stories)
        self.hline(952)

    def also(self):
        d = self.d
        d.text((24, 960), "ALSO TODAY", font=face("sans_b", 12), fill=GOLD)
        items = [
            "Gold falls to a 14-month low, down 9.4% on the week.",
            "2027 Hyundai Elantra debuts at the Los Angeles Auto Show.",
            "Sensex rallies 898 points to 83,919.71 in Mumbai.",
        ]
        x = 150
        for item in items:
            para(d, x, 960, item, face("sans", 10), 270, 13, MUTE, max_lines=2)
            x += 290
        foot = "Sources: Reuters \u2022 AP \u2022 BBC \u2022 UN News \u2022 CBS \u2022 PANA \u2014 all stories reported 20\u201321 November 2026"
        ff = face("sans", 9)
        d.text(((W - d.textlength(foot, font=ff)) / 2, 1002), foot, font=ff, fill=PALE)

    def build(self):
        self.masthead()
        self.lead()
        self.numbers()
        self.grid()
        self.also()
        out = os.path.join(os.path.dirname(__file__), "entry.png")
        self.img.save(out, "PNG", optimize=True)
        print("wrote", out, self.img.size)


if __name__ == "__main__":
    Page().build()
