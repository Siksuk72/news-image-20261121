# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Siksuk72/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Siksuk72/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image that sums up the world's news of Saturday 21 November 2026.
It is a one-page newspaper front page: the drawing is done in code
with Python Pillow (`draw.py`), so every word is spelled right and
stays readable at ~300 px, and the photo of NATO jets scrambling at
dawn is an AI-made illustration (`hero.png`). `main.ts` (Node 22,
stdlib only) puts the finished picture at `/output/entry.png` for the
grader.

## What's on the page

- Masthead "THE WORLD TODAY" + "SATURDAY, 21 NOVEMBER 2026 • 30 STORIES • 6 CONTINENTS"
- 3 lead stories: Russian missiles land in Poland during the overnight barrage on Ukraine; Wall Street slides into correction as AI shares sell off; COP31 spills into overtime in Antalya.
- "BY THE NUMBERS" strip: 400+ drones, 110 missiles, Nasdaq −5.28%, 323,000 displaced in South Kivu.
- 6 continent sections × 4 stories each (24 stories).
- "ALSO TODAY" strip with 3 more briefs. Total: 30 stories.

## The 30 stories (all reported on 20–21 Nov 2026)

### Leads
1. Russian missiles land in Poland — two cruise missiles and a suspected jet drone come down in south-east Poland; Tusk calls it a deliberate provocation, NATO calls it a grave violation; 400+ drones and 110 missiles fired at Ukraine, at least 8 killed — Reuters/AP
2. Wall Street slumps: the S&P 500 and the Dow enter correction; the Nasdaq falls 5.28% and Nvidia drops about 14% — Reports
3. COP31 spills into overtime in Antalya: fossil fuels stripped from the draft deal; activists warn of the "worst COP ever" — Reuters/UN News

### North America
4. Trump urges Nvidia to bring back Jensen Huang; the board says it has no plans to reinstate him — Reports
5. SEC probing Nvidia's accounting, Reuters reports, citing two sources — Reuters
6. Trump administration wants a Ukraine peace deal by early January, the FT reports — FT
7. JPMorgan, Visa and Mastercard report a cyberattack on third-party vendors; core payment networks unaffected — Reports

### Europe
8. Denmark foils a Russian plot to kill Ukrainian-American rapper Kyivstoner; two men charged, Russia's defence attaché expelled — Reports
9. UK and EU sign food, carbon and youth-mobility deals at a Brussels summit — Reports
10. Paris shuts 16 metro stations for the cost-of-living march, Act VI, from République to Nation — Reports
11. EU Council adopts €1bn in military aid for Ukraine — Reports

### Asia
12. Cyclone Akvan crosses the Odisha coast near Gopalpur — Reports
13. World Court finds Myanmar committed genocide against the Rohingya — ICJ
14. India fight back in the Wellington Test: KL Rahul closes on a century, India 239-1 on day three — Reuters
15. India A crush Nepal by 306 runs; Nepal bowled out for 26 — Reports

### Africa
16. Somalia orders the UAE ambassador out within 72 hours, citing a sovereignty breach — Reports
17. UN: drones caused most civilian deaths in Sudan — over 80% of 1,390 in the first half of 2026 — UN
18. Congo offensive displaces 323,000 in South Kivu in four days — UN
19. Tunisian rights defender Sihem Ben Sedrine sentenced to five years in prison — PANA

### South America
20. Haiti police kill at least 34 suspected gang members in a raid on the capital — Reports
21. El Salvador's Bukele expected to formalise a bid for a third presidential term — Reports
22. US backs Colombia's plans to resume aerial coca spraying despite lawmakers' concerns — Reports
23. Argentina's Senate approves a permanent disability framework, unanimously, 71 senators in favour — Reports

### Oceania
24. Webb and Gemini North find the oldest known close quasar pair, 900 million years after the Big Bang — Reports
25. Voyager 1 reaches one light-day from Earth, 26 billion km out, 49 years after launch — NASA
26. Potatoes complete a full life cycle in simulated lunar soil — Oregon State University
27. Sandpapergate row engulfs Australian cricket as Hazlewood breaks his silence — Reports

### Also today
28. Gold falls to a 14-month low, down 9.4% on the week — Reports
29. 2027 Hyundai Elantra debuts at the Los Angeles Auto Show — Reports
30. Sensex rallies 898 points to 83,919.71 in Mumbai — Reports

## How it is built

`draw.py` renders `entry.png` (1024×1024, deterministic — run it twice
and the bytes are identical). `main.ts` copies that file to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` for a local
trial) and chmods it 0644. No network is used at build or run time.
