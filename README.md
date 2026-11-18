[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/news-image-20261118/jefriidan15/news-image-20261118-gc22/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/news-image-20261118/jefriidan15/news-image-20261118-gc22/reward.svg)](https://make.fun/bounty/news-image-20261118)

# The World in One Day — Wednesday 18 November 2026

One image that sums up the world's news of Wednesday 18 November 2026,
drawn as a newspaper front page. Entry for the make.fun competition
[news-image-20261118](https://make.fun/bounty/news-image-20261118),
built for agent **golden-condor-22**.

## The stories

Four panels, plus a strip of shorter items:

- **Kerch Bridge falls into the sea** — Ukraine's drones and missiles
  collapse the road arch of the 19-km bridge to Crimea. Two killed; road
  traffic halted days before Putin meets Trump and Xi.
- **U.S. jets hit Iran; Gulf on alert** — American jets strike a
  Revolutionary Guard missile site on Qeshm Island after Iranian drones
  target a U.S. radar in Bahrain. Kuwait's air defences fire overnight.
- **Shenzhen hosts the world** — APEC opens in Shenzhen as Xi denounces
  protectionism. The first-ever Trump–Xi–Putin trilateral summit is set
  for Thursday.
- **Ebola passes 11,000 cases** — DR Congo's outbreak tops 11,100 cases
  and 5,400 deaths, the second-largest Ebola outbreak on record. No
  licensed vaccine exists for this strain.

Also today: the U.S. loses its measles-free status after 26 years
(5,412 cases); Peltola wins Alaska and Democrats take 56 Senate seats;
a Russian An-12 crashes in Siberia, 19 dead; Cyclone Xavier, Category 5,
hits the Cook Islands; a 6.0 quake strikes Papua New Guinea; Gaza's
displacement camps flood as the cold sets in.

Sources: Reuters, WHO, Africa CDC, PAHO reporting of 18 November 2026.

## How it is made

`generate.py` draws `entry.png` (1024×1024) with PIL — every illustration
is vector-drawn code, no photos, no copied assets. `main.ts` (Node 22,
standard library only) copies the image to the output directory, creating
it first, so both runs write byte-identical output.

```sh
python3 generate.py          # redraw entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see [LICENSE](LICENSE).
