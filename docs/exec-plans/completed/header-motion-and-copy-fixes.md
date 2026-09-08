# ヘッダー追加・背景を動かす・FV下の重複を外す・参加条件の文言

- **Started:** 2026-09-08
- **Completed:** 2026-09-08
- **Rule:** 2026-09-08 の依頼者の指示（5点）
- **Completed path:** `docs/exec-plans/completed/header-motion-and-copy-fixes.md`

## Goal

依頼の5点が `index.html` とセクションごとの Sass に入り、
**動きが実際に動いていること**と**止められること**を実測で確かめてある。

## Scope

- [x] ヘッダーを追加（`src/scss/sections/_header.scss`）
- [x] 背景の模様を動かす
- [x] FVすぐ下の開催情報を消す
- [x] 参加条件を「オレンジバンド着用者限定」に
- [ ] **チャイムの写真の差し替え —— 素材が無いので未実施。**下記参照

## Non-scope

- 店舗名・公式LINE URL・料金・入店時刻・年齢確認・キャンセル規定（支給待ち）
- og:image / og:url / noindex 解除（公開先未定）

## Constraints

- ヘッダーにリンクを置かない（`exit-routes-not-added`）。予約以外の出口を作らない。
- 動きは1つの物理法則に揃える（`lp-visual-knowledge` §6）。
- `prefers-reduced-motion: reduce` で全部止まること。

## Acceptance

- [x] ヘッダーが sticky で、店名だけ（リンクなし）
- [x] 背景の模様が**実際に動いている**（宣言だけでなく transform の変化を確認）
- [x] `prefers-reduced-motion` 相当の宣言でアニメーションが 0 本になる
- [x] FV下に開催情報が無く、`h1` が失われていない
- [x] 参加条件の文言が「オレンジバンド着用者限定」

## Verification

- [x] `node scripts/build.mjs`（Sassの非推奨警告なし）
- [x] `node scripts/harness/harness-check.mjs`
- [x] セクションごとの描画確認（`tools/render.sh`）
- [x] 実ブラウザ（http://localhost:3000）で走行本数・transform変化・fps・reduced-motion

## Result

| 検証 | 実際の出力 |
| --- | --- |
| `build` | 警告0で `Built css/style.css` |
| `harness-check` | 機械判定すべて pass、`manual` 27行 |
| 走行中のアニメーション | **55本** —— art-drift 6／art-flow 18／art-twinkle 19／art-spark 5／dot-drift 3／hero系 4 |
| 本当に動いているか | `.hero .art-layer` の transform が 1.2秒で変化（`matrix(1.01028,…,-4.39,2.28)` → `matrix(1.01097,…,-4.12,2.14)`） |
| reduced-motion | 同等の宣言を当てると **55本 → 0本** |
| フレーム | 2.0秒で121フレーム、**60.3fps・最悪フレーム 17.6ms** |
| 読み込み | 7件すべて200、コンソールエラーなし |

### 動きの決め方

**1つの物理法則 = ゆっくり漂う。**イージング（`ease-in-out`）と向き（`alternate`）を全部揃え、
**duration だけ全部違う値**にして位相をずらしています
（hero 19s / cta 18s / mechanism 21s / intro 23s / info 24s / benefits 26s）。
振幅は translate ±1.4%・scale 1.01〜1.035 まで。
**大きく動かすと「漂う」ではなく「移動する」になります**（リボンで学んだのと同じ）。

輪郭線は `stroke-dasharray: 120 1400` の**長い実線＋長い空白**にして
`stroke-dashoffset` を流しています。破線には見えず、線の上を光が1つ流れます。

### カンプ17から意図的に変えた2点

- **ヘッダーはカンプに無い。**依頼で足しました。店名だけでリンクは置いていません。
- **FVのロゴバッジを外しました。**ヘッダーに同じロゴが乗るので二重になります。1行で戻せます。

`img/asobibar-logo-light.svg` は**明色の版（暗い地用）**でした。実際に暗地・明地の両方で
描画して確認済み。**明るいセクションに置くと文字がほぼ消えます**（赤いRと多色のIだけ残る）。

### チャイムの写真を差し替えていない理由

**支給素材に「会話をして楽しんでいる様子」がありません。**
支給バナーは8人が全員カメラに向かってポーズした1枚で、実際に切って確かめました ——
別の場所を切っても会話の場面にはならず、しかも**焼き込み文字（取り下げ済みの言い回し）が
入ってしまいます。**偽らずに、`index.html` に理由付きの `TODO(依頼者確認)` を残しました。
**店内のスナップが1枚あれば差し替えます。**

### 検証していないこと、残っているリスク

- **60.3fps は Mac の数字。実機の中位Androidでは測っていません。**
  `art-flow` は18本の輪郭線の `stroke-dashoffset` を動かしており、
  **合成任せにできず毎フレーム再描画になります。**重いと分かったら最初に削る候補。
- **`prefers-reduced-motion` は「同等の宣言を当てると止まる」ところまで。**
  OS設定を実際に切り替えての確認はしていません。
- 実機のSP幅（375〜430px）での確認はしていません。確認は430px固定。
- ヘッダーが sticky なので、**FVの上端に常に被ります。**
  スクロール中に写真の一部が隠れることを、依頼者に見てもらう必要があります。
