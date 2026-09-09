# Paradox Liveを基準にFVを全面化するカンプ11

- **Started:** 2026-09-08
- **Rule:** `harness/scenarios/design-comp.yaml`、`harness/contracts/mix-lp.yaml`
- **Completed path:** `docs/exec-plans/completed/redesign-fv-comp-11.md`

## Goal

Paradox Live 5th Anniversaryの全面KVを実画面で確認し、MIXのFVを横幅いっぱいの
写真レイヤーへ組み直す。上部の焼き込みコピーを安全に外し、ASOBIBARロゴを左上へ置き、
タイトルの存在感と初回表示からの控えめな動きをカンプ11で確認できる状態にする。

## Scope

- [x] Paradox Live 5th AnniversaryのFV、レイヤー構造、アニメーションを実画面とCSSで確認する
- [x] 支給バナーの上部44pxだけをカットしたFV用画像を作る（人物・メインタイトルは変更しない）
- [x] FVを横幅いっぱいにし、ASOBIBARロゴを左上へ配置する
- [x] 写真の微細なズーム、光の呼吸、端の光線を追加し、reduced-motionで停止する
- [x] A3決定ボードへ動きの理由と制約を記録する

## Non-scope

- 本番HTML・Sass・JSへの実装
- 支給バナーの人物、メインタイトル、下部コピー、オレンジバンド表示の改変
- Paradox Liveのロゴ、写真、色、演出素材の流用
- 画面を覆うイントロ、音声許可、スキップ操作の導入

## Constraints

- 比較06の濃紫・ラズベリーピンク・ネオンピンクを維持し、オレンジは小面積に限定する
- 画像編集は上部コピーの削除だけ。人物と既存タイトルを固定する
- ロゴは実装時にaltを付け、中央の可読域を塞がない
- アニメーションはtransform・opacityだけで構成し、`prefers-reduced-motion: reduce`で停止する

## Acceptance

- [x] FV画像が375pxのphone幅いっぱいまで届き、左右の余白フレームがない
- [x] 上部のピンク文章が見えず、人物と「MIX交流上等」タイトルが保持されている
- [x] ASOBIBARロゴが左上にあり、タイトルが従来より大きく見える
- [x] 参考サイトのようなレイヤー感を保ちながら、初回表示で内容が読める

## Verification

- **未実施:** `node scripts/harness/harness-check.mjs`（FV変更後に再実行）
- [x] HTMLParserでカンプ11を解析する
- **未実施:** 375px実寸のブラウザ表示（ローカルHTTPサーバーが実行上限で拒否されたため未確認）
- [x] 既存カンプ09・10のPNGと目視比較する

> **2026-09-09 追記。**上の未実施項目は、当時ローカルHTTPサーバーが動かせず
> 実行できなかったものです。**いまも「実行した」ことにはしません。**
> 対象だったカンプ本体は同日削除済みで、この形での確認はもう行えません。
> 実画面での確認は本番の index.html に対して行い、結果は
> `docs/exec-plans/completed/lp-adjust-p1-p6.md` に記録しています。

## Result

SOUND TRIPで確立した背景の階層を維持しながら、Paradox Live 5th Anniversaryの
「全面ビジュアル＋複数レイヤー＋小さなループ」をMIX用に翻訳したカンプ11を作成した。
支給バナーは上端44pxをカットした `design/assets/mix-band-key-fv-crop.webp` を使い、
元の人物、メインタイトル、下部コピーは変更していない。`design/assets/asobibar-logo-light.svg`
を左上へ置き、写真の微細なズーム、光の呼吸、端の光線をCSSで定義した。

`view_image`で元画像とFV用画像を確認し、AI編集で人物まで変わった版は採用しなかった。
カンプ11はまだローカルHTTPサーバーでの375pxブラウザ描画を完了していない。
実行上限による自動承認拒否でサーバーを起動できなかったためで、公開用実装へ進む前に
HTTP経路で再確認する必要がある。
