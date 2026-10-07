# Working notes: Scott Alexander vs. Steven Pinker on AI (Sept–Oct 2026)

## Primary docs on disk
- `post.md`: Scott Alexander, "An Open Letter To Steven Pinker On AI", ACX, published 2026-10-06T21:23Z (Substack API `wordcount` 10,538). Pulled from `https://www.astralcodexten.com/api/v1/posts/an-open-letter-to-steven-pinker-on`, converted with pandoc. Images in `img/`.
- `pinker-quillette-letter.md`: Pinker, "An Open Letter to Scott Alexander", Quillette, 2026-09-26T20:09Z.
- `media/lehmann-2026-09-18-australian-via-x.md`: Lehmann's Australian piece, full text from her X long-post.
- `scry-pinker-ai-tweets-pre2026-09.tsv`: 294 Pinker tweets 2014→2026-08 matching AI/doom tokens (scry).

## scry account
- `whoami` OK (roster 938f84c9 synced). All queries were billed `free_slack` (spend 0).
- Handle → author_id via `twitter.author_handles`: sapinker=107225267, slatestarcodex=1526643050, clairlemon=1398479138, garymarcus=232294292, marcus_j_w=1853742243682582528.

## Queries (verbatim SQL)

1. Hydrate every tweet ID the post cites:
```sql
SELECT toString(tweet_id) AS id, author_handle, original_timestamp, text, toString(quoted_tweet_id) AS quoted, toString(in_reply_to_tweet_id) AS reply_to, like_count, retweet_count, view_count, text_is_complete FROM twitter.tweets_latest WHERE tweet_id IN (2101700244895572065, 2101073872267493554, 2044510743014375792, 2104218250724655495, 2104222160042553696, 2101477407329018067, 2103979089778675736, 2106203042140102868, 1491554478243258368) LIMIT 20
```
→ all 9 found. Engagement counts are as of scry's observation (often minutes after posting), so they understate final counts. E.g. the cult tweet shows 5 likes in scry vs 85.1K views in Scott's screenshot.

2. Pinker tweets per year (`twitter.tweets_by_author`, uniqExact): 2018=573, 2019=804, 2020=1182, 2021=1265, 2022=1019, 2023=448, 2024=552, 2025=1633, 2026=1924 (to Oct 6).

3. Pinker AI tweets since 2026-09-01:
```sql
SELECT toString(tweet_id) AS id, min(original_timestamp) AS ts, argMax(text, version) AS t, toString(argMax(quoted_tweet_id, version)) AS q, max(like_count) AS likes FROM twitter.tweets WHERE author_id = 107225267 AND tweet_id IN (SELECT tweet_id FROM twitter.tweets_by_author WHERE author_id = 107225267 AND bucket_date >= '2026-09-01') AND hasAnyTokens(search_text_lc, ['ai','doomer','doomers','doomerism','superintelligence','agi','yudkowsky','rationalist','rationalists','alexander','slatestarcodex','debate','duel','apocalypse','extinction','llm','llms','sentience','welfare','anthropic','openai','omohundro','instrumental','catechism','cult','alignment','newport','sibarium','suleyman','lehmann','clairlemon','p(doom)','existential']) AND NOT startsWith(text, 'RT @') GROUP BY tweet_id ORDER BY tweet_id ASC LIMIT 200
```
→ 31 rows. Key ones are listed in "Key Pinker tweets" below.

4. Pinker's non-self retweets since 2026-08-01 (`startsWith(text,'RT @') AND NOT startsWith(text,'RT @sapinker')`): 40 rows. Lehmann-related: only `RT @clairlemon: An Open Letter to Scott Alexander From @sapinker` (2026-09-27, 2026-09-28). **No RT of Lehmann's EA "selfish males / gullible females", Hinton "stop platforming", or "AI conscious = 2-year-old" tweets** was observed. Others: RT @mboudry (2026-09-27, "Prophecies of doom are dangerous..."), RT @michaelshermer (2026-09-10 "187,000 people escaped extreme poverty yesterday? Boring! Today's news is that AI may kill us all..."; 2026-09-27 "If you are following the AI doomsday story..."), RT @haider1 (2026-09-09, the superintelligence clip).
   Caveat: retweet capture in the archive may be incomplete.

