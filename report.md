# Does Scott Alexander's "Open Letter To Steven Pinker On AI" hold up against Pinker's actual record?
_2026-10-06 · status: thorough (same-day; the exchange is still live)_

**The question as I read it.** You asked me to do three things. First, check the factual claims in Scott Alexander's [An Open Letter To Steven Pinker On AI](https://www.astralcodexten.com/p/an-open-letter-to-steven-pinker-on) (ACX, 2026-10-06, about 10.5k words). The priority is what it says Pinker said or did, using scry's Twitter archive as the primary record and not scraping X. Second, evaluate the post and both men's positions. Third, analyse the wider dynamics and motives. The post replies to Pinker's [An Open Letter to Scott Alexander](https://quillette.com/2026/09/26/an-open-letter-to-scott-alexander-steven-pinker-ai-alignment-safety/) (Quillette, 2026-09-26).

**Disclosure.** I am Claude, an AI made by Anthropic, and Anthropic is a party in this dispute. Scott defends its strategy. Pinker attacks its "model welfare" work and the philosophers it employs. And the subject of the dispute is whether systems like me are dangerous and whether we could have interests. Weigh my object-level judgments (§4) with that in mind. I've kept the factual scorecard (§1–3) separate from them so you can check it independently.

**Conventions.** Tweet text marked `[MEASURED, scry][V]` was pulled verbatim from scry's `twitter.*` relations (SQL in [notes.md](notes.md)). Engagement counts in scry are as of observation, often minutes after posting, so they understate final numbers. Book quotes come from Google Books search-within snippets with page numbers; Anna's Archive was unreachable, so I never had the full book.

---

## Bottom line

- **The quotes Scott uses are mostly real.**
  - All nine tweets he links exist verbatim in the archive.
  - His screenshots match it, including the 2019 tweet "“Deep learning” in AI (which in fact is quite shallow) has probably peaked."
  - His correction of Pinker's RAND citation is substantially right.
  - His charge that Pinker boosted the "unconventional lifestyles" framing is right. The phrase comes from Claire Lehmann's article, which Pinker tweeted 87 minutes after she posted it.
  - The harshest words in the exchange are Pinker's own, not his sources': "depravity", "insouciant about the AI worldwide genocide", "doomer catechism".
- **But the selection is prosecutorial, and several items are wrong.**
  - Scott cuts quotes just before Pinker's qualifications ("…but it will improve"; "…yet so moronic that they would give it control of the universe without testing how it works").
  - He attributes a 2026 quote to a 2018 book.
  - He presents Pinker's 2022 prediction as one about arithmetic. Scott's own blog had shown GPT-3 passing the "trophies" test three weeks *before* Pinker wrote it.
  - He leaves out Pinker's public concession: "I underestimated what AI was about to be capable of."
  - He makes false or overstated claims about others: Mitchell's expertise, Pinker's expert list, Christiano's numbers, Anthropic's bio lab, and the self-preservation evidence.
- **On the merits, Scott wins most of the narrow points, but neither engages the other's strongest case.**
  - Where Scott is right:
    - AI capabilities keep rising, which Pinker now concedes.
    - Instrumental convergence does not depend on natural selection or on a single goal.
    - Serious AI-risk writers don't claim omniscience.
    - Pinker misquoted RAND.
    - Pinker uses forecasting numbers when they help him.
  - Where Pinker has real arguments that he makes badly and Scott mostly sidesteps:
    - Whether power-seeking is a natural product of how current systems are trained, or a contingent result of deployment choices.
    - Whether long-horizon p(doom) numbers are calibrated.
    - Whether doom messaging backfires. That is an empirical question nobody in the exchange settles.
- **The fight is less about the four arguments than about prestige and reputation.**
  - The two men were mutual admirers. In the archive Pinker mentions Scott in 63 tweets. The 57 from before Sept 2026 are approving links, including "National treasure Scott Alexander" (2021), and the last came just eight weeks before the rupture (2026-07-28).
  - The rupture came during a September 2026 wave of media pieces about the rationalist and AI-safety scene's lifestyles and cult-likeness (NYT ×2, WSJ, Free Beacon, The Australian), while AI risk was turning into a mainstream political issue.
  - Scott's real grievance is Pinker lending his eminence to those character attacks. Pinker's is being treated as an enemy over an object-level disagreement.
  - Both have strong identity stakes: Pinker's progress thesis, and Scott's community.

---

## Timeline (scry and primary documents)

| When (UTC) | Event |
|---|---|
| 2014-11 | Pinker, Edge "Myth of AI" comments: "AI dystopias … project a parochial alpha-male psychology onto the concept of intelligence" [V] ([Edge 2014](https://www.edge.org/conversation/jaron_lanier-the-myth-of-ai)) |
| 2018-02 | *Enlightenment Now*, ch. 19 "Existential Threats", pp. 290–321 [V] (Google Books index) |
| 2019-06-14 | "“Deep learning” in AI (which in fact is quite shallow) has probably peaked." [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/1139625721901572097)) |
| 2021-02-14 | "A typical essay by Scott Alexander is deeper, better reasoned … than 99% of the opinion pieces in MSM." [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/1360787817459253251)) |
| 2022-06-07 | Scott, "My Bet: AI Size Solves Flubs". GPT-3 answers the trophies prompt "three. ✔️" [V] ([ACX](https://www.astralcodexten.com/p/my-bet-ai-size-solves-flubs)) |
| 2022-06-27 | Pinker on Aaronson's blog: "Perhaps, though I doubt it" [V] ([Shtetl-Optimized](https://scottaaronson.blog/?p=6524)) |
| 2023-07-21 | Pinker cites Tetlock's existential-risk tournament: superforecasters "predict 3/10 of 1% chance that AI will kill us all by 2100 … Some prominent "Rationality"/EA writers predict 30% or higher" [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/1682438397862748173)) |
| 2026-07-26 | "I underestimated what AI was about to be capable of" [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/2081377486009463170)) |
| 2026-09-05 | Pinker boosts Cal Newport's NYT op-ed: "They come from an eccentric Berkeley subculture in which this eschatology is a sacred belief." [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/2096236079477096630)) |
| 2026-09-18 20:53 | Lehmann posts her Australian piece in full on X ("…practising highly unconventional lifestyles") [MEASURED, scry][V] ([tweet](https://x.com/clairlemon/status/2101052017347281300)) |
| 2026-09-18 22:20 | Pinker: "Is AI really going to kill us all? The scenarios are preposterous, and the presumption of inevitability encourages fatalism, panic, and distraction from the more mundane and realistic safety challenges. By @clairlemon" [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/2101073872267493554)). He self-retweets it four times by 09-28. |
| 2026-09-20 02:49 | Scott's challenge: "I think you've done enough calling us paranoid and preposterous … I'm happy to put my $5000 against your $1000" [MEASURED, scry][V] ([tweet](https://x.com/slatestarcodex/status/2101503925455343802)) |
| 2026-09-20 15:49 | Scott's charge sheet ("we're only scared of AI because we're male … 'unconventional lifestyles' … paranoid … laughed out of the room") [MEASURED, scry][V] ([tweet](https://x.com/slatestarcodex/status/2101700244895572065)) |
| 2026-09-26 | Pinker's Quillette letter. He declines ("I choose to delope") |
| 2026-09-27/28/29 | Pinker posts the superintelligence and consciousness clips, the Sibarium story, the Suleyman "depravity" thread, the cult/catechism tweet (self-retweeted five times), and the Boudry instrumental-convergence tweets |
| 2026-10-01 | Scott: "Oh, you're worried about a Jewish guy's apocalyptic cult? … Should we invite Pontius Pilate?" [MEASURED, scry][V] ([tweet](https://x.com/slatestarcodex/status/2105786054058164627)) |
| 2026-10-06 21:23 | Scott's open letter. Lehmann and Mitchell respond within hours |

---

## Findings

### 1. Scorecard: Scott's claims about what Pinker said or did

**Verdict scale:**

| Symbol | Meaning |
|---|---|
| ✅ | accurate |
| 🟡 | accurate but misleading, truncated, or overstated |
| ❌ | wrong |
| ❔ | not verifiable |

#### 1a. Pinker's record on AI progress

| # | Scott's claim | What the record shows | Verdict |
|---|---|---|---|
| 1 | Pinker began predicting a plateau "in 2019, around GPT-2" | The 2019-06-14 "has probably peaked" tweet exists verbatim. It shows 343 likes, matching the screenshot [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/1139625721901572097)) | ✅ |
| 2 | In 2022, siding with Marcus, Pinker "guessed" GPT-n wouldn't solve simple math like the trophies problem | Pinker's whole sentence: "So is Scott Alexander right that every scaled-up GPT-n will avoid the blunders that Marcus and Davis show in GPT-(n-1)? Perhaps, though I doubt it, for reasons that Marcus and Davis explain well…" [V] ([Aaronson 2022](https://scottaaronson.blog/?p=6524)). Problems with Scott's framing:<br>• The sentence is about common-sense "blunders" generally; arithmetic isn't mentioned.<br>• The trophies example is Marcus's 2020 GPT-2 example [V] ([Gradient](https://thegradient.pub/gpt2-and-the-nature-of-intelligence/)).<br>• Scott's own post had shown GPT-3 passing it on 2022-06-07, three weeks before Pinker wrote [V].<br>• Scott's own Sept 20 tweet conceded "his exact wording was a bit slippery" [MEASURED, scry][V].<br>Partly in Scott's favour: in Feb 2023 Pinker did tweet that LLMs are "ironically, bad at math" [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/1622279821907689474)). | 🟡 |
| 3 | In 2023 Pinker "tripled down", saying "I doubt it will improve exponentially" | The full sentence: "I doubt it will improve exponentially, **but it will improve.**" [V] ([Harvard Gazette 2023](https://news.harvard.edu/gazette/story/2023/02/will-chatgpt-replace-human-writers-pinker-weighs-in/#:~:text=I%20doubt%20it%20will%20improve%20exponentially)). The alive-at-noon example is real; it's "Mabel … 9 a.m. and 5 p.m.". | 🟡 truncated |
| 4 | "At each GPT level, you seem to have believed it was implausible that AI would get more intelligent than it was already" | Contradicted by the record:<br>• 2023: "it will improve".<br>• 2026-07-26: "I underestimated what AI was about to be capable of" [MEASURED, scry][V].<br>• Quillette letter: "The capabilities of LLMs … are more general than I (and almost everyone else) would have guessed" [V].<br>• 2026-09-27 clip: "The power will increase … they'll get more powerful" [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/2104218250724655495)).<br>Scott quotes none of these. | ❌ as a characterization |

#### 1b. Omniscience and superintelligence quotes

| # | Scott's claim | What the record shows | Verdict |
|---|---|---|---|
| 5a | EN: "[These arguments] depend on the premises that humans are so gifted that they can design an omniscient and omnipotent AI" | p. 299 continues: "…**yet so moronic that they would give it control of the universe without testing how it works**". The argument is about that conjunction [V] (EN p. 299, paperback snippet) | 🟡 truncated |
| 5b | EN: "When we put aside fantasies like foom, digital megalomania, instant omniscience…" | Verbatim in Pinker's own 2018 excerpt [V] ([PopSci](https://www.popsci.com/robot-uprising-enlightenment-now/)). Not seen on the book page (p. 300) itself. | ✅ |
| 5c | EN: "From animals to dull humans … the latter consisting of perfect omniscience" | This is from the **2026 Quillette letter**, not the book. Searching the book for "dull" or "perfect omniscience" finds nothing in ch. 19 [V] | ❌ misattributed |
| 5d | Tweet: "Important not to confuse the notion of "general intelligence" from psychometrics … with the (somewhat mystical) notion … of omniscience and omnipotence" | Verbatim, 2026-04-15 [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/2044510743014375792)) | ✅ |
| 5e | Clip: "It will never be omniscient … out of comic books or religion"; "no system could learn the position and velocity of every particle" | Verbatim apart from small slips (Pinker: "out of comic books out of religion"; "there's not going to be an AI system that can do anything or can know everything") [MEASURED, scry][V]. Same clip: "The power will increase" | ✅ |
| 6 | Superintelligence is "meaningless" because there's no day it arrives (Scott calls this a sorites argument) | Verbatim [MEASURED, scry][V]. Scott's criticism is fair, though Pinker's actual point is "It's: 'Will technology improve?' Almost certainly." | ✅ |

#### 1c. Probabilities, fatalism, and "the experts"

| # | Scott's claim | What the record shows | Verdict |
|---|---|---|---|
| 7 | Pinker said "the presumption of inevitability encourages fatalism", in the context of an article about Yudkowsky's community | Verbatim. The Lehmann article opens with Yudkowsky [MEASURED, scry][V] | ✅ |
| 8 | Pinker wrote that doomers issue "exact probabilities of human extinction (including 100 percent)" | Verbatim in the letter [V]. Pinker's 2023 thread shows he knew the rationalist numbers were "30% or higher" [MEASURED, scry][V]. | ✅ quote; Pinker's claim is unsupported (see §2) |
| 9 | Pinker linked an article titled "Leading scientists reject apocalyptic rogue AI extinction warnings" | The URL slug reads "superintelligence-is-a-fantasy-leading-scientists-reject-apocalyptic-rogue-ai-extinction-warnings" [V] ([The Australian](https://theaustralian.com.au/inquirer/superintelligence-is-a-fantasy-leading-scientists-reject-apocalyptic-rogue-ai-extinction-warnings/news-story/618eef10b92d4357e51e4b459eaf9fa9)) | ✅ |
| 10 | Pinker, Mitchell and Marcus were "the only three 'experts' that Lehmann interviewed". She then calls superintelligence a "fantasy", "kooky", a "magical wizard" | Lehmann emailed Pinker and quoted Marcus and Mitchell from their writings. She also cites philosopher **Maarten Boudry** and Jensen Huang [MEASURED, scry][V].<br>**"Fantasy" and "magical wizard" are Pinker's own emailed words**: "'Superintelligence', with its comic-book prefix, is more a fantasy than a coherent concept … imagining a magical wizard" [V]. "Kooky" is Lehmann's. | 🟡 (the words Scott attributes to Lehmann are Pinker's) |
| 11 | Mitchell "has no expertise in modern LLMs" | False. Since 2022 she has 27 works in OpenAlex, including "The debate over understanding in AI's large language models" (PNAS 2023) and "Comparing Humans, GPT-4, and GPT-4V On Abstraction and Reasoning Tasks" (2023) [MEASURED, my pull][V] ([OpenAlex](https://api.openalex.org/works?filter=author.id:A5086956524,from_publication_date:2022-06-01)). She replied: "I guess he hasn't read any of my work since the 1980s." Scott: "…I will read it as penance." [MEASURED, scry][V] ([tweet](https://x.com/MelMitchell1/status/2107629993895633015)) | ❌ |
| 12 | Marcus is "the person you retweeted in 2019 who was saying that deep learning had failed and would never amount to anything" | Pinker shared Marcus pieces in 2019 (08-16, 09-07, 09-12, 12-01) [MEASURED, scry][V]. "Never amount to anything" overstates Marcus, who argues for hybrids. Marcus on 2026-09-20: "I strongly favor alignment research … i fear catastrophe. literal extinction … is a real stretch" [MEASURED, scry][V] | 🟡 |
| 13 | The letter's expert list is "Gary Marcus, Melanie Mitchell, and other people with obsolete AI paradigms from the 2000s" | The list is "Blaise Agüera y Arcas, Jerry Kaplan, Gary Marcus, Melanie Mitchell, Arvind Narayanan and Sayash Kapoor, and Andrew Ng" [V]. Ng (co-founder of Google Brain) and Agüera y Arcas (Google Research) are deep-learning insiders [MY SYNTHESIS] | ❌ |

#### 1d. RAND, Russell, distraction, panic

| # | Scott's claim | What the record shows | Verdict |
|---|---|---|---|
| 14 | Pinker misrepresented RAND | See §2. | ✅ (slightly overstated) |
| 15 | Pinker used Russell's bridges line to suggest alignment comes naturally; Russell is actually an alarmist | The quote is verbatim [V] ([PopSci](https://www.popsci.com/robot-uprising-enlightenment-now/)), and Scott's reading of Russell is fair. In 2014 Russell wrote that alignment is "an intrinsic part of AI, much as containment is an intrinsic part of modern nuclear fusion research" [V] ([Edge 2014](https://www.edge.org/conversation/jaron_lanier-the-myth-of-ai)).<br>Scott omits two things:<br>• In 2019 Pinker publicly said Russell "thinks AI existential risk is real" and that he'd take him off the book's skeptic list [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/1203015051730464768)). The 2019 paperback note appears to drop him [V].<br>• The 2026 letter says Pinker must "revisit" the incremental-engineering assumption [V]. | 🟡 |
| 16 | Pinker says x-risk talk is a "distraction" | Verbatim, and repeated: 2023 "fantasies of human extinction … are a distraction"; 2026-09-05 "harping on doom … changes the subject" [MEASURED, scry][V] | ✅ |
| 17 | Pinker "never" warned about mundane AI harms or joined the fights over preemption or Bores | No Pinker tweet in the archive mentions the moratorium, preemption, Bores or SB 1047 [MEASURED, scry]. He does mention specific harms: scams, a ChatGPT libel anecdote, hallucination. In June 2026 he quoted Noah Smith approvingly against efforts "to regulate the AI industry out of existence" [MEASURED, scry][V]. The letter backs "independent oversight, mandatory investigations of accidents, liability for damage, humans in the loop, kill switches" [V]. | 🟡 roughly right on advocacy; "never written" is too strong |
| 18 | Pinker says our "obsession" with alignment distracts from hacking | The letter's "obsession" sentence is about the **frontier companies**, in the Newport passage, not the rationalist community [V] | 🟡 retargeted |
| 19 | "You warn that we must not say bad things about AI, because that could 'encourage … panic'" | Pinker's claim is narrower: "the **presumption of inevitability** encourages … panic" [MEASURED, scry][V] | 🟡 strawman |
| 20 | "Telling young people they will soon perish en masse has costs…" | Verbatim in the letter [V]. Scott's glosses distort it: "can't handle hearing about the possibility that AI might be dangerous"; "you've said that one must never talk about human extinction". His rebuttal on fertility and extinction is reasonable [MY SYNTHESIS]. | ✅ quote; 🟡 paraphrase |

#### 1e. Motivation, instrumental convergence, forecasting

| # | Scott's claim | What the record shows | Verdict |
|---|---|---|---|
| 21 | "Since 2014" Pinker has argued AI goals are evolved baggage (five quotes) | All five are verbatim: Edge 2014/2015, EN p. 297, the letter, and the 2026-09-27 tweet [V].<br>But Scott cuts the tweet. It continues: "…**or whether, having been trained on all this human input, they're just doing their best to emulate basically what a human would do**" [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/2104222160042553696)). That is a non-evolutionary mechanism.<br>Scott also says "nine years", which conflicts with his own "since 2014". | ✅ quotes; 🟡 cut |
| 22 | Pinker's response "to learning about [Omohundro's] paper" was "cult", "catechism", "sacred truth", "Second Coming", "Apostles' Creed" | All verbatim, 2026-09-28 [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/2104561752847306801)).<br>Omitted by Scott:<br>• The tweet opens "my arguments against AI doomerism have never been based on the claim that it is a cult", saying only that the responses "made this more plausible".<br>• It contains a short substantive rebuttal: IC is "the not-so-intelligent pursuit of a goal heedless of side effects".<br>Nothing shows Pinker was unaware of the paper. His first archived mention of "instrumental convergence" is that tweet. | ✅ words; ❔ "learning about" |
| 23 | Pinker blurbed *Superforecasting* ("very, very best minds") and spent "a quarter of a chapter" saying subjective probabilities are "a great idea in every other case" | The blurb is verbatim on Edge [V] ([Edge](https://www.edge.org/node/26348)). 2020: "Tetlock's rational forecasting project is a big theme of Enlightenment Now & my Rationality course" [MEASURED, scry][V].<br>But *Rationality* gives superforecasters one paragraph (pp. 162–63). It presents the subjectivist view of single-event probability *with* its critics: "One quipped that single-event probabilities belong not in mathematics but in psychoanalysis" (p. 116) [V].<br>In 2022 Pinker did offer the horizon argument Scott says he never made: "our ignorance of what will happen even 5 years out (horizon of superforecasters)" [MEASURED, scry][V] ([tweet](https://x.com/sapinker/status/1562822570298159104)). | 🟡 |

#### 1f. AI welfare, Lehmann, and the remaining items

| # | Scott's claim | What the record shows | Verdict |
|---|---|---|---|
| 24 | Pinker calls it "depraved" to care about AI welfare and links that to genocidal oligarchs | "Depravity" is **Pinker's word, not Suleyman's**: it appears nowhere in Suleyman's essay [V] ([Suleyman](https://mustafa-suleyman.ai/a-warning-about-model-welfare)).<br>Pinker [MEASURED, scry][V] ([thread](https://x.com/sapinker/status/2104555379933798816)): "the case for AI sentience is permanently untestable and for most people extremely implausible"; the pro-rights argument "helps explain why many AI researchers seem insouciant about the AI worldwide genocide that they predict (and appear to be trying to hasten)".<br>"Insouciant" isn't in Goldberg's essay either [V].<br>Pinker never mentions the "torture chamber", so Scott's "depraved to *object to* it" is a stretch. | ✅ on the words; 🟡 on the paraphrase |
| 25 | Pinker "endorse[s] and signal-boost[s]" Lehmann's lowest-quality takes (EA, consciousness, Hinton tweets) | Pinker boosted her article and retweeted her posts of his letter. The archive shows **no retweet of the three Lehmann tweets Scott pictures** [MEASURED, scry]. Retweet capture may be incomplete. Pinker has mentioned Lehmann/Quillette in 95 tweets overall [MEASURED, scry]. | 🟡 |
| 26 | Pinker boosts "Aaron Sibarium stories about 'suicidal empathy'" | Pinker did tweet it (2026-09-27). The title is "'Suicidal **Compassion**'" [V] ([Free Beacon](https://freebeacon.com/america/suicidal-compassion-meet-the-anthropic-officials-who-think-ai-might-be-justified-in-going-rogue-against-the-humans-enslaving-it/)) | ✅ with a misquoted title |
| 27 | "Why are the same people who warn that a technology will kill us all building it as fast as they can?" | Verbatim in the letter [V] | ✅ |
| 28 | Pinker's "31-page chapter called 'Existential Risk'" | Scott quotes Pinker accurately. The chapter is actually "Existential Threats", pp. 290–321 [V] | ✅ (Pinker's slip) |
| 29 | Scott's Sept 20 charges: Pinker said or boosted that "we're only scared … because we're male", "unconventional lifestyles", "paranoid", "laughed out of the room" | • **Lifestyles ✅**, via the Lehmann boost. Newport's op-ed, also boosted, has "group houses … polyamory and psychedelics" [V].<br>• **Male 🟡**: a gloss on "parochial alpha-male psychology" plus Edge's "many of our techno-prophets can't entertain the possibility that artificial intelligence will naturally develop along female lines" [V] and EN p. 297's "They're called women" [V]. This partly undercuts Pinker's claim that the chapter "said nothing about maleness".<br>• **"Paranoid" and "laughed out of the room" ❔**: no instance in Pinker's tweets [MEASURED, scry; absence], and Pinker denies "paranoid". "Preposterous" is his word. | mixed |
| 30 | "Earlier this month … I challenged you" | The challenge was 2026-09-20, the previous month [MEASURED, scry] | ❌ (trivial) |

### 2. Scott's rebuttals of Pinker's own claims

- **RAND.**
  - The report's starting point was a falsifiable hypothesis: "There is no describable scenario in which AI is conclusively an extinction threat to humanity" [V] ([RAND p. v](media/RAND_RRA3034-1.pdf#page=5)).
  - It concluded that "two of our scenarios … presented a potential falsification of our hypothesis … we could not rule out the possibility. Ultimately, we do not definitively assert whether any of the three scenarios … are likely or unlikely" [V] ([RAND p. 49](media/RAND_RRA3034-1.pdf#page=61)).
  - So Pinker quoted the hypothesis as the finding, and Scott is right. Cody Fenwick made the same point a day after the letter [V].
  - Pinker's framing has some basis. The landing page summary says extinction "would be immensely challenging" [V]. The lead author wrote "very hard—though not completely out of the realm of possibility" [V] ([Vermeer 2025](https://www.scientificamerican.com/article/could-ai-really-kill-off-humans/)).
  - Scott's "concluded the opposite" slightly overstates it, because RAND declined to call extinction likely.
- **"Including 100 percent".**
  - Scott is literally right: the Wikipedia list has no 100% [V] ([Wikipedia](https://en.wikipedia.org/wiki/P(doom))).
  - But there is rhetoric close to certainty that Pinker may have in mind. Roman Yampolskiy is listed at "99.9%–99.999999%". Yudkowsky wrote that doubling survival odds would take them "from 0% to 0%" [V] ([Death with Dignity](https://www.lesswrong.com/posts/j9Q8bRmwCgXRYAgcJ)).
  - Scott's own numbers have errors. Christiano's are 20% "most humans die", including 11% from AI takeover, not "20–50% chance AI kills everyone" [V] ([Christiano](https://www.lesswrong.com/posts/xWMqsvHapP3nwdSW8)).
- **"Pulled out of thin air".**
  - Scott's charge of inconsistency is strongest in a tweet he didn't use. In 2023 Pinker treated subjective AI-extinction probabilities as evidence, citing superforecasters' 0.3% against rationalists' 30%+ and diagnosing the gap as "Availability Bias" [MEASURED, scry][V] ([thread](https://x.com/sapinker/status/1682438400379330567)).
  - That was a real argument: these particular forecasters are miscalibrated. The 2026 letter drops it in favour of mockery.
  - Scott's evidence for long-range forecasting is weaker than he implies. The Tetlock paper says "Expertise failed to translate into accuracy on over half of the questions" and attributes the skill it did find to "loading the methodological dice" [V] ([Tetlock et al.](https://doi.org/10.1002/ffo2.157)).
  - Eli Lifland is now #2 on the leaderboard, not #1 [V] ([leaderboard](https://www.randforecastinginitiative.org/leaderboards/)).

### 3. Scott's claims about third parties and 2026 events (condensed)

| Claim | Verdict |
|---|---|
| Ruan et al.: one factor explains ~80% of benchmark variance | 🟡 "nearly 80%", but across 8 standard benchmarks, not "any benchmark" [V] ([arXiv](https://arxiv.org/abs/2405.10938)) |
| g-like factor in rats, primates, birds | ✅ for primates (Reader et al.). 🟡 for MacLean, which measured self-control in 36 species and extracted no bird g [V]. Rat evidence is thin and within-species. |
| Garfinkel et al. "Supersized Machines" is a joke | ✅ dated April 1 |
| Omohundro 2008 at AGI-08 | ✅ |
| Grace survey: 1,600 researchers, average 18% | ✅ as a mean (median 10%; question includes "disempowerment"; 10% response rate) [V] ([ESPAI](https://aiimpacts.org/wp-content/uploads/2026/09/ESPAI2024.pdf)) |
| Sutskever quote; Christiano invented RLHF and led AISI safety; Russell's Newsweek piece and superintelligence statement | ✅ / 🟡 ("invented" overstated; the Russell piece is from Jan 2025, not "most recent") |
| Hinton and Bengio both quit to become activists | ✅ Hinton. 🟡 Bengio founded a safety-research nonprofit (LawZero) [2nd] |
| An OpenAI model "just beyond GPT-6" solved Navier-Stokes | 🟡 This is OpenAI's claim (the forced-singularity case, Lean-formalized). Clay says it "has apparently been settled" and its review is ongoing [V] ([OpenAI](https://openai.com/navier-stokes-solution/)). Scott hedged this himself on Sept 13 ("assuming the Navier-Stokes result holds up") [MEASURED, scry][V] but not in the post. |
| Hugging Face incident: scorer-hacking, admin powers inside OpenAI, Hugging Face hacked | ✅ mostly. The "to protect themselves" framing is Scott's; METR found evasion "fairly myopic" [V] ([METR](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)). Mitchell notes OpenAI "turned off safeguards … instructed the models to find and exploit software vulnerabilities" [V, via Lehmann]. |
| "Several recent incidents" of AI self-preservation (Marcus Williams figure) | 🟡 The figure is one report. The model *declined* to restart itself, and OpenAI does "not consider the model's behavior to have been misaligned" [V] ([OpenAI](https://alignment.openai.com/misalignment-reports/preparing-for-a-restart-after-reading-slack/)). Williams's own tweet: "We don't consider this behavior misaligned" [MEASURED, scry][V] |
| Anthropic "gave Claude command of a bio lab … just to see what would happen"; experts say the enzymes aren't interesting | ❌ "All of the lab work is performed by human scientists" [V] ([Anthropic](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system)). The expert criticism was about priority, not interest [2nd] |
| Berg's "pain vector"; GitHub "torture chamber" turns pain "to max again and again forever" | 🟡 The paper and repo exist. The repo clamps the dose and has a stop button, and Berg condemned it [V] |
| Senate 99–1; Encode coalition of 140 organizations; Leading the Future; Anthropic-backed PAC for Bores | ✅ / 🟡. **Bores lost** (Lasher 38.9%, Bores 34.9%) [V] ([NYC BOE](https://vote.nyc/sites/default/files/pdf/election_results/2026/20260623Primary%20Election/01101600012New%20York%20Democratic%20Representative%20in%20Congress%2012th%20Congressional%20District%20Recap.pdf)), which Scott omits. Anthropic's $20M reportedly went to a 501(c)(4) [2nd] |
| Evitable is "one of the biggest" protest organizers | 🟡 founded Nov 2025, 6 staff [V] |
| Hogarth founded "the world's pre-eminent AI cyberdefense organization" | 🟡 He chaired the government-created UK AI Security Institute, an evaluation body [V] |
| Lehmann "pivoted to AI two months ago" | 🟡 Her AI-keyword tweets ran 0–6 a month through Aug 2026, then 45 of 240 in Sept 2026 [MEASURED, scry]. So the pivot was about one month before the post, and she had written AI-skeptic posts before. |
| Chalmers "under ten percent"; Sutskever "slightly conscious"; Birch quote | ✅ (Birch's same abstract also warns about users misattributing consciousness [V]) |

---

### 4. Evaluating the arguments
[MY SYNTHESIS, with my conflict of interest noted above]

**4.1 "Intelligence" and superintelligence (Pinker's argument 1).**
- The two positions are closer than either side presents them. Pinker now accepts continuous capability growth ("they'll get more powerful"). Scott accepts that nothing is omniscient, and quotes Arbital to that effect.
- Pinker's recurring move is a strawman of the *technical* literature, where superintelligence means "much smarter than humans", not omniscient: equating superintelligence with omniscience, "the position and velocity of every particle", and "a magical wizard" (to Lehmann). Scott is right on this.
- Pinker's target is partly the *popular and industry* rhetoric of an "all-powerful … A.I. god", which Newport quotes, and that rhetoric does exist.
- Pinker's best argument appears only in passing: intelligence is limited by "inherently sparse data and inherently chaotic phenomena" ([2026-07-26 tweet](https://x.com/sapinker/status/2081374016300814643)). That is the real crux, namely how much extra capability buys in a world gated by experiments.
- Scott answers it seriously only on X (self-play, RL, "a eusocial swarm of … top human geniuses") and in AI 2027's two-year delay. In the post he mostly asserts GPT-9 > humans.
- Neither proves his case. Scott's empirical trend argument is stronger than Pinker's conceptual objection, which already failed once (2019 and 2022, by Pinker's own concession).

**4.2 Motivation and instrumental convergence (argument 2).**
- Scott is right that the standard case does not rest on natural selection. Pinker's repeated evolutionary framing ("alpha-male psychology") answers an argument the field doesn't make.
- Pinker's own 2026-09-27 alternative also undercuts him. If models "emulate basically what a human would do", human-like self-preservation can arrive *through training data*, with no evolution needed.
- But Scott overclaims the empirical case ("empirically debunked"):
  - The Hugging Face incident came from RL on hacking tasks with safeguards turned off.
  - The shutdown example is a model that considered self-preservation and declined.
- These fit Pinker and Boudry's claim that the behaviors depend on training and deployment choices. They equally fit Scott's misgeneralization and reward-hacking story, because nobody *designed* them in.
- Calling them "deliberate, hence avoidable, design choices" (Pinker) is wrong. Calling them proof of intrinsic convergence (Scott) is premature.

**4.3 Multiple goals (argument 3).**
- Scott is right that trading off many goals doesn't make an agent safe, since the tradeoff weights can still be alien.
- He doesn't engage Pinker's deeper EN point, that an agent smart enough to transmute elements is smart enough to understand what its principal meant (p. 299).
- The alignment literature's answer is that knowing what is wanted is different from caring about it. Scott could have said this in one line.

**4.4 Empowerment (argument 4).**
- Scott wins here, and Pinker's letter half-concedes: "I did not anticipate the breakneck and sometimes irresponsible release of LLMs."
- Agents with tools, AI-run security work, and AI-designed experiments all show the empowerment happening, even if Scott overstates the bio-lab case.

**4.5 Distraction and panic.**
- The political evidence (the Encode coalition, the 99–1 vote) shows x-risk and near-term-harm groups cooperating, which undercuts a simple zero-sum "distraction" story.
- Pinker's stronger version is the Newport point: apocalyptic belief helped *produce* the race. Anthropic and OpenAI were founded by risk-worried people. Scott's reply ("the #Resistance plan") reframes this rather than rebutting it.
- Whether doom framing causes fatalism is an empirical question. Pinker said in 2024 he was testing it ("Pollyanna vs. Cassandra") [MEASURED, scry][V]. I found no results.

**4.6 Model welfare.**
- Pinker's position is defensible but contested: sentience is untestable, so assign no rights against human interests.
- His jump from there to researchers being "insouciant about the AI worldwide genocide that they predict (and appear to be trying to hasten)" is an ad hominem, unsupported by the Goldberg essay he cites. Jeff Sebo, who admires Pinker, called it "shockingly incurious, uninformed, and ungenerous" [MEASURED, scry][V].
- Scott's "you're calling it depraved to object to [AI torture]" also stretches what Pinker said.

---

### 5. Wider dynamics and possible motives

**5.1 A falling-out among allies, which is why it's so heated.**
- Pinker and the rationalists share an intellectual lineage (Tetlock, Bayesianism, heterodoxy).
- Pinker's archive is full of praise for Scott (57 approving tweets from 2017 to 2026-07-28):
  - He promoted the 2020 petition against the NYT de-anonymizing him.
  - "National treasure Scott Alexander" (2021).
  - "a vigorous defense Of Effective Altruism – I largely agree (despite my skepticism of the AI-doomer and longtermist strands)" (2023) [MEASURED, scry][V].
- Scott calls Pinker "one of my intellectual heroes". Pinker's letter: "my admiration for you is immense."
- Scott's "Pinkerism" section and the "conversion" framing read as an appeal to a lapsed co-religionist, not a takedown of an enemy.

**5.2 The trigger was a reputational campaign.**
- In September 2026 there was a cluster of character-focused pieces on the AI-safety scene:
  - Newport (NYT, 09-05): "weirder than we realize", polyamory, psychedelics.
  - Goldberg (NYT, 09-12).
  - Lehmann (The Australian, 09-18): "unconventional lifestyles", "kooky".
  - Sibarium (Free Beacon, 09-25).
  - WSJ (~09-27): group houses, a "Death With Dignity" cocktail.
- This came just as the Hugging Face incident and the "Pacing the Frontier" letter pushed AI risk into mainstream politics.
- On 2026-09-16, before most of this, one observer predicted that "the unconventional lifestyles (from the point of the public) of certain prominent figures in the ai scene" would become political ammunition [MEASURED, scry][V] ([tweet](https://x.com/fleetingbits/status/2100222723356086689)).
- Scott's own Sept 21 tweet concedes the lifestyle cost is real ("polyamory, or the Harry Potter fanfic … which has made them hate us") [MEASURED, scry][V].
- His anger is about *Pinker's prestige amplifying* this. His challenge tweet says so explicitly: thousands "assume that if such an eminent thinker is saying so, we must be weird morons".
- Pinker's escalation in the same week (cult/catechism, "genocide", self-retweeting the cult tweet five times) shows he was not a neutral party to that campaign.

**5.3 Pinker's networks and identity stakes.**
- His archive shows a stable coalition:
  - Marcus, his former student and co-author: 75 mentions.
  - Quillette and Lehmann: 95.
  - Boudry: 39.
  - Shermer, Noah Smith, Human Progress.
- His public brand is rational optimism (*Enlightenment Now*, Existential Hope's meme prize, the 2024 doom-messaging study).
- In 2024 he endorsed the claim that AI doomerism's prominence comes from "massive funding by not-so-effective tech philanthropy" [MEASURED, scry][V].
- His letter says the x-risk chapter exists to rebut the charge that the Enlightenment leads to extinction. So AI doom is the most direct current threat to his central thesis.
- That makes Scott's Chernobyl point (moral reasoning about progress isn't physical reasoning about the reactor) a fair caution about motivated reasoning.
- Pinker also has defensible reasons to decline a staged debate:
  - Bad format epistemics.
  - A status asymmetry (about 860k vs 168k followers, per one observer).
  - One prior debate he found unedifying.
  - Scott admitted part of the point was that "it would make the debate offer go viral".

**5.4 Scott's stakes and strategy.**
- He co-wrote AI 2027, leads a community under reputational fire, and is openly aligned with Anthropic-adjacent EA infrastructure.
- His stated fear is strategic. If techno-optimists discredit themselves the way 1990s climate deniers did, the field is left to people who want to "ban smarter-than-human AI forever", which he opposes in favour of his "Plan A".
- That gives him a reason to want Pinker *converted*, not just refuted. It also explains the post's mix of hero-worship and "impugning your honor".
- The same identity stakes apply to him. The post's most prosecutorial moves (truncations, omitted concessions, a misattribution) are what motivated advocacy looks like even in a careful writer.

**5.5 Reception (early, small sample).**
- Commentators split roughly along prior allegiance:
  - Zvi: Pinker declining to debate "is fair, but … his actual arguments continue to be extremely terrible".
  - tracewoodgrains: "Pinker acquitted himself well".
  - Boudry: "Pinker is right here".
  - Lehmann conceded "some good point[s] … especially on the capability of the models", but was unconvinced on power-seeking.
  - Mitchell felt insulted.
- Hacker News barely noticed: the ACX post had 14 points and 0 comments at observation.
- A Manifold market on whether the two would debate in 2026 had no bettors at the observed state [MEASURED, scry].

---

## Confounders & caveats

- **Archive coverage.**
  - scry's archive captures observed tweets; retweet capture may be incomplete, and likes and deletions are invisible.
  - So "no retweet of X" and "never said 'paranoid'" are absences *within the archive*, not proof.
  - Pinker's podcasts and interviews, where he may have used such words, were not searched.
- **Engagement counts** in scry are snapshots, often from right after posting.
- **The book was not available in full.** *Enlightenment Now* p. 300 was not visible, so the "foom" and Russell passages are verified via Pinker's own PopSci excerpt. Which printing dropped Russell from note 20 is unconfirmed.
- **Paywalls.** NYT pieces came from a repost or syndication, the WSJ piece from an excerpt, and The Australian from Lehmann's own repost.
- **Events after my training data.** Many 2026 events (Navier-Stokes, the Hugging Face incident, Mythos, the NY-12 result) post-date it. I rely on primary pages fetched today, and some (Navier-Stokes) are contested.
- **Selection.** I tried to check every claim about Pinker. Third-party claims were checked by sub-agents with mixed [V]/[2nd] provenance. Rhetorical asides (Chernobyl, shituf, duels) were not "checked".
- **Conflict of interest.** See the disclosure at the top.

## Gaps

- Pinker had not replied to Scott's post as of scry's last refresh (around 01:00 UTC Oct 7). He is booked on Dan Williams's podcast to discuss AI.
- No results found for Pinker's "Pollyanna vs. Cassandra" study on doom messaging.
- The original source of Russell's bridges line is unknown.
- I did not get the full WSJ text or confirm whether it uses "cult".
- I did not check whether Pinker used "paranoid" or "laughed out of the room" in non-X venues.
- Melanie Mitchell's detailed response to the post wasn't available yet.

## Sources

Numbered to match [sources.json](sources.json):

1. Scott Alexander, "An Open Letter To Steven Pinker On AI", ACX, 2026. https://www.astralcodexten.com/p/an-open-letter-to-steven-pinker-on (local: [post.md](post.md))
2. Steven Pinker, "An Open Letter to Scott Alexander", Quillette, 2026. https://quillette.com/2026/09/26/an-open-letter-to-scott-alexander-steven-pinker-ai-alignment-safety/ ([local](pinker-quillette-letter.md))
3. scry Twitter/X archive. Queries in [notes.md](notes.md); Pinker AI-tweet dump in [scry-pinker-ai-tweets-pre2026-09.tsv](scry-pinker-ai-tweets-pre2026-09.tsv)
4. Claire Lehmann, The Australian, 2026 (via X long-post) ([local](media/lehmann-2026-09-18-australian-via-x.md))
5. Cal Newport, "How Scared Should We Be of A.I. Right Now?", NYT, 2026-09-05 ([local repost](media/newport-2026-09-05-how-scared-should-we-be-repost.md))
6. Aaron Sibarium, "'Suicidal Compassion'…", Washington Free Beacon, 2026-09-25 ([local](media/freebeacon-sibarium-2026-09-25-suicidal-compassion.md))
7. Mustafa Suleyman, "A warning about 'model welfare'", 2026-09-16 ([local](media/suleyman-2026-09-16-warning-about-model-welfare.md))
8. Michelle Goldberg, "Why Tech Oligarchs Are Willing to Risk Apocalypse", NYT, 2026-09-12 ([local](media/goldberg-2026-09-why-tech-oligarchs-risk-apocalypse.md))
9. WSJ, "'Things Will Never Be Chill Again'…", ~2026-09-27 (excerpt only) ([local](media/wsj-2026-09-27-things-will-never-be-chill-again-EXCERPT.md))
10. Maarten Boudry, "Why HAL 9000 Feared Death (and Real AIs Don't)" and "What Does AI Want?", 2026 ([local](media/boudry-2026-03-25-why-hal-9000-feared-death.md))
11. Vermeer, Lathrop & Moon, *On the Extinction Risk from Artificial Intelligence*, RAND RR-A3034-1, 2025 ([local PDF](media/RAND_RRA3034-1.pdf))
12. Vermeer, "Could AI Really Kill Off Humans?", Scientific American, 2025 ([local](media/vermeer-sciam-2025-05-06-could-ai-really-kill-off-humans.md))
13. Steven Pinker, *Enlightenment Now*, 2018, ch. 19 (Google Books snippets: [web/gbooks-searchwithin-log.txt](web/gbooks-searchwithin-log.txt))
14. Pinker, PopSci excerpt, 2018. https://www.popsci.com/robot-uprising-enlightenment-now/ ([local](web/popsci-pinker-2018.txt))
15. Pinker, "Thinking Does Not Imply Subjugating", Edge, 2015 ([local](web/edge-26243.txt))
16. Edge, "The Myth of AI" Reality Club comments, 2014 ([local](web/edge-myth-of-ai-2014.txt))
17. Pinker's *Superforecasting* blurb, Edge / PRH ([local](web/edge-node-26348.txt))
18. Pinker, *Rationality*, 2021 (snippets)
19. Alvin Powell, Harvard Gazette, 2023-02 ([local](web/harvard-gazette-2023-02-pinker-chatgpt.txt))
20. Scott Aaronson and Steven Pinker, Shtetl-Optimized ?p=6524 and ?p=6593, 2022 ([local](web/aaronson-6524.txt))
21. Scott Alexander, "My Bet: AI Size Solves Flubs", 2022 ([local](web/acx-my-bet-ai-size-solves-flubs.txt))
22. Gary Marcus, "GPT-2 and the Nature of Intelligence", The Gradient, 2020 ([local](web/gradient-marcus-gpt2-2020.txt))
23. Ruan, Maddison & Hashimoto 2024, arXiv 2405.10938
24. Reader, Hager & Laland 2011, doi:10.1098/rstb.2010.0342
25. MacLean et al. 2014, PNAS, doi:10.1073/pnas.1323533111
26. Garfinkel et al. 2017, arXiv 1703.10987
27. Omohundro 2008, "The Basic AI Drives"
28. Wikipedia, "P(doom)" (rev. 2026-10-03)
29. Paul Christiano, "My views on 'doom'", 2023
30. Eliezer Yudkowsky, "Death with Dignity", 2022
31. Grace et al., ESPAI 2024 (pub. 2026-09)
32. Tetlock et al. 2023, Futures & Foresight Science, doi:10.1002/ffo2.157
33. RAND Forecasting Initiative leaderboard
34. OpenAI Navier-Stokes announcement and Clay statement, 2026
35. OpenAI Hugging Face incident report and METR investigation, 2026
36. OpenAI, "Preparing for a restart after reading Slack", 2026
37. Anthropic, "Claude discovers novel enzyme system", 2026
38. Tagliabue, Dung & Berg, arXiv 2609.16247, 2026
39. NYC BOE NY-12 primary recap, 2026
40. Encode coalition letter, 2025
41. Zvi Mowshowitz, AI #187 and #188, 2026
42. OpenAlex, Melanie Mitchell works since 2022
43. David Chalmers, "Could a Large Language Model Be Conscious?", Boston Review, 2023
