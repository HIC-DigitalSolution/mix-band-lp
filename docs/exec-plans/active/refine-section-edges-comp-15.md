# WHAT IS MIXとYOUR NIGHTの端装飾を整えるカンプ15

- **Started:** 2026-09-08
- **Rule:** `harness/scenarios/design-comp.yaml`, `harness/contracts/mix-lp.yaml`
- **Completed path:** `docs/exec-plans/completed/refine-section-edges-comp-15.md`

## Goal

カンプ14の「WHAT IS MIX」左下にある未整理な線と星を、土台・輪郭・アクセントの階層へ整える。
「YOUR NIGHT」横の斜めアウトライン文字を外し、見出しと右端の有機形の役割を明確にする。

## Scope

- [x] カンプ14を複製し、カンプ15として編集する
- [x] WHAT IS MIX左下を暗い有機形、平行な輪郭線、短いオレンジ線、小さな点へ再構成する
- [x] YOUR NIGHT横の斜め文字「FEEL THE NIGHT」を削除する
- [x] A3決定ボードと設計文書へ変更理由を記録する
- [x] `design/README.md` と `AGENTS.md` の現在の確認対象をカンプ15へ更新する

## Non-scope

- 本番の `src/index.html`、`src/sections/`、Sass、JSへの実装
- 人物モチーフの造形変更
- FV、配色、内容順、CTA動線の変更

## Constraints

- 比較06の配色と、オレンジを小面積に限定する役割を維持する
- 左下の形は本文へ入らず、画面外へ終端を逃がす
- YOUR NIGHTと日本語見出しより強い文字装飾を追加しない
- カンプ14は比較用として残し、上書きしない

## Acceptance

- [x] WHAT IS MIX左下が、単独の星と途切れた線ではなく3段階の装飾として記述されている
- [x] YOUR NIGHT横に「FEEL THE NIGHT」の斜め文字が存在しない
- [x] A3ボードと設計文書から変更理由を追跡できる
- [ ] 375pxのHTTPブラウザ表示で、左下の形が本文へ干渉せず横スクロールもない

## Verification

- [x] `node scripts/harness/harness-check.mjs`（all machine-verified invariants passed。manual 24行は人の確認待ち）
- [x] HTMLParserでカンプ15を解析する（304 start-tags / errorsなし）
- [x] `git diff --check`（問題なし）
- [ ] 375px実寸のHTTPブラウザ表示（環境上の制限により未確認）
- [x] `tools/render.sh design/mix-lp-content-design-comp-15.dc.html 1200` を実行（QuickLook描画に失敗。画像確認は未完了）

## Result

カンプ15へ2か所の端装飾調整を反映した。`harness-check.mjs` は all machine-verified invariants passed
（manual 24行）、HTMLParserは304 start-tags / errorsなし、`git diff --check`も問題なしだった。
QuickLook描画とHTTP経路の375px表示は未確認のため、左下の有機形の面積と境界付近の見え方には目視確認が残る。