5. Pinker AI backlog before 2026-09 (tokens incl. doomer, superintelligence, agi, yudkowsky, rationalist, slatestarcodex, extinction, omniscient, alignment, paperclip, foom, gpt, chatgpt, llm, deep, scaling, marcus, aaronson): 294 rows → `scry-pinker-ai-tweets-pre2026-09.tsv`.

6. 2019 "deep learning peaked" tweet:
```sql
... AND (hasAnyTokens(search_text_lc, ['peaked','shallow','futurism']) OR lower(text) LIKE '%deep learning%')
```
→ 1139625721901572097, 2019-06-14 20:08:39 UTC: "“Deep learning” in AI (which in fact is quite shallow) has probably peaked." 343 likes, 94 RTs (matches screenshot).

7. Scott's tweets since 2026-09-10 (51 rows), including the challenge (2101503925455343802, 2026-09-20 02:49 UTC).

8. Pinker vocabulary check: tweets containing {paranoid, paranoia, laughed, laugh, alpha, male, polyamory, lifestyles, weird, eccentric, cult, eschatology, prophecy, catastrophists, fear-sowers, hysteria, panic, fatalism, moronic, stupid} AND an AI/doom token, over the whole archive → 23 rows. **No "paranoid", "laughed", "male", "lifestyles" in Pinker's own AI tweets.** Hits: "AI-fear-sowers" (2018), "AI catastrophists" (2018), "panic about AI" (2018), "eccentric Berkeley subculture ... eschatology is a sacred belief" (2026-09-05), cult tweet (2026-09-28), end-times prophecies (2026-09-29). Pinker self-retweeted the "preposterous" tweet 4× (09-20, 09-24, 09-27, 09-28) and the cult tweet 5× (09-28 → 10-03).

9. "unconventional lifestyles" phrase, all X since 2026-08-15 → Lehmann long-post 2101052017347281300 (2026-09-18 20:53 UTC): "This conviction is shared by many people who live together in the San Francisco Bay Area practising highly unconventional lifestyles. It is not at all surprising that a community in San Francisco would share kooky or even apocalyptic beliefs". Pinker tweeted the piece 1h27m later.

10. Pinker mention counts over the whole archive (9,548 tweets excl. self-RTs; uniqExactIf): Lehmann/Quillette 95, Gary Marcus 75, Scott Alexander/slatestarcodex 63, Boudry 39, Melanie Mitchell 3.

11. Reactions: X tweets with "pinker" + (slatestarcodex | scott alexander | debate | duel) since 2026-09-18, ranked by likes; tweets since 2026-10-06 mentioning either. HN stories with "pinker" since 2026-09-15: 5 stories, max 14 points (ACX post), 0–1 comments each. Manifold: one market, "Will Steven Pinker and Scott Alexander have a debate on AI safety in 2026?" (created 2026-09-20, 0 bettors at the observed state). LessWrong/EA Forum: Zvi AI #187 and #188; Algon comment citing Cody Fenwick on RAND; "RAND's extinction report estimates one side of an inequality" (Marko Katavic, 2026-09-29).

