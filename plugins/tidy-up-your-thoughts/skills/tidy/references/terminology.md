# Terminology — sourcing a word before using it

A report that uses a domain term it has not checked is wrong in a way the reader cannot see: the word
carries a definition the writer did not choose, and the argument inherits it. This file is the
procedure for the second step of `tidy`.

## The two registers

| | The user's terms | Domain terms |
| --- | --- | --- |
| Where they come from | `summary.md` → 詞的用法 | statute, standard, specification, textbook, field usage |
| How they are used | exactly as written | defined at first use, sourced in 詞的定義 |
| Changing them | forbidden | allowed, with the change stated |
| Example | 「簽約人」 | 「擔保人」「清算」「名義本金」 |

**Never promote the user's word into a professional category.** 「簽約人」 is a person who signs;
「決策單位（DMU）」 is a marketing taxonomy with its own claims about roles and influence. Writing the
second where the user said the first silently adds a theory of how organisations buy.

## Source hierarchy

Take the highest tier that answers the question. One tier below is acceptable if stated; two tiers
down needs a reason.

| Tier | Source | Why |
| --- | --- | --- |
| 1 | the instrument itself — the statute, the rulebook, the standard, the official specification | it defines the term it uses, and its definition binds |
| 2 | the regulator's or standards body's own glossary or guidance | an authorised reading of tier 1 |
| 3 | a peer-reviewed textbook or a primary paper in the field | the field's settled usage, with a date |
| 4 | a practitioner reference, an audited filing, an exchange rulebook | usage in the market, not the definition |
| 5 | reporting and commentary | evidence that a term is used, never evidence of what it means |

Wikipedia, an SEO article and a model's memory are not on the ladder. A term whose only support is one
of those gets deleted from the report.

## What to record

One row per term in the report's 詞的定義 section:

| 詞 | 定義（一句） | 來源 |
| --- | --- | --- |
| 簽約人 | 以自己名義在合約上簽署、承擔合約責任的一方 | 用戶定義 [Q6] |
| 名義本金 | 用以計算手續費與風險暴露的合約面額，不必然等於實際交付金額 | HKMA 《…》 第 3.2 段，2026-11-17 檢索 |

The source cell names the document and the place inside it — section, paragraph, page — and the date
the report writer read it. A URL alone fails the test six months later, when the page has changed.

## When a term means two things

Some words are contested across fields, and the report cannot use one sense while the reader supplies
the other. Two policies, in order:

1. **The user's sense wins inside the report**, and the divergence is stated:
   「本報告的『清算』指交易後的資金與資產交收（用戶用法 [Q4]）；傳統金融文獻中該詞另指結算與交收之間
   的環節。」
2. **Where the report must use the field's sense**, it says so and gives both:
   「以下採用《…》對『清算』的定義，與 Q4 的用法不同：前者指……」

The divergence paragraph is affirmative. It states what each sense is; it does not declare one wrong.

## Worked cases

**「清算」** — in a regulated market the word covers clearing and settlement stages with defined
obligations; in a crypto setting it usually names a liquidation of a collateralised position. A report
that mixes them describes two different businesses under one heading. Tier 1 source for the regulated
sense; the user's usage for the other; both in 詞的定義, divergence stated.

**「供給側」** — an economic-policy term with a specific lineage, often used loosely to mean "the side
that produces". If the report means "the party providing the instrument", say that instead and drop
the term; a historical policy programme is not a description of a business.

**「微利」** — in Chinese business usage it names a thin unit margin. The report's meaning is
「低單位費率」, which is a different statement about a different quantity. The term is defined at first
use, even though it is the user's own word, because a reader will supply the other meaning.

## The test before any term is used

1. Can I state its definition in one sentence, in the report's own words?
2. Can I name where that definition comes from — a paragraph, a page, a date?
3. Would the sentence still say the same thing if the term were removed and the phenomenon described?

If (1) or (2) fails, remove the term. If (3) is yes and nothing is lost, remove it anyway — the
sentence gets shorter and the reader gets a fact.
