# 配色比較06を反映したデザインカンプ09

- **Started:** 2026-09-08
- **Rule:** `harness/scenarios/design-comp.yaml`、`harness/contracts/mix-lp.yaml`
- **Completed path:** `docs/exec-plans/completed/restyle-comp-09.md`

## Goal

内容カンプ08の構成を保ち、依頼者が最も良いと判断した配色比較06の色面積、
ネオンの線、ゼブラの置き方を反映したカンプ09を作る。

## Scope

- [x] 375px本文カンプを比較06の濃紫・ラズベリーピンク・淡いピンクへ組み直す
- [x] 比較06の重なるネオン円、点描、細いオレンジの光を反映する
- [x] 店舗選択ダイアログと決定ボードを新しい配色へ合わせる

## Non-scope

- 本番HTML・Sass・JSへの実装
- 内容構成と確定コピーの変更
- 店舗名と各公式LINE URLの確定

## Constraints

- 支給バナーはFVへ仮置きしたままにする
- リボンを使わない
- CTAはネオンピンクの最強面として残す
- オレンジは比較06と同じく、細線・点・小さな光だけにする

## Acceptance

- [x] 比較06と同じく濃紫・ラズベリーピンク・淡いピンクが主役に見える
- [x] ブルーバイオレットとオレンジが広い面で競合しない
- [x] 375pxで本文、装飾、CTA、ダイアログが重ならず読める

## Verification

- [x] `node scripts/harness/harness-check.mjs`
- [x] `tools/render.sh design/mix-lp-content-design-comp-09.dc.html 1600`
- [x] 全ページPNGを開き、比較06と並べて目視する

## Result

`design/mix-lp-content-design-comp-09.dc.html` と全ページ描画
`design/mix-lp-content-design-comp-09.png` を作成した。内容順とコピーはカンプ08を継承し、
比較06の濃紫、電気的な紫、ラズベリーピンク、淡いピンクの面積関係へ変更した。
判断は `docs/design-docs/content-design-comp-09.md` とハーネスへ記録した。

Quick LookとヘッドレスChromeの両方で描画し、375px本文、ネオン円、ゼブラ、CTA、
店舗選択ダイアログを目視した。HTML parserは成功し、`git diff --check` は出力なし、
harnessの機械判定はすべてpassした。

目標CVR、店舗名、各公式LINE URL、広告最終コピーは未確定のまま。公開後の
公式LINE遷移率を基準値にする方針と、実装前の確認事項は変更していない。