## Key Pinker tweets (verbatim, scry)
- 2018-05-21: "Elon Musk thinks flying cars will chop our heads off. (Ever notice how AI-fear-sowers see catastrophe everywhere? Many belong to "existential threat" projects that think up as many as they can)."
- 2018-06-25: "...People flooded with worst-case scenarios may develop "apocalypse fatigue" (AI catastrophists take note.)"
- 2019-06-14: "“Deep learning” in AI (which in fact is quite shallow) has probably peaked."
- 2019-12-06 (to @juliagalef): "Yes, Russell has made it increasingly clear, particularly in Human Compatible, that he thinks AI existential risk is real. In the next printing of Enlightenment Now, I'll take his name off the list of AI existential-risk-skeptics in Note 20 on. p. 477."
- 2021-02-14: "A typical essay by Scott Alexander is deeper, better reasoned, better referenced, more original, and wittier than 99% of the opinion pieces in MSM." / "National treasure Scott Alexander" / 2021-02-16: "Among the virtues of Scott Alexander @slatestarcodex, & the "rationality community" in general, is acknowledging his fallibility and uncertainty".
- 2022-06-02: "Scott Alexander @slatestarcodex unmasks the same problem. Human combinatorial cognition opens an exponential space ... Bigger & bigger data can approximate a lot of it, but the long tail of novelties always shows its limits."
- 2023-02-05: "Large Language Models have no notion of truth. ... Also, ironically, bad at math" / "Suggests that "artificial general intelligence" and "superintelligence" are incoherent concepts. Intelligence isn't one thing."
- 2023-04-19: "AI safety is important, but fantasies of human extinction (including calls to bomb AI labs) are a distraction."
- 2023-07-12 (quoting Tetlock on XPT): "More accurate forecasters are less worried about AI existential risk."
- 2023-07-21: "For me, this is a familiar demonstration of the Availability Bias..." / "...the muddle of AI-X-risk discussion w/in that closed community: "intelligence" as a magic power rather than a mechanism; "AGI" equated w omniscience & omnipotence..."
- 2024-08-23 (quoting @DrTechlash, "$1.6 BILLION dollars from Effective Altruism billionaires"): "I agree that AI doomerism has attracted outsize attention (compared to real dangers) because of massive funding by not-so-effective tech philanthropy."
- 2025-03-14: "As a cognitive scientist I’ve always been skeptical of the theory that “scale is all you need”..."
- 2026-04-15: "Important not to confuse the notion of "general intelligence" from psychometrics ... with the (somewhat mystical) notion bandied about in AI of omniscience and omnipotence." (reply under his own "Artificial Intelligence and Artificial Stupidity" thread)
- 2026-07-26: "At most of historical interest: I made some of these points in a debate with ... Scott Aaronson ... (2022, before the release of ChatGPT). **I underestimated what AI was about to be capable of**, but expressed some of the ideas about the nature of intelligence..."
- 2026-09-05: "Why are the leaders of AI companies saying "Our products are going to extinguish humanity. Invest in us!" They come from an eccentric Berkeley subculture in which this eschatology is a sacred belief. Good analysis in a NYT op-ed by Cal Newport." + "As Newport points out, harping on doom for the species changes the subject from immediate and obvious threats from AI, such as enabling bioterrorism, undermining truth-seeking institutions, and breaching cybersecurity."
- 2026-09-18: "Is AI really going to kill us all? The scenarios are preposterous, and the presumption of inevitability encourages fatalism, panic, and distraction from the more mundane and realistic safety challenges. By @clairlemon"
- 2026-09-27: superintelligence clip ("The power will increase ... It'll never be omniscient. It'll never be omnipotent. That's out of comic books out of religion ... they'll get more powerful.")
- 2026-09-27: Into the Machine clip ("...or whether, having been trained on all this human input, they're just doing their best to emulate basically what a human would do...")
- 2026-09-27: "I've been suspicious of the philosophers hired by Anthropic who specialize in AI ethics ... | ‘Suicidal Compassion’: Meet the Anthropic Officials Who Think AI Might Be Justified in Going Rogue..."
- 2026-09-28: Suleyman thread (3 tweets) + cult/catechism tweet + WSJ subculture link.
- 2026-09-29: "Do AIs inherently protect their own interests ... @mboudry shows how this "instrumental convergence" doomer dogma is dubious anthropomorphism." / end-times-prophecies tweet / "Thanks, @mboudry, for explaining why I don't feel compelled to use the proprietary doomer lexicon (orthogonality, convergence, etc.), since that would concede points that in fact I am challengenging."

