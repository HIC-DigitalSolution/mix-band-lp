# 内容デザインカンプ16の決定

- **Date:** 2026-09-08
- **Status:** 依頼者支給の乾杯SVGを採用。375pxのHTTP表示確認待ち
- **Comp:** `design/mix-lp-content-design-comp-16.dc.html`
- **Asset:** `design/assets/mix-toast-couple.svg`
- **Previous candidate:** `design/mix-lp-content-design-comp-15.dc.html`

## 採用理由

依頼者が作成した `mix-toast-couple.svg` を人物モチーフとして採用する。素材は2人の全身シルエット、中央の
グラス、波線、オレンジの乾杯マークを1枚にまとめており、カンプ14・15の仮SVGよりも、乾杯する瞬間と人物同士の
向きが読みやすい。形・色・重なりは支給素材を正とし、ページ側で再描画しない。

素材の `viewBox` は `0 0 180 220`、表示サイズは `120×147px` とする。イベント理解セクションの右端に置き、
大きな有機形の一部として扱う。SVG自体は透明背景で、本文中央、焼き込みタイトル、日付、CTAを覆わない。

## 素材の確認

支給ファイルは外部画像、JavaScript、`foreignObject`、テキスト、ロゴを含まない。人物は濃紫・電気的な紫・
淡いピンク、乾杯部分はオレンジで、比較06の役割と一致する。オレンジは素材内でもグラスと小さなマークに
限定されている。外部参照や動きは追加しない。

## 変更しないこと

カンプ15で整えたWHAT IS MIX左下の有機形・輪郭線・点、YOUR NIGHT横の斜め文字を削除した状態、比較06の配色、
全面FV、左上ロゴ、6区間の内容順、店舗選択ダイアログ、CTAの役割は維持する。本番HTML・Sass・JSには反映しない。

## 確認状況

カンプ16でインライン仮SVGを削除し、`assets/mix-toast-couple.svg` を `img` として参照した。`xmllint` は問題なし、
HTMLParserは293 start-tags / errorsなし、`harness-check.mjs` は all machine-verified invariants passed
（manual 24行）、`git diff --check` も問題なしだった。ローカルファイルを開いているブラウザタブはコンピューター
操作のURLポリシーで取得できず、`tools/render.sh` もQuickLook描画に失敗するため、375pxの実画面確認は未完了である。
実装へ進む前に、人物の表示サイズ、右端のクリップ、本文との重なり、横スクロールの有無をHTTP経路で確認する。
