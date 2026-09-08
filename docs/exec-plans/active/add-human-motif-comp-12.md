# 乾杯シルエットを加えるカンプ12

- **Started:** 2026-09-08
- **Rule:** `harness/scenarios/design-comp.yaml`, `harness/contracts/mix-lp.yaml`
- **Completed path:** `docs/exec-plans/completed/add-human-motif-comp-12.md`

## Goal

カンプ11の全面FVへ、幾何学背景だけでは伝わりにくい「交流が始まる温度」を補う人のモチーフを
追加する。乾杯する男女の上半身シルエットを1組だけSVGで配置し、既存の写真・タイトル・CTAの
可読性を保ったカンプ12として確認できる状態にする。

## Scope

- [x] カンプ11を複製し、カンプ12として編集する
- [x] 左右からグラスを寄せる男女の上半身シルエットをインラインSVGで追加する
- [x] 色、配置、静止の扱い、幾何学背景との役割分担をA3決定ボードへ記録する
- [x] `design/README.md`、`AGENTS.md`、LP固有ハーネスへ決定を追記する

## Non-scope

- 本番の `src/index.html`、`src/sections/`、Sass、JSへの実装
- 支給バナーの人物、ロゴ、焼き込みタイトルやコピーの編集
- 新しい写真素材やAI生成素材の追加
- シルエットを動かすアニメーション、音、イントロ画面の追加

## Constraints

- 比較06の濃紫・電気的な紫・ラズベリーピンクを主軸にし、オレンジはグラスと火花だけにする
- シルエットは写真と別レイヤーに置き、中央のタイトル・日付・CTAを覆わない
- 顔や衣装を描き込まず、男女1組の「乾杯」という記号へ抽象化する
- 既存の `prefers-reduced-motion` 方針を維持し、シルエット自体は静止させる

## Acceptance

- [x] カンプ12のFVに左右のシルエットと中央のグラス・火花が1組だけ見える
- [x] A3ボードと設計文書から、モチーフの意味・色・静止の理由を追跡できる
- [ ] 375pxのHTTPブラウザ表示で、タイトル・日付・CTAへの干渉と横スクロールがない

## Verification

- [x] `node scripts/harness/harness-check.mjs`（機械検証は全てpass。manual 24行は人の確認待ち）
- [x] HTMLParserでカンプ12を解析する
- [x] `git diff --check`
- [ ] 375px実寸のHTTPブラウザ表示（ローカルHTTPサーバーが実行上限で拒否されたため未確認）

## Result

カンプ11へ乾杯する男女のSVGシルエットを追加し、A3決定ボード、設計文書、README、AGENTS、ハーネスへ
意図を記録した。`harness-check.mjs` は「all machine-verified invariants passed」（manual 24行）を返し、
HTMLParserは289 start-tags / errorsなし、`git diff --check`も問題なしだった。`tools/render.sh` は環境の
QuickLook描画に失敗し、ローカルHTTPサーバー起動も実行上限による自動承認拒否で未確認である。実装へ
進む前にHTTP経路で、シルエットがタイトル・日付・CTAを覆わないことと横スクロールがないことを確認する。

この塊状シルエット案は依頼者の確認で不採用となり、人物のポーズ・頭の向き・腕の動きを読ませる
カンプ13へ置き換えた。カンプ12は比較用の記録として残し、現在の確認対象にはしない。
