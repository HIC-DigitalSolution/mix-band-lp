# 導入セクションを予告編のカット割りにする

- **Started:** 2026-09-09
- **Rule:** `harness/contracts/mix-lp.yaml` の `reference-motion-is-watched-not-inferred`
- **Completed path:** `docs/exec-plans/completed/intro-trailer-cuts.md`

## Goal

依頼者が指定した mememe-official.jp の動きに、写真素材でできる形で近づける。

## Constraints

- **GSAPを入れない**（JS無しで何が壊れるか言えないものは足さない）
- index.html は手書き、CSS は Sass のコンパイル物のみ
- 中央配置・改行位置・可読性は目視で決めず実測する
- push / デプロイは依頼者の指示があるときだけ

## Scope

- [x] スクロール連動のハードカット4枚
- [x] テロップを角から入れる
- [x] 最後を題字（ロゴ）で締める
- [x] 文字の上下中央を直す
- [x] 日本語の改行を文の単位にする

## Non-scope

- mememe と同じ 3D/WebGL 表現（素材制作が別規模）
- FVバナーの「1日限り」（焼き込み）

## Acceptance

- [x] カットがフェードせず切り替わる
- [x] JSが無くても1枚目と全文が出る
- [x] テロップの上下余白が対称（差1px以内）
- [x] 375/390 で文が行の途中から始まらない

## Verification

- [x] `node scripts/harness/harness-check.mjs`
- [x] `node scripts/build.mjs`
- [x] 時間差スクリーンショット4枚で実際の動きを確認
- [x] 行の切れ目を Range で走査して実測
- [x] `is-cuts` を外してJS無しの状態を再現

## Result

**方向を2回やり直した。**1回目（1行ずつフェード）は、参考サイトの動きを見ずに
computed値だけで「単純なフェード」と断定したのが原因。2回目（ロゴ型のマスクが広がる）は
ロゴの色と立体感を殺し、動きが3つの別々の操作に分かれていて弱かった。
**依頼者の選択で「予告編のカット割り」に決めて3回目で通った。**

**動き** —— スクロールに連動して4カットがハードカットで切り替わる。カットの中では
写真が `scale 1.04 → 1.11` でじわっと寄る（これが無いとカット間が静止画になり紙芝居に見える）。
テロップは `0.18s` で角から入る。フェードは一切使わない。

**踏んだ罠** —— `mask-image` に WebP を渡すと computed値は入るのに要素ごと消える
（docs/gotchas/webp-alpha-does-not-work-as-a-css-mask.md）。マスク案は捨てたが記録は残した。

**中央配置** —— テロップを `justify-items: center`（横だけ）で重ねていたため、縦は stretch で
箱が伸び、文字が上に張り付いていた（上13px / 下41px）。`place-items: center` で 上13 / 下13。
依頼者から2度目の指摘だったので `boxes-center-on-both-axes` として不変条件にした。

**改行** —— PC用 `<br>` を SP で消す作りにしていたため、SPで文が行の途中から始まり
鉤括弧が割れていた。支給コピーの1行を `<span class="u">` の inline-block にして、
幅に関係なく文の単位で折れるようにした。375pxで列が足りなかったので
`--sp-edge` の最小を 24px → 16px にした（列 285 → 301px）。全12行が単位どおり。

**ページの伸び** —— 貼り付き区間のぶん PC 5,868 → 8,025px、SP 4,080 → 6,280px。
カットを3つに減らせば約450px短縮できる。

**残っているもの** —— FVバナーの「1日限り」、背景SVGの歪み、店舗名と公式LINE URL。
