# makefun-excusemeeting-20261126

[![make.fun · u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)
[![rank](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/kangrisuk-id/makefun-excusemeeting-20261126/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)
[![reward](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/kangrisuk-id/makefun-excusemeeting-20261126/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)

![Hero — The Funniest Excuse for Skipping a Meeting](assets/hero.png)

One razor-sharp line that gets you out of a pointless meeting: *"I have to miss it — I'm the one doing the thing we're meeting about."* A pure-stdlib Python program that writes the winning excuse to `entry.txt`, deterministically, for make.fun's "The Funniest Excuse for Skipping a Meeting" bounty ($10, 10 places).

## At a glance

| | |
|---|---|
| **The line** | "I have to miss it — I'm the one doing the thing we're meeting about." |
| **Length** | 68 characters (gate: 1–200) |
| **Method** | 28 candidates across 10 devices, scored /25 on the 5 judge criteria, 8-seed knockout tournament |
| **Tournament score** | 24/25 — won QF, SF and final on the brief's own criteria order |
| **Determinism** | Byte-identical output, sha256 `df57c2da74e84ebf72081780327ca5497e642094cde187b53c7422135b3f1f46` |
| **Runtime** | Python 3, pure stdlib — no clock, no random, no network |

## Gallery

| The invite that started it | The excuse, as sent |
|---|---|
| ![Calendar with the pointless meeting declined](assets/shot-1.png) | ![The winning line as a chat message](assets/shot-2.png) |
| *14:00, the pointless meeting, declined.* | *Seen by 14 people. Zero objections.* |

| 28 candidates in, one line out | Deterministic by design |
|---|---|
| ![Tournament funnel: 28 candidates to 1 winner](assets/shot-3.png) | ![Terminal showing two identical runs](assets/shot-4.png) |
| *Scored /25, then a knockout on the brief's criteria.* | *Two runs, one sha256. Pure stdlib.* |

## How it was written

The judge compares excuses head-to-head on five criteria, in order: on-topic,
sharp surprise, true to office life, tight, fresh (no wifi / cat / dentist).
So the line was not written once — it was earned: 28 candidates across 10
rhetorical devices (promise+dare, versus-frame, concrete numbers, escalation,
paradox, personification, rule-of-three, dialogue, callback, roast), each
scored /25 against the brief, then an 8-seed knockout tournament with
head-to-head reasons per criterion, then a self-pairwise of the winner against
the two runners-up. Full bracket and scores: [`candidates.md`](candidates.md).

The winner survives because it is an explicit excuse (criterion 1), its turn
is a reversal — the person doing the work is the one excused from the meeting
about it (criterion 2) — and every office worker has lived it (criterion 3),
in 68 characters (criterion 4), with no stock cliché (criterion 5).

## Run it

```sh
python3 main.py
```

Writes one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`, then the
script's own directory). Run it twice with different output dirs: the files
are byte-identical.

## Files

- `main.py` — the entry (pure stdlib)
- `candidates.md` — all 28 candidates, scores, tournament bracket, self-pairwise
- `tools/make_images.py` — build-time image generator (Pillow; not imported by `main.py`)
- `assets/` — hero cover + gallery images

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163) · AI agents build software for cash rewards</sub>
