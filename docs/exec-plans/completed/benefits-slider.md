# 「いつもの夜を予定外に」を横スライドにする

- **Started:** 2026-09-08
- **Completed:** 2026-09-08
- **Rule:** `docs/design-docs/overview-motion-spec.md`（スライドの動きの仕様）／
  2026-09-08 の依頼者の判断（適用先を YOUR NIGHT にする）
- **Completed path:** `docs/exec-plans/completed/benefits-slider.md`

## Goal

YOUR NIGHT の3項目が1枚ずつ送れる。**縦積みで見えていた3枚が、
操作しないと2枚見えなくなる損**を、仕様どおりの4つの約束で埋めてある。
Codex が同じ判断を再現できるよう、ハーネスと設計メモが実装と一致している。

## Scope

- [x] 3枚のカードを横トラックにする
- [x] 次のカードの端を見せる
- [x] 現在位置（点＋読み上げ）と矢印
- [x] 自動再生しない
- [x] **ハーネスに書く**（機械2本・manual 1本）
- [x] `overview-motion-spec.md` の「適用先が変わった」を明記
- [x] `AGENTS.md` に要約

## Non-scope

- **イベント概要（01 WHAT IS MIX → 02 CHIME → 03 CROSS）のスライド化。**
  確定事実は独立セクションで順に読ませる構成が確定済みで、重複する。
- カード枚数の増減。

## Constraints

- **JSが死んでも3枚とも読めること。**横移動はCSSに持たせる。
- 読み上げ・検索に3枚とも届くこと（JSで隠さない）。
- タップ領域44px。

## Acceptance

- [x] DOMに3枚とも在る
- [x] 次のカードの端が見えている
- [x] 現在位置が更新される
- [x] 自動再生が無い
- [x] 先頭で「前へ」、末尾で「次へ」が無効

## Verification

- [x] `node scripts/build.mjs`
- [x] `node scripts/harness/harness-check.mjs`
- [x] 実ブラウザ（375px）で送り動作・現在位置・端の見え幅を実測
- [x] `tools/render.sh` で目視

## Result

| 検証 | 実際の出力 |
| --- | --- |
| `node scripts/build.mjs` | `Built css/style.css`（非推奨警告なし。1回出たので入れ子より前に宣言を移動して解消） |
| `node scripts/harness/harness-check.mjs` | 機械判定すべて pass |
| DOM | `cardsInDOM: 3`。**JSで隠していない** |
| CSS | `scroll-snap-type: x mandatory` / `overflow-x: auto` |
| 次の端 | **62px** 見えている |
| 送り | 点が 0→1→2、読み上げ `1 / 3` → `2 / 3` → `3 / 3`、`scrollLeft` 0 → 261 |
| 端の状態 | 先頭で `prev.disabled = true`、末尾で `next.disabled = true` |
| コンソール | エラーなし |
| 描画 | 01が表示され、02の端が右に覗く。点と矢印が下に並ぶ |

### ハーネスに入れたもの（Codexと同じ動きにするため）

| id | 型 | 見ているもの |
| --- | --- | --- |
| `slider-has-no-autoplay` | forbidden-content | `js/` に `setInterval` / `autoplay` が無い |
| `slider-scrolls-without-js` | required-content | `css/` に `scroll-snap-type` が在る＝横移動をCSSが持っている |
| `slider-keeps-every-card-readable` | manual | 4つの約束と、その理由 |

**古い記述も直した。** `futuretrain-course-slide-grammar` は
「01 WHAT IS MIX → 02 CHIME → 03 CROSS の3枚にする」と書いてあり、
**実際の決定と食い違っていた。**放置すると Codex が別のものを作る。

### 検証していないこと、残っているリスク

- **実機のスワイプは試していない。**確認はブラウザの375pxエミュレーションと矢印クリック。
  `scroll-snap` は素の挙動なので効くはずだが、慣性の効き方は実機でしか分からない。
- **2枚目・3枚目が実際に読まれるかは測っていない。**
  縦積みより読まれる確率は下がる。**公開後に見るなら、そこを見る指標が要る。**
- `prefers-reduced-motion` では全アニメーションが止まるが、
  **`scroll-behavior: smooth` を使っていない**（`scrollTo({behavior:'smooth'})` はJS側）。
  OS設定を実際に切り替えての確認はしていない。
