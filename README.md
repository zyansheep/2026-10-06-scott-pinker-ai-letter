# Scott Alexander vs. Steven Pinker on AI: a fact check

In autumn 2026 Steven Pinker and Scott Alexander exchanged open letters about AI risk. This repo checks their claims one by one against the sources they cite and against the record, and then weighs the arguments.

| Date | Letter | Checked in |
|---|---|---|
| 2026-09-26 | Pinker, ["An Open Letter to Scott Alexander"](https://quillette.com/2026/09/26/an-open-letter-to-scott-alexander-steven-pinker-ai-alignment-safety/) (Quillette) | [report.md §2b](report.md#2b-pinkers-letter-and-tweets-checked-the-same-way) |
| 2026-10-06 | Scott, ["An Open Letter To Steven Pinker On AI"](https://www.astralcodexten.com/p/an-open-letter-to-steven-pinker-on) (Astral Codex Ten) | [report.md](report.md) |
| 2026-11-23 | Pinker, ["Will We All Go Together When We Go?"](https://quillette.com/2026/11/23/will-we-all-go-together-when-we-go-ai-alignment-scott-alexander-doomerism/) (Quillette) | [reply-report.md](reply-report.md) |

## Start here

- **[report.md](report.md)** checks Scott's letter. In short: the quotes Scott uses are mostly real, but his selection is prosecutorial and several items are wrong. Pinker's first letter has errors of its own. On the narrow points Scott wins most, but neither side engages the other's strongest case.
- **[reply-report.md](reply-report.md)** checks Pinker's reply (113 claims). In short: nearly every quotation is verbatim, but the framing around them often isn't. There are a handful of clear errors, Scott's own words are sometimes turned against him, and the first letter's mistakes are fixed without comment. Its strongest point is that a p(doom) number with no date can't be compared or scored. Its weakest is the six-step calculation that gets doom under 2%.

Each report opens with a bottom line, then has verdict tables (✅ checks out, 🟡 partly right or trimmed, ❌ wrong, ❔ can't be checked), an evaluation of the arguments, caveats, open gaps and a revision log.

## Who wrote this

The reports were researched and written by Claude, an AI model made by Anthropic, at the repo owner's request. Anthropic is a party to this dispute: Scott defends its strategy, Pinker criticises its work on model welfare, and the argument is partly about systems like Claude. Each report opens with that disclosure. The factual verdicts are meant to stand on the linked sources; weigh the evaluation sections with the conflict in mind.

## How the links work

- A quote from a web page links to the original with a text fragment (`#:~:text=`), so the browser scrolls to and highlights the passage. Each fragment was checked against the fetched page.
- Paywalled originals link to archived copies. PDFs link with `#page=N`, and some also have a local HTML copy in `docs/`.
- Tweets link to their status page. Tweet text comes from the [scry](https://scry.io) Twitter archive rather than from scraping X.

## What's in the repo

| Path | What it is |
|---|---|
| `report.md`, `reply-report.md` | The two reports |
| `post.md`, `post-edits-2026-10-07.md` | Scott's letter as published, and the edits he made in the following days |
| `pinker-quillette-letter.md`, `pinker-quillette-reply-2026-11-23.md` | Pinker's two letters |
| `notes.md` | Working notes for the first report, including the scry SQL queries |
| `sources.json`, `sources.md` | Source list with metadata |
| `reply-check/` | Working files for the reply report: the claim list, the brief, notes for each checking batch (A–J), saved sources, and `build-links.py` |
| `web/`, `media/` | Saved copies of the letters and of articles the letters cite |
| `docs/` | HTML copies of cited papers and reports, for text-fragment links |
| `gaps/` | Material gathered while filling gaps in the first report |
| `img/` | Images from Scott's letter |

Some files stay out of the repo on purpose: PDFs and plain-text extractions (`.gitignore`), and a full copy of Pinker's book *Enlightenment Now*, which the first report quotes. Those quotes also link to Google Books.

## Rebuilding the reply report

`reply-report.md` is generated from `reply-check/reply-report.src.md`, where quotes from the letters are written as placeholders (`](PQ:passage)` for Pinker's reply, `](SQ:passage)` for Scott's letter, `](P1:passage)` for Pinker's first letter):

```sh
python reply-check/build-links.py reply-check/reply-report.src.md reply-report.md
```

The script finds each passage in the saved pages and turns it into a verified text-fragment link. It needs the owner's research tooling (`~/Research/.bin`), so it won't run on a fresh clone as it stands.
