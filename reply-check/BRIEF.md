# Brief for the claim-check sub-agents

You are checking one batch of claims in Steven Pinker's Quillette essay "Will We All Go Together When We Go?"
(2026-11-23), his reply to Scott Alexander's "An Open Letter To Steven Pinker On AI" (ACX, 2026-10-06). Today is
2026-11-24. Many events in 2026 are after your training data: trust pages you fetch today over your memory, and never
fill a gap from memory.

Working folder: `~/Research/topics/2026-10-06-scott-pinker-ai-letter/` (call it TOPIC). Read first:
- `TOPIC/reply-check/claims.md`: your batch (by letter) and what to check for each claim.
- `TOPIC/pinker-quillette-reply-2026-11-23.md`: Pinker's essay (line numbers in claims.md refer to this file).
- As needed: `TOPIC/post.md` (Scott's letter as first published), `TOPIC/post-edits-2026-10-07.md` (his later edits),
  `TOPIC/pinker-quillette-letter.md` (Pinker's first letter), `TOPIC/report.md` (the earlier fact-check; reuse its
  verified findings and links rather than redoing them), `TOPIC/notes.md` (scry ids and SQL), `TOPIC/media/`, `TOPIC/docs/`,
  `TOPIC/web/`, `TOPIC/gaps/` (saved sources).

## Standard

Be adversarial in both directions. For every claim, look for the evidence that would make Pinker wrong *and* the
evidence that would make him right, and report both. Quote context when a quotation is cut, conditional, or reversed by
the next sentence. A quote can be verbatim and still misleading; say so.

Verdicts:
- ✅ accurate
- 🟡 accurate but misleading, truncated, out of context, or overstated (say which)
- ❌ wrong
- ❔ not verifiable (say what you tried)

Provenance tags on each piece of evidence:
- `[V]`: verbatim, from text you fetched and read yourself (raw HTML/PDF text, API JSON, scry rows).
- `[2nd]`: from a search snippet, a WebFetch summary (it is a summariser: never treat its quotes as verbatim), or a
  secondary report.
- `[MEASURED, scry]` for tweet text and counts pulled from scry; `[MEASURED, my pull]` for numbers you computed from
  an API or table.

## How to fetch and link

- Get verbatim text with `curl -sL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"`
  into a scratch dir (`/tmp/rc-<batch>/`), then extract text (python html parsing, `pandoc -t plain`, or
  `pdftotext -layout`). WebFetch and WebSearch are fine for discovery only.
- Make every link to a passage with the verified-link tool, run from TOPIC:
  `~/Research/.bin/tools link '<url>' '<exact passage as it appears on the page>'`
  It fetches the page, checks the passage, and prints a text-fragment URL (falling back to an archive copy if the
  original is blocked). Use the URL it prints, unchanged. If it fails, try a shorter distinctive passage; if the page is
  blocked everywhere, link the plain URL and tag the quote `[2nd]` unless you read it elsewhere verbatim.
- PDFs: link `<pdf-url>#page=N` (find N with `pdftotext -layout` and `awk -v RS='\f' '/pattern/{print NR}'`; check
  against printed page numbers). Where the exact wording matters, also make a local HTML copy:
  `cd TOPIC && ~/Research/.bin/tools pdf2html --file <pdf>` → `docs/<stem>.html`, then
  `~/Research/.bin/tools link docs/<stem>.html '<passage>'`. Put the PDF itself in TOPIC (PDFs are gitignored).
- Paywalled pages (NYT, WSJ, The Australian, Lawfare sometimes): try archive.today (`https://archive.ph/newest/<url>`)
  and Wayback (`https://web.archive.org/web/2026/<url>`); `~/Research/.bin/tools archive <url>` finds copies.
- Tweets: link `https://x.com/<handle>/status/<id>`. Get the text from scry, not from X. scry is an MCP server: load
  its tools with ToolSearch (`+scry`), call `whoami` first with the roster fingerprint its tool description gives, and
  read `guide` if unsure. Useful: `twitter.tweets_latest` (by tweet_id), `twitter.tweets_by_author` +
  `twitter.tweets` (by author_id and date), `twitter.author_handles`. Pinker author_id 107225267, Scott
  1526643050, Lehmann 1398479138 (more in TOPIC/notes.md). Put each SQL you run in your batch file's notes section.
- Google Books: `https://books.google.com/books?id=<id>&q=%22<phrase>%22` plus the page number, tagged `[2nd]` unless
  you saw the snippet text yourself.
- Save the pages you rely on (HTML or extracted text) under `TOPIC/reply-check/sources/<batch>-<short-name>.<ext>`,
  except PDFs and anything over ~3 MB. Never save a whole copyrighted book.

## Output

Write `TOPIC/reply-check/batch-<LETTER>.md`, one section per claim id, in this shape:

```markdown
### <ID>. <short title>
- **Pinker:** "<his exact words>" (L<n>)
- **Verdict:** <emoji> <one-line reason>
- **Evidence:**
  - "<verbatim quote>" ([<source, date, page>](<link from the link tool>)) [V]
  - …evidence for the other side…
- **Context / what's left out:** <bullets, only if there is something>
- **How checked:** <one line: fetched X, archive used, scry query n>
```

End the file with `## Notes` (SQL, dead ends, sources you could not reach, anything surprising that is outside your
claims but matters to the dispute). Keep prose plain and short; the evidence carries it.

Then reply to me with: the file path, a table of claim id → verdict, and the 3–5 findings you think matter most.
Do not edit any file outside `TOPIC/reply-check/` and `TOPIC/docs/` (and TOPIC for PDFs). Do not commit or push.
Do not post anything anywhere.
