# Incident report — skeleton

Copy into the host's report path (`~/thoughts/<topic>/friction/…` or `<repo>/docs/retro/…`) and fill.
Every section is required; a section with nothing to say is a sign the step was skipped.

---

```markdown
# <一句話的事件> — 2026-11-16

## 事件

<What happened, observable, with the artefact. 「refine 在合併六份回報時，格式核對發生在合併之後，
第一份報告已經寫入。」 No adjectives, no self-assessment.>

## 指引

- 當時遵守的原文：`skills/refine/SKILL.md:64` —「<verbatim quote>」
- 當時的讀法：<one declarative sentence: what the agent believed, and why that line produced it>
- 形態：<misleading rule | silent gap | conflicting rules>

<For a silent gap: 缺口 — `skills/<name>/SKILL.md` 缺少一條關於 <moment> 的規則。>

## 反模式

### AP-004 · 合併後才驗格式

- 觸發：多個 subagent 的回報需要合成一份產物時
- 錯誤動作：先把六份合成一份，再檢查格式
- 為何看起來合理：合併像整理，檢查像挑錯；整理在前符合直覺
- 正確動作：逐份對照規格驗一次，全部通過才合併
- 可觀察徵兆：合併完成後才出現一輪格式修補
- 來源：2026-11-16 refine 首次實戰

## 改進

**改進類別**：提示改進

**未採用**：流程改進（合併步驟本身沒有錯，次序才是）；資訊改進（規則已有，是位置不對）；
代碼改進（沒有腳本參與這一步）

**為何不用提示**：<required only when 流程改進 is chosen>

### 落地

- `skills/refine/SKILL.md` 第 5 步改為先驗後併，`version` 0.1.1 → 0.1.2
- 反模式索引新增 AP-004

## 回歸判準

下次合併多份回報時，第一份產物出現前已完成一次逐份核對；若合併後再出現格式修補，即判未修好。
```

---

## Notes on filling it

- **事件** holds only what can be observed. 「我沒有先驗」 is an interpretation; 「合併已完成，核對在其後」
  is an observation.
- **指引** is the load-bearing section. If no citation can be produced, the shape is a silent gap, and
  the gap names the file and the moment. A report with neither is a complaint.
- **反模式** is written for a stranger: no file names, no dates outside 來源, no product names.
- **改進** records the three rejections. Their reasons are what show the cause was located rather than
  guessed.
- **回歸判準** is a sentence about the future, checkable by someone who was not in this session.
