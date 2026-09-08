# 「いつもの夜を予定外に」をスクロールで重なるカードにする

- **Started:** 2026-09-08
- **Completed:** 2026-09-08
- **Rule:** 2026-09-08 の依頼者の指定
  （futuretrain.jp の Future Imagination Course と同じ流れにしたい）
- **Completed path:** `docs/exec-plans/completed/scroll-stacked-cards.md`

## Goal

スクロールすると3枚のカードが重なりながら現れる。**JavaScriptを使わない。**
Codex が同じ判断を再現できるよう、ハーネスと設計メモが実装と一致している。

## Scope

- [x] 参考サイトの実装を**実物を開いて**読む
- [x] 同じ機構で組み直す（横スライドを置き換え）
- [x] 全セクションの `overflow` を `hidden` → `clip` にする
- [x] 使わなくなった `js/slider.js` と旧CSSを消す
- [x] **ハーネスの旧スライド規則を書き換える**
- [x] 設計メモ・AGENTS.md・gotcha を実装に合わせる

## Non-scope

- イベント概要（01 WHAT IS MIX → 02 CHIME → 03 CROSS）のスライド化。重複するため。
- カード枚数の増減。

## Constraints

- **JSを増やさない。**参考サイトが使っていないため。
- 3枚とも常にDOMに在ること。
- 装飾の切り抜きを失わないこと。

## Acceptance

- [x] 1枚目がスクロール中に上へ貼り付く
- [x] セクションの `overflow` が `clip`
- [x] JSファイルが増えていない
- [x] 3枚ともDOMに在る

## Verification

- [x] `node scripts/build.mjs`
- [x] `node scripts/harness/harness-check.mjs`
- [x] 実ブラウザで sticky の固定を実測
- [x] `tools/render.sh` で目視

## Result

| 検証 | 実際の出力 |
| --- | --- |
| 参考サイトの実装 | 1枚目 `position: sticky; top: 0`、2枚目以降 `position: relative` + `clip-path: inset(0px)`、全て `height: 100svh`、セクションは `overflow-x: clip`。**scroll駆動CSSルール 0件、JS不使用** |
| `node scripts/build.mjs` | `Built css/style.css`（途中で括弧不整合を1回出したので該当箇所を削除して解消） |
| `node scripts/harness/harness-check.mjs` | 機械判定すべて pass |
| セクションの overflow | `clip`（`hidden` から変更） |
| sticky | `scrollIntoView` 後に `top: 12` → 320pxスクロール後も `12` → 640px後も `12`。**固定されている** |
| カード | `cardCount: 3`、高さ 268px |
| JS | `js/slider.js` を削除。**このセクションのJSは0** |
| コンソール | エラーなし |

### いちばん効いた発見

**`overflow: hidden` ではなく `overflow: clip`。**

`hidden` はスクロールコンテナを作るので、**その中の `position: sticky` が無効になる。**
`clip` は作らないので sticky が生きる。切り抜きの効果は同じ。

**このプロジェクトで2回踏んでいる** —— ヘッダー（`.page` が hidden で貼り付かなかった）と、
今回のカード。2回目は**参考サイトが `overflow-x: clip` を使っているのを見て**気づいた。
向こうがそう書いているのには理由がある。

### ハーネスを書き換えた（前の規則が実装と食い違うため）

| 旧 | 新 |
| --- | --- |
| `slider-scrolls-without-js`（`scroll-snap-type` を要求） | **`stacked-cards-need-overflow-clip`**（`overflow: clip` と `position: sticky` を要求） |
| `slider-keeps-every-card-readable` | **`stacked-cards-appear-on-scroll`**（作り方と守ることを言葉で） |
| `slider-has-no-autoplay` | 残す（理由の記述を現状に合わせた） |

**放置すると、直後の commit で落ちるか、Codex が別のものを作る。**

### 検証していないこと、残っているリスク

- **実機で見ていない。**確認はブラウザの375pxエミュレーションと qlmanage。
  **重なりの手応えはスクロールの慣性で変わる**ので、実機で見て高さを詰め直す可能性がある。
- **カードの中身が薄い。**参考サイトのカードは画像＋本文＋導線で埋まっているが、
  こちらは1行＋1文。`min(42svh, 268px)` に抑えたが、**まだ白が余っている。**
  埋めるなら中身を足す判断が要る（カンプ工程へ戻す）。
- `overflow: clip` は Safari 16 以降。**それ以前では切り抜きが効かず装飾がはみ出す**
  （sticky は効く）。対象ブラウザの取り決めはまだ無い。
