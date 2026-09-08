# FV直下の必須訴求3点を戻す

- **Started:** 2026-09-08
- **Completed:** 2026-09-08
- **Rule:** `docs/design-docs/pre-code-design-blueprint.md`「必須訴求3点」／
  `harness/contracts/mix-lp.yaml` の `facts-are-client-confirmed-only`
- **Completed path:** `docs/exec-plans/completed/restore-required-messaging.md`

## Goal

依頼者指定の3語（恋愛リアリティ体験／最大4〜6組／日〜木曜日限定）が、
**FV直下に読める文字として**並んでいる。開催期間の日付は戻さない。

## Scope

- [x] カンプ17と実装の差分を、装飾要素とCSS値で突き合わせる
- [x] 設計メモから「設計済みで未実装」を洗い出す
- [x] FV直下の3点要約を戻す
- [x] 使われなくなった `.hero__audience` / `.hero__date` のCSSを消す

## Non-scope

- **3枚の概要スライド**（`overview-motion-spec.md`）。**カンプ17に入っていない。**
  仕様自身が「実装前の設計メモ」「デザイン確認が終わってから」と書いており、
  `implementation-respects-the-frozen-comp` は実装者がカンプを再設計することを禁じている。
- 開催期間の日付。開催情報セクションと重複するため戻さない（2026-09-08の指示）。

## Constraints

- 依頼者の「FV直下の開催情報を消す」指示を戻さないこと。
- 支給バナーの焼き込みだけに頼らないこと。SPでは約8pxで読めない。

## Acceptance

- [x] 3語がFV直下に画面上の文字として出ている
- [x] 日付は出ていない
- [x] 装飾とCSS値がカンプ17と一致したままであること

## Verification

- [x] タグとコメントを除いた表示テキストで3語の出現位置を数える
- [x] `node scripts/build.mjs` / `node scripts/harness/harness-check.mjs`
- [x] `tools/render.sh` で目視

## Result

| 検証 | 実際の出力 |
| --- | --- |
| `node scripts/build.mjs` | `Built css/style.css`（Sassの非推奨警告なし） |
| `node scripts/harness/harness-check.mjs` | 機械判定すべて pass、`manual` 29行 |
| 表示テキストの語数（タグ・コメント・`<svg>`・`<head>` を除去して算出） | 恋愛リアリティ体験 **3回**（sr-only の h1 ／ FV直下 ／ 仕組み）、最大4〜6組 **2回**、日〜木曜日限定 **2回** |
| FV冒頭の並び | `… AFTER DARK 01 恋愛リアリティ体験 02 最大4〜6組 03 日〜木曜日限定 予約はこちら …`。**日付は出ていない** |
| `tools/render.sh tmp/probe/hero.html 700` | 3点要約がバナー直下・CTAの上に並ぶことを目視 |

### カンプ17との突き合わせ（先に実施）

| 項目 | 結果 |
| --- | --- |
| `.shape` 系（orb / pink / side / top / berry / hot / violet） | **カンプ17側で全部 `display:none`。**過去カンプの残骸なので未実装が正しい |
| padding | intro 88/118・benefits 96/100・mechanism 102/102・info 108/108 —— **全部一致** |
| `.title` 24px / 1.38、`.body` 13px、カードの丸み、番号の色、期間の色、`4〜6` の字寸 | **一致**（`18px` と `var(--radius)` のような表記差のみ） |

**カンプとの意図しないズレは無かった。**差はすべて依頼で意図的に変えた分。

### 見つけた本当の欠落

**必須訴求3点がページ下部にしか無くなっていた。**

2026-09-08に「FVのすぐ下の開催情報を消して」と言われて `.hero__summary` を丸ごと消したが、
**その中には日付だけでなく3点要約も入っていた。**日付は開催情報セクションと重複するので
消して正しいが、「恋愛リアリティ体験」「最大4〜6組」は開催情報ではない。

| | 修正前（画面上） | 修正後 |
| --- | --- | --- |
| 恋愛リアリティ体験 | 1回（仕組みセクション） | **2回**（FV直下＋仕組み） |
| 最大4〜6組 | 1回（仕組みセクション） | **2回**（FV直下＋仕組み） |
| 日〜木曜日限定 | 1回（開催情報） | **2回**（FV直下＋開催情報） |

**同じ指示を二度と取り違えないよう、HTMLに「消さないこと」と理由を書いた。**

### 検証していないこと、残っているリスク

- **3枚の概要スライドは未実装のまま。**カンプに無いので足していない。
  実装するならカンプ工程へ戻す必要がある。
- 実機では見ていない。確認は qlmanage の375px幅。
