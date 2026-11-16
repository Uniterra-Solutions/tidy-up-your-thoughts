# The report skeleton

Copy this into `~/thoughts/<topic_name>/report.md` and fill it. Delete a section only when it has
nothing to hold — never leave an empty heading as a promise.

---

```markdown
# <topic_name>

<Topic in one line, the reader's entry. No heading above this.>

## 摘要

<Under 150 characters: what this is about, and the state the discussion reached. A reader who stops
here knows what was decided and what was not.>

## 主題與範圍

<First sentence states what the report covers. Then what it leaves out, and why the boundary sits
there. Example topic sentence: 「本報告處理的是企業客戶的採購主體與交付容量，兩個問題在紀錄中互相
牽動。」>

## 現在確立的

<Ordered by support strength, not by when it was said. One paragraph per statement, or one table when
the statements are parallel.>

<Example topic sentence: 「定價權目前集中在創辦人一人手上，紀錄中沒有書面規則。」>

## 判準與條件

<The criteria the user stated, and the condition each conclusion carries. A claim without its scope is
not finished: 在什麼條件下、對誰、多久。>

## 壓力測試

<Which situations from refine.md were met, on what criterion, and which were not. Unanswered ones keep
their id. Example topic sentence: 「五個情境之中，兩個得到可觀察的判準，三個停在方向。」>

## 尚未確立的

<The open questions, each with the piece that is missing. No tasks, no steps — the missing piece, not
the plan.>

## 詞的定義

| 詞 | 定義（一句） | 來源 |
| --- | --- | --- |
| <term> | <one sentence, the report's own words> | 用戶定義 [Q3] |
| <domain term> | <one sentence> | <document, section, retrieval date> |

## 附錄

<Diagrams from diagrams/, embedded by path. The source index: every [Qn] used, with its question in
one line. Revision history, when a correction changed a conclusion.>
```

---

## A paragraph that holds

> 定價權目前集中在創辦人一人手上，紀錄中沒有書面規則。兩次報價都出現在通話之中，會後沒有留下數字
> [Q9][Q11]。這個狀態在第一個企業客戶要求書面報價時結束：採購流程要求一個寫下來的數字，而該數字
> 一經發出，即成為後續客戶的參照。

Three properties, all of them checkable: the first sentence is the claim; the second supplies the
evidence with its citations; the third states the condition under which the claim stops holding.

## A rebuttal block

```markdown
### 反駁：企業客戶的續約可以沿用個人客戶的續費率

對方論證的完整形態是這樣：個人客戶的續費率約七成，續費代表課程有效；企業客戶購買同一套課程，
成效判斷因此可以沿用同一個比率。前提是續約的決定者與受益者一致。

紀錄中的決定者並不一致。個人客戶由家長決定續費 [Q4]；企業客戶由人事部門決定續約，而人事部門的
衡量標準是員工表現，不是課程滿意度 [Q6][S05]。

由此可以說的只有一句：企業續約的判準尚未確立，七成的續費率在這個場景中沒有對應的樣本。
```

The first paragraph is the counter-argument at full strength — premises, evidence, inference,
conclusion. The second names the observation that breaks it. The third states what follows, at the
scope the observation supports, and it stops there: the record holds no data on enterprise renewal,
so the report claims none.

## Two sentences to rewrite on sight

| As written | Why it fails | Rewritten |
| --- | --- | --- |
| 「因此這個方向並不可行。」 | a negation standing alone: no counter-argument was built, so nothing was refuted | 「這個方向成立所需的前提是 X；紀錄中的 X 是 Y [Qn]。」 |
| 「我們應該先處理簽約主體的問題。」 | an imperative: advice, not description | 「簽約主體是尚未確立的一項，紀錄停在 Q6 的追問。」 |
