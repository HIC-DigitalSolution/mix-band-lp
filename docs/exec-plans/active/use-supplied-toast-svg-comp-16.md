# 支給された乾杯SVGを採用するカンプ16

- **Started:** 2026-09-08
- **Rule:** `harness/scenarios/design-comp.yaml`, `harness/contracts/mix-lp.yaml`
- **Completed path:** `docs/exec-plans/completed/use-supplied-toast-svg-comp-16.md`

## Goal

依頼者が作成した `mix-toast-couple.svg` を、イベント理解セクションの人物モチーフとして採用する。
カンプ15のインライン仮SVGを置き換え、支給素材の形・色・乾杯の構図をそのまま確認できる状態にする。

## Scope

- [x] 支給SVGのviewBox、外部参照、スクリプト、文字の有無を確認する
- [x] `design/assets/mix-toast-couple.svg` へ素材を保存する
- [x] カンプ15を複製し、カンプ16でインラインSVGを支給SVGの`img`へ置き換える
- [x] A3決定ボード、設計文書、README、AGENTSへ採用理由を記録する

## Non-scope

- 本番の `src/index.html`、`src/sections/`、Sass、JSへの実装
- 支給SVGの形・色・構図の描き直し
- 新しい人物素材、写真、アニメーションの追加

## Constraints

- 素材は外部画像、JavaScript、文字、ロゴを含まない静的SVGであること
- 表示位置はイベント理解セクション右端とし、本文中央・日付・CTAを覆わないこと
- ページの比較06配色と、オレンジを乾杯の小面積へ限定する役割を維持すること
- カンプ14・15は比較用として残し、上書きしないこと

## Acceptance

- [x] `mix-toast-couple.svg` が `design/assets/` に存在し、カンプ16から参照されている
- [x] カンプ16にインライン仮SVGが残らず、人物モチーフが1組だけである
- [x] A3ボードと設計文書から、支給素材を再描画せず採用した理由を追跡できる
- [ ] 375pxのHTTPブラウザ表示で、人物の大きさ・重なり・横スクロールが問題ない

## Verification

- [x] `node scripts/harness/harness-check.mjs`（all machine-verified invariants passed。manual 24行は人の確認待ち）
- [x] `xmllint --noout design/assets/mix-toast-couple.svg`（問題なし）
- [x] HTMLParserでカンプ16を解析する（293 start-tags / errorsなし）
- [x] `git diff --check`（問題なし）
- [ ] 375px実寸のHTTPブラウザ表示（環境上の制限により未確認）

## Result

支給SVGを `design/assets/mix-toast-couple.svg` へ保存し、カンプ16の人物レイヤーを `img` 参照へ差し替えた。
`xmllint` は問題なし、HTMLParserは293 start-tags / errorsなし、`harness-check.mjs` は all machine-verified
invariants passed（manual 24行）、`git diff --check`も問題なしだった。QuickLookとHTTP経路の375px表示が
未確認のため、素材の表示サイズと本文への重なりには目視確認が残る。
