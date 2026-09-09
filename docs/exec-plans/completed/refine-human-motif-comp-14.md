# SOUND TRIPのスケールへ人物モチーフを戻すカンプ14

- **Started:** 2026-09-08
- **Rule:** `harness/scenarios/design-comp.yaml`, `harness/contracts/mix-lp.yaml`
- **Completed path:** `docs/exec-plans/completed/refine-human-motif-comp-14.md`

## Goal

カンプ13の大きな上半身ポーズを取り下げ、SOUND TRIPで確認した「大きな有機形の端に小さな人物・記号をまとめる」
スケールへ人物モチーフを組み直す。人の気配と乾杯の意味を残しながら、本文とキーアートの主役を奪わない状態にする。

## Scope

- [x] カンプ13を複製し、カンプ14として編集する
- [x] `.intro` の有機形の端へ小さな人物記号を1組だけ追加する
- [x] 頭・髪・短い腕・中央のグラス・波線・火花へ要素を絞り、A3決定ボードへ意図を記録する
- [x] 設計文書、README、AGENTS、ハーネスの人物モチーフ説明をカンプ14へ更新する

## Non-scope

- 本番の `src/index.html`、`src/sections/`、Sass、JSへの実装
- SOUND TRIPの人物イラスト、ロゴ、色、SVG輪郭のコピー
- 新しい写真素材やAI生成素材の追加
- 人物記号を動かすアニメーション、音、イントロ画面の追加

## Constraints

- 比較06の濃紫・電気的な紫・ラズベリーピンクを主軸にし、オレンジはグラスと火花だけにする
- 人物記号は小さな装飾レイヤーとし、本文中央、焼き込みタイトル、日付、CTAを覆わない
- 顔・衣装・指などの描写を増やさず、人物1組と波線・乾杯の記号に留める
- `prefers-reduced-motion` 方針を維持し、人物記号自体は静止させる

## Acceptance

- [x] カンプ14のイベント理解セクション右端に小さな人物記号と中央のグラス・火花が1組だけ見える
- [x] A3ボードと設計文書から、SOUND TRIPのスケールを借りた理由と配置を追跡できる
- [ ] 375pxのHTTPブラウザ表示で、人物記号が本文・日付・CTAへ干渉せず横スクロールもない

## Verification

- [x] `node scripts/harness/harness-check.mjs`（all machine-verified invariants passed。manual 24行は人の確認待ち）
- [x] HTMLParserでカンプ14を解析する（296 start-tags / errorsなし）
- [x] `git diff --check`（問題なし）
- **未実施:** 375px実寸のHTTPブラウザ表示（環境の自動承認上限により未確認）
- [x] `tools/render.sh design/mix-lp-content-design-comp-14.dc.html 1200` を実行（QuickLook描画に失敗。画像確認は未完了）

> **2026-09-09 追記。**上の未実施項目は、当時ローカルHTTPサーバーが動かせず
> 実行できなかったものです。**いまも「実行した」ことにはしません。**
> 対象だったカンプ本体は同日削除済みで、この形での確認はもう行えません。
> 実画面での確認は本番の index.html に対して行い、結果は
> `docs/exec-plans/completed/lp-adjust-p1-p6.md` に記録しています。

## Result

カンプ14へ小さな人物記号、波線、中央の乾杯を反映し、カンプ13の大きなポーズを置き換えた。機械検証とHTMLParser、
差分チェックの結果は作業後に追記する。HTTP経路の375px表示は未確認のため、人物の端のはみ出しが横スクロールや
本文との重なりを作るリスクが残る。
