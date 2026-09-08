# 内容を反映したデザインカンプ

- **Started:** 2026-09-08
- **Rule:** `harness/scenarios/design-comp.yaml`、`harness/contracts/mix-lp.yaml`
- **Completed path:** `docs/exec-plans/completed/content-design-comp.md`

## Goal

確定した内容構成を、375px基準のデザインカンプへ落とす。支給バナー、必須訴求3点、
2026年10月の日程、オレンジバンド、公式LINEへ進む店舗選択ダイアログが1本の流れで見える。

## Scope

- [x] 本文6区間とFooterを1本のSPカンプへ配置する
- [x] 店舗選択ダイアログを開いた状態を別アートボードで示す
- [x] 決定と未支給データを仕様ボードに記録する

## Non-scope

- 本番HTML・Sass・JSへの実装
- 店舗名と各公式LINE URLの確定
- 料金、受付時間、実績、お客さまの声、FAQ

## Constraints

- CVは、店舗選択ダイアログを経由した店舗公式LINEへの遷移に絞る
- 対象は20〜30代の男女。流入は支給バナーを使うSNS広告・ポスターとして扱う
- 目標CVRは依頼者が未設定。初回公開後の公式LINE遷移率を基準値として取る
- リボンを使わず、SOUND TRIPから取った有機形の構成文法を使う
- CTAはネオンピンク。オレンジはチャイム面でブルーバイオレットの補色として使う

## Acceptance

- [x] SPページを上から読むと、対象→体験→価値→仕組み→開催情報→店舗選択の順になる
- [x] 支給バナーの焼き込み文字へHTML側の文字を重ねていない
- [x] 店舗一覧は本文ではなくダイアログ内だけにある
- [x] 375px相当で描画し、本文、輪郭、ゼブラ、CTA、ダイアログを目視できる

## Verification

- [x] `node scripts/harness/harness-check.mjs`
- [x] `tools/render.sh design/mix-lp-content-design-comp-08.dc.html 1600`
- [x] 生成PNGを開き、全体とダイアログ状態を目視する

## Result

`design/mix-lp-content-design-comp-08.dc.html` に375pxの本文カンプ、店舗選択ダイアログ、
決定ボードを作成し、`design/mix-lp-content-design-comp-08.png` に全体を描画した。
内容と採否の理由は `docs/design-docs/content-design-comp-08.md` に記録した。

`tools/render.sh` は `tmp/render/mix-lp-content-design-comp-08.dc.png` を生成し、
全ページPNGもブラウザ描画で確認した。HTML parserは `HTML parse: OK`、
`git diff --check` は出力なし、harnessは機械判定がすべてpassした。

22件のmanual項目も読み、単一CV、内容順、空枠を置かない判断、参考構成、配色、
支給バナー、描画確認をカンプと設計記録へ反映した。目標CVRは依頼者が未設定のため、
初回公開後の公式LINE遷移率を基準値にする。店舗名・各公式LINE URLと広告最終コピーは
未支給で、実装前の確認事項として残る。