## Scott's own tweets (scry), relevant
- 2026-09-20 02:49 UTC, reply to Pinker's 09-18 tweet: "I think you've done enough calling us paranoid and preposterous. ... I'm happy to put my $5000 against your $1000 (ie 5:1 odds in your favor) that I'll win by some standard of audience opinion change."
- 2026-09-20 15:49: the accusation tweet (male / "unconventional lifestyles" / paranoid / laughed out of the room). It concedes "his exact wording was a bit slippery" about arithmetic.
- 2026-09-13: "...(it went from 1+1 to Navier-Stokes over the past five years ...)" and "...(**assuming the Navier-Stokes result holds up**)". The post states it without that hedge.
- 2026-09-21: "I do pretty regularly encounter people who at least claim that it's some tangential lifestyle thing - whether it's polyamory, or the Harry Potter fanfic ... which has made them hate us".
- 2026-10-01: "Oh, you're worried about a Jewish guy's apocalyptic cult? You're scandalized that they consort with prostitutes? ... Should we invite Pontius Pilate?" (1,981 likes, 227K views as observed)
- 2026-10-07 00:37: reply to @MelMitchell1: "I didn't mean for that to be an insult, but feel free to link me to your relevant work and I will read it as penance."

## Third-party reactions (scry)
- Mitchell 2026-10-07: "I got insulted online by Scott Alexander! Fun times. I guess he hasn't read any of my work since the 1980s."
- Lehmann 2026-10-06: "...He makes some good point as you'd expect, especially on the capability of the models. I was less convinced when he tried to explain why LLMs would become power seeking. He also calls me a 'culture warrior' & 'lowest quality voice'"
- Gary Marcus 2026-09-20: "...I strongly favor alignment research, and definitely would entertain some sort of pause; i fear catastrophe. literal extinction, even if you assume AGI, is a real stretch. if Scott is serious about the issues, he should debate me, with or without Pinker."
- Zvi (AI #187, 2026-09-24): "Whenever they pull out the Fallacy of Relative Privation you know they do not have a good argument." / "I think leading with the wager is a misstep." (AI #188, 2026-10-01): "Steven Pinker declines to debate Scott Alexander, which is fair, but also his actual arguments continue to be extremely terrible."
- tracewoodgrains 2026-09-27: "I think Pinker acquitted himself well in this article".
- Jeff Sebo 2026-09-28 (277 likes): Pinker's model-welfare dismissal is "shockingly incurious, uninformed, and ungenerous".
- Maarten Boudry 2026-09-27: "Both are brilliant, but imho Pinker is right here."
- Richard Hanania 2026-10-07: "...the story of global warming cuts the other way..."

## Melanie Mitchell, recent LLM work (OpenAlex author A5086956524, works since 2022-06; 27 total)
"The debate over understanding in AI’s large language models" (PNAS 2023, 10.1073/pnas.2215907120); "Comparing Humans, GPT-4, and GPT-4V On Abstraction and Reasoning Tasks" (2023, arXiv 2311.09247); "The ConceptARC Benchmark" (2023); "Evaluating the Robustness of Analogical Reasoning in Large Language Models" (2024, arXiv 2411.14215); "Can Large Language Models generalize analogy solving like children can?" (2024); "Large language models and emergence: a complex systems perspective" (Phil Trans A 2026); "Do AI Models Perform Human-like Abstract Reasoning Across Modalities?" (2025, arXiv 2510.02125).

## Forecasting / instrumental-convergence record (scry, query 12)
Tokens: omohundro, instrumental, orthogonality, convergence, bostrom, russell, hinton, bengio, sutskever, tegmark, miri, lesswrong, tetlock, superforecasting, forecasters → 28 rows.
- 2020-03-10: "Tetlock's rational forecasting project is a big theme of Enlightenment Now & my Rationality course."
- 2022-08-25: "Given our ignorance of what will happen even 5 years out (horizon of superforecasters), it's unclear what long-termism adds..." (Pinker DID offer a horizon argument against long-range probabilities, in a longtermism context.)
- 2023-07-21 thread: "Superforecasters (well-incentivized experts with no ulterior motives plus masters of statistics/rationality/predictions) predict 3/10 of 1% chance that AI will kill us all by 2100. AI experts predict 3%. Some prominent "Rationality"/EA writers predict 30% or higher..." → "For me, this is a familiar demonstration of the Availability Bias..." → "...the muddle of AI-X-risk discussion w/in that closed community..." → link to Tetlock's XPT report.
  ⇒ In 2023 Pinker himself treated subjective AI-x-risk probabilities as meaningful (using XPT superforecaster numbers), and he knew the doomer numbers were "30% or higher", not 100%.
- No pre-2026-09 Pinker tweet mentions Omohundro, "instrumental convergence" or "orthogonality". The first are 2026-09-28/29 (cult tweet; Boudry tweets). Earlier, 2026-05-06 (Boudry): "Neither malevolence nor lethal means to an end are natural products of intelligence, though they could arise if anyone was so stupid and reckless as to both empower AIs and let them evolve in the wild." 2018-02-15: "Why AI won't kill us (neither as targets nor as collateral damage--the so called value alignment problem). Excerpt from the "Existential Risks" chapter of Enlightenment Now."
- 2017-09-16: "Geoff Hinton may be the most brilliant living cognitive scientist". 2020-06-15: long conversation with Stuart Russell (FLI podcast).

## Pinker's letter "experts" list vs Scott's description
Letter: "Blaise Agüera y Arcas, Jerry Kaplan, Gary Marcus, Melanie Mitchell, Arvind Narayanan and Sayash Kapoor, and Andrew Ng". Scott: "Once again, it's Gary Marcus, Melanie Mitchell, and other people with obsolete AI paradigms from the 2000s". Andrew Ng (Google Brain co-founder) and Agüera y Arcas (Google Research VP/Fellow) are deep-learning-era insiders, so Scott's description is inaccurate for at least these two. [MY SYNTHESIS]

## Lehmann "pivoted to AI two months ago" (scry, query 13)
```sql
SELECT toStartOfMonth(bucket_date) AS m, uniqExactIf(tweet_id, hasAnyTokens(search_text_lc, ['ai','agi','llm','llms','chatgpt','openai','anthropic','superintelligence','doomer','doomers','yudkowsky','rationalists','claude'])) AS ai_tweets, uniqExact(tweet_id) AS all_tweets FROM twitter.tweets WHERE author_id = 1398479138 AND tweet_id IN (SELECT tweet_id FROM twitter.tweets_by_author WHERE author_id = 1398479138 AND bucket_date >= '2025-01-01') AND NOT startsWith(text, 'RT @') GROUP BY m ORDER BY m LIMIT 30
```
AI-token tweets per month (of all non-RT tweets): 2025-01..2026-08 range 0–6/month (e.g. 2026-07: 2/205, 2026-08: 2/92). 2026-09: **45/240**. 2026-10 (6 days): 9/54.
⇒ A sharp pivot, but it started in September 2026 (about 1 month before the post), not 2 months. Keyword proxy only.

## Pinker on mundane AI harms / regulation, 2025-01 → now (scry, query 14)
Tokens: (moratorium|preemption|bores|sb1047|regulation|regulate|deepfake(s)|misinformation|hallucinate|hallucinations|scams|scammers|cybersecurity|bioterrorism) AND (ai|llm|llms|chatgpt|chatbots|bots) → 8 rows.
- **No tweet on the 2025 moratorium/preemption fight, Bores, or SB 1047.**
- Mundane-harm mentions: AI publishing scams (2026-05-02, 2026-09-27); why LLMs hallucinate (2026-03-07); the Newport "immediate and obvious threats" thread (2026-09-05); ChatGPT libel anecdote (2026-09-04, from query 3).
- 2026-06-13, quoting Noah Smith approvingly: "To embrace the poisonous nonsense of degrowth now — to shut down nuclear power plants, to regulate the AI industry out of existence, ..."
- 2026-03-08: LLMs "generally push toward rational and objective conclusions, and even change minds in positive directions".
⇒ Scott's "you didn't join the fight against preemption" is consistent with the archive (absence, within archive coverage). "Never written any particular warning about mundane harms" is roughly right as to advocacy. Pinker mentions specific harms (scams, libel, hallucination) as asides, not campaigns. His letter does endorse oversight, liability and kill switches.

## Sub-agent results (2026-10-06): see report.md. Anna's Archive was unreachable (book_search returned nothing; annas-archive.li is a parked domain), so no downloads were spent and no ledger line was written.

## Link rebuild (2026-10-07): text fragments, no end list
The user asked for fragment links to original pages, archive copies for blocked pages, local pdf2html for PDFs, and no source list at the end. AGENTS.md was updated to match.
- **Method.** report.md was rewritten with placeholders and resolved by `/tmp/pinker-scripts/fraglinks.py` (ephemeral):
  - Web: fetch the page, extract the visible text with block boundaries, find the quote (normalizing curly quotes, dashes and whitespace), then build `#:~:text=start,end` from the page's own characters, encoding `-`, `,` and `&`. It checks that the start term's first occurrence is the intended passage.
  - PDFs: the original URL with `#page=N`, plus `docs/*.html` fragments from `.bin/tools fragment`.
- **Result.** 103 web fragments, 5 local fragments, 6 PDF page links and 9 Google Books search links. An independent re-check (`verify.py`) decoded all 108 fragments and found each start and end term in the page text (0 failures; 203 links total, none with raw spaces or unbalanced parentheses). Short generic terms ("writing in", "elifland") were checked in context by hand.
- **Blocked originals:**
  - Wayback Save Page Now (POST form) "captured" the two NYT op-eds with http_status 403 (the block page), and The Australian refused the crawler ("The target server blocks access").
  - archive.today already had full-text snapshots, which I verified by fetching them and finding the quotes:
    - Newport `archive.is/20260908091028/…`
    - Goldberg `archive.is/20260928173816/…`
    - Lehmann (The Australian) `archive.is/20260927140739/…`
    - WSJ `archive.is/20261004133739/…`
  - WSJ links use the Wayback copy `web.archive.org/web/20261003170018/…`, which contains the text.
- **Local HTML** (pdf2htmlEX via podman, run by hand because these are open-access, not Anna's): `docs/RAND_RRA3034-1.html`, `docs/Long-range subjective probability - Tetlock et al 2023 (accepted manuscript).html`, `docs/ESPAI2024 - Grace et al 2026.html`. The PDFs are in `media/` and gitignored.
- **Fixes along the way.** The OpenAI Navier-Stokes URL is `/index/navier-stokes-solution/` (the old one 404s). The Wikipedia P(doom) link had an unescaped `)`.

## Wayback archiving of cited pages (2026-10-07)
Asked to submit missing pages. I looked up each open cited URL in the CDX API (many lookups timed out, so those were submitted anyway; a re-capture is harmless) and submitted via the Save Page Now POST form.
- **Already archived (status 200):** christiano (20250728005130), edge2014 (20260915205659), edge2015 (20260520163821), edgeblurb (20200123003743), freebeacon (20260930190926), gradient (20260909231105), leaderboard (20260914211041), mybet (20260925020933), navier (20261005200455), popsci (20260412051317), randland (20261004093835), sciam (20260929033120), suleyman (20261004125321).
- **Newly captured, confirmed `success 200`:** quillette (20261007024521), gazette (20261007024619), aaronson (20261007024642), boudry (20261007024827), chalmers (20261007024857), clay (20261007024901), enzyme (20261007024915), espai_pdf (20261007024934), evitable (20261007024952), hogarth (20261007025008), pdoom (20261007025114).
- **Submitted, unconfirmed:** scott, manifold, metr, rand_pdf, restart, ruanhtml, tetlockdoi, tetlock_pdf, yudkowsky, zvi187, zvi188. The status endpoint stopped responding, so these are queued at archive.org but not verified.
- **No job ID returned:** arxiv.org/abs/2609.16247 (twice). The ai-torture-chamber repo got a job on its second try (unconfirmed).
- **Blocked:** NYT ×2 were captured as 403 block pages, and The Australian refused the crawler. The report links archive.today copies instead (see above).

## Red-team review queries (2026-10-07, scry, free_slack)
Report not edited; these support a reviewer pass.
1. Hydrate Pinker/Sebo/Boudry/trace/Lehmann tweets cited in the report:
```sql
SELECT toString(tweet_id) AS id, original_timestamp, text, like_count, view_count, text_is_complete FROM twitter.tweets_latest WHERE tweet_id IN (2104555373101256891, 2104555379933798816, 2104561752847306801, 2096236079477096630, 2096236083713327125, 2104221154726572385, 2104222160042553696, 2104628024628928988, 2081377486009463170, 2107605101041127659, 2104031443689361457, 2104220627594772969) LIMIT 30
```
→ Suleyman tweet defines "model welfare" as "training AI to reason and act as if it were an entity with sentience … alarmingly implied by Anthropic's "Constitution""; the 09-27 clip ends "unless they're programmed to emulate a human down to the last twitch, they would actually have no incentive to continue their existence"; Boudry's "Pinker is right here" quotes the nuclear-1960s passage.
2. Reactions since 2026-10-06 mentioning Pinker, by likes:
```sql
SELECT toString(tweet_id) AS id, argMax(author_handle, (length(author_handle) > 0, version)) AS h, min(original_timestamp) AS ts, argMax(text, version) AS t, max(like_count) AS likes, max(view_count) AS views FROM twitter.tweets WHERE bucket_date >= '2026-10-06' AND hasToken(search_text_lc, 'pinker') AND NOT startsWith(text, 'RT @') GROUP BY tweet_id ORDER BY likes DESC LIMIT 60
```
3. Named commentators (Haider, Hanania, trace, Zvi, Bensinger, ciphergoth) since 2026-10-06:
```sql
SELECT toString(tweet_id) AS id, argMax(author_handle, (length(author_handle) > 0, version)) AS h, min(original_timestamp) AS ts, argMax(text, version) AS t, max(like_count) AS likes, max(view_count) AS views, max(reply_count) AS replies FROM twitter.tweets WHERE bucket_date >= '2026-10-06' AND (lower(author_handle) IN ('sarahthehaider','richardhanania','tracewoodgrains','thezvi','robbensinger','ciphergoth')) AND NOT startsWith(text, 'RT @') AND hasAnyTokens(search_text_lc, ['pinker','scott','alexander','duel','dishonorable','debate']) GROUP BY tweet_id ORDER BY ts ASC LIMIT 40
```
4. Sarah Haider timeline since 2026-10-06 (found 2107613722789155206, quoting the "watch you squirm" paragraph):
```sql
SELECT toString(tweet_id) AS id, min(original_timestamp) AS ts, argMax(text, version) AS t, max(like_count) AS likes, max(view_count) AS views, max(reply_count) AS replies, max(quote_count) AS quotes FROM twitter.tweets WHERE bucket_date >= '2026-10-06' AND lower(author_handle) = 'sarahthehaider' AND NOT startsWith(text, 'RT @') GROUP BY tweet_id ORDER BY ts ASC LIMIT 30
```
Also: Google Books SearchWithinVolume2 on hf9MDwAAQBAJ (Enlightenment Now): "superforecasters" → pp. 368–71 (ch. 21 "Reason", pp. 351–84); "missile gap" → p. 291; "Rabinowitch" → p. 311.
