# Writing rules for the record

The record is a description of a conversation about a thought. It is read weeks later, by someone
who has forgotten the session, and it is read as fact. Everything below follows from that.

## 1. Declarative only

Every sentence states what is. The voice is descriptive and nominal.

| Not allowed | Why | Written as |
| --- | --- | --- |
| 「你應該先確認需求。」 | advice; the record holds no agent opinion | 「需求尚未確認，這件事在 Q9 被提出。」 |
| 「我們來看看邊界在哪。」 | imperative, and it narrates the process | 「邊界在 Q11 被問到，答案停在『看情況』。」 |
| 「這樣做對嗎？」 | rhetorical question inside a document | 「這個做法在 Q14 被質疑，理由是成本未計入。」 |
| 「很明顯，這個方向行不通。」 | verdict with no warrant | 「這個方向的前提在 Q18 落空，理由如下。」 |

Rules of the sentence itself:

- **Nominal phrasing** carries the subject. 「推送通道的維護成本高於主動查詢」 beats 「維護推送通道
  很貴」.
- **Passive where the actor is unknown or irrelevant.** 「這個假設從未被檢驗」 rather than 「我們沒有
  檢驗這個假設」, which invents an actor.
- **Rotate the shape.** Four consecutive sentences of the form 「A 是 B」 read as a list of slogans.
  A definition, a consequence, a contrast and a condition, in some order, keep the page readable.
- **No sentence ends on a hook.** A closing clause that invites agreement (「不是嗎」「可想而知」)
  imports argument into a document that is supposed to hold description.
- **Every negative sentence names its object.** 「不可行」 is not a sentence; 「在缺少第一批使用者的
  條件下不可行」 is.

## 2. Negation pays a debt first

A negative claim is cheap to write and expensive to trust. It is written in three moves, in order,
and skipping the first move invalidates the other two.

**Move 1 — construct the strongest version.** State the claim being negated at its best: its
premises, its warrant, the evidence its smartest defender would bring, and what it would explain if
true. Declarative sentences only. This is not a courtesy to the opposition; it is the only way to
know what is being refuted.

**Move 2 — break the warrant.** Name the specific observation, condition or measurement that the
strongest version cannot absorb.

**Move 3 — state what follows.** The conclusion, scoped to exactly what move 2 broke. A negation
that generalises past its own evidence is a new unsupported claim.

### Case 1 — a direction

> **Not this:** 這個方向不可行。

> **This:**
> 這個方向的前提是需求會在半年內出現。支持這個前提的論證是：同類產品在三個市場的採用曲線形狀
> 一致，且這三個市場的付費意願都高於本地（最強版本）。
> 你剛才說的第一批使用者來自一個尚未成立的組織，採用曲線的起點因此沒有對應的群體；同類產品的
> 曲線不能遷移到一個沒有起點的情境（warrant 被打破）。
> 在第一批使用者到位之前，這個方向的前提不成立。需求本身是否存在，尚未被檢驗。

### Case 2 — a method

> **Not this:** 自建比採購划算。

> **This:**
> 自建的論證是：成本隨規模攤薄，控制權完整，長期單價低於任何供應商報價（最強版本）。
> 這個論證成立需要一個條件：使用量在攤薄週期內不下降。你剛才描述的場景在第三個月會有一次需求
> 重估，重估的結果可能是減半。
> 在使用量可能減半的前提下，攤薄的假設落空；「長期單價更低」在這個場景裡沒有對應的數字。

### Case 3 — a person's position

> **Not this:** 他不同意是因為他保守。

> **This:**
> 他的立場可以完整表述為：現金流在任何擴張之前必須先自給，因為上一次擴張的教訓是應收帳款拖了
> 十四個月（最強版本）。
> 你提出的方案在第一年需要外部資金，這一點與他的前提直接衝突，與保守與否無關。
> 分歧的位置是現金流的時序，不是風險偏好。

## 3. What never enters the record

- **The agent's recommendation**, however good. It belongs in the conversation, addressed to the
  user, and only if he asks.
- **Any claim not traceable to a `[Qn]`.** A line in `summary.md` without provenance is a claim the
  reader cannot check.
- **A paraphrase presented as the user's words.** Quotation marks mean the sentence was said;
  paraphrase is marked as paraphrase.
- **Process narration.** 「接下來我會問你三個問題」 describes the session, not the thought.

## 4. Lint before closing

Run these five over `summary.md` and `README.md`; each is a mechanical read, not a judgement.

1. Any sentence containing 「應該」「必須」「建議」 — advice entered.
2. Any negative sentence whose object is unnamed — the debt is unpaid.
3. Any paragraph of more than three sentences sharing one shape — rotate.
4. Any `[Qn]` that does not exist in `qa.md` — invented provenance.
5. Any term in the text that a non-specialist would have to look up — apply the noun test from the
   skill body.
