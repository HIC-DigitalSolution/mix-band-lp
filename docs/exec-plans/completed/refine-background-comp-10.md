# SOUND TRIPを基準に背景を磨くカンプ10

- **Started:** 2026-09-08
- **Rule:** `harness/scenarios/design-comp.yaml`、`harness/contracts/mix-lp.yaml`
- **Completed path:** `docs/exec-plans/completed/refine-background-comp-10.md`

## Goal

内容カンプ09の配色と情報構成を保ち、SOUND TRIPで再確認した背景レイヤーの作り方を
取り入れて、各セクション固有の背景を持つカンプ10へ更新する。

## Scope

- [x] SOUND TRIPの実画面、背景SVG、疑似要素の寸法を再確認する
- [x] 375px本文の各セクションへ専用SVG背景と輪郭線を追加する
- [x] 大きなアウトライン文字、点描、火花、ゼブラの密度を整理する
- [x] 店舗選択ダイアログと決定ボードへ背景ルールを反映する

## Non-scope

- 本番HTML・Sass・JSへの実装
- SOUND TRIPの色、ロゴ、人物、SVG輪郭の流用
- 内容構成、確定コピー、CTA動線の変更

## Constraints

- 配色比較06の濃紫・電気的な紫・ラズベリーピンク・淡いピンクを維持する
- リボンを使わない
- 装飾を左右端・四隅・境界へ寄せ、本文の背面を空ける
- 1セクション1SVGを基本にし、背景の形を使い回さない

## Acceptance

- [x] 各セクションの背景が同じ丸形の反復に見えない
- [x] 大きな形・中間の輪郭線・小さな記号の3段階が見える
- [x] 375pxで背景が本文、支給バナー、CTAへ干渉しない
- [x] カンプ09より背景に奥行きがあり、比較06の配色は崩れていない

## Verification

- [x] `node scripts/harness/harness-check.mjs`
- [x] `tools/render.sh design/mix-lp-content-design-comp-10.dc.html 1600`
- [x] 全ページPNGを開き、カンプ09とSOUND TRIPの背景階層を見比べる

## Result

SOUND TRIPの実画面、`abount_002_sp.svg`、`how_to_001.svg` と疑似要素の寸法を
再確認し、背景の差を「大きな色面・中間の輪郭またはパターン・小さな記号」の3段階として
整理した。カンプ10では6区間に異なる専用SVGとアウトライン文字を追加し、MIXのゼブラ、
ネオン線、火花へ置き換えた。内容順、比較06の配色、支給バナー、CTA動線は変更していない。

`tools/render.sh` は `tmp/render/mix-lp-content-design-comp-10.dc.png` を生成した。
ヘッドレスChromeでも1420px幅の全ページPNGを生成し、ブラウザでは375pxの本文列を
上・中・下に分けて確認した。カンプ09との比較で背景の奥行きが増し、本文とCTAへ干渉しない
ことを目視した。HTMLParser、`git diff --check`、ハーネスの機械判定はすべて通過した。
ハーネスのmanual 22件も読み、今回の差分が確定コピー、単一CV、配色、参照サイトの流用範囲を
変えていないことを確認した。

本番HTML・Sass・JSには未実装で、動き、PC外周、実際の店舗数を入れたダイアログは未検証である。
目標CVRと広告の最終コピーも未支給のため、実装前の確認事項として残る。
