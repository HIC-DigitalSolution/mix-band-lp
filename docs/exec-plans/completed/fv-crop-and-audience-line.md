# FVの写真が切れていたのを直し、FV上の対象文を消す

- **Started:** 2026-09-08
- **Completed:** 2026-09-08
- **Rule:** 2026-09-08 の依頼者の指摘（FVの写真が切れているのが気になる／
  予約はこちらの上の20〜30代の文章を消す）
- **Completed path:** `docs/exec-plans/completed/fv-crop-and-audience-line.md`

## Goal

FVの支給バナーが**1pxも切れずに全部映る**。FVの「20〜30代の男女へ」が無くなっている。

## Scope

- [x] 何が切っているのかを数字で特定する
- [x] 切っている原因を外す
- [x] 動きは残す（切らない方法へ置き換える）
- [x] 「20〜30代の男女へ」を削除

## Non-scope

- 素材ファイル側のトリミング。**支給バナーの上部を切る判断は
  `mix-band-key-fv-crop.webp` の中で既に済んでいる**（カンプ11の決定）。そこは触らない。
- FVの構成（全面ビジュアル・ヘッダーのロゴ・端の光線）。

## Constraints

- カンプ11の「横幅いっぱいのFV」「控えめなループ」を保つ。
- `prefers-reduced-motion` で止まること。

## Acceptance

- [x] 画像の実比と表示枠の比が一致し、`transform` が掛かっていない
- [x] FVに対象を示す文が無い
- [x] 動きが残っている

## Verification

- [x] `node scripts/build.mjs`
- [x] `node scripts/harness/harness-check.mjs`
- [x] `tools/render.sh` で目視
- [x] 実ブラウザで実比・枠比・transform・走行アニメーションを実測

## Result

| 検証 | 実際の出力 |
| --- | --- |
| 切れの原因 | **`cover` ではなく `scale(1.07)`→`1.11` のズーム。**素材(750x583)と枠(750/583)の比は完全一致で、`cover` では1pxも切れない |
| 切れ方 | `transform-origin: 50% 72%` だったため**最大9.9%が上側に偏って**枠外へ出ていた |
| 直し方 | ズームを削除。動きは**参考にした Paradox Live と同じ「明るさの呼吸」**（`brightness .94→1.06` / `saturate 1→1.06`）に置き換え。**拡大しないので何も切れない** |
| 実ブラウザ | `naturalRatio 1.2864` = `boxRatio 1.2864`（一致）／`transform: none`／`objectFit: cover`／走行中 `hero-breathe` |
| 対象文 | `.hero__audience` が DOM から消えていることを確認 |
| コンソール | エラーなし |

### なぜズームが「意図しない切れ」だったか

**支給バナーの上部を切る判断は、素材ファイル側で済んでいた**
（`mix-band-key-fv-crop.webp` = カンプ11の「上部44pxを決定的にカット」）。
その上からさらに `scale(1.07)` を掛けていたので、
**同じ判断が二重に効いて、意図していない分まで落ちていた。**

### 検証していないこと、残っているリスク

- **`brightness` の呼吸は写真全体の明るさを動かす。**暗い環境では
  「光っている」より「明滅している」に見えるかもしれない。実機で見て判断してほしい。
- FVから対象の明示が無くなったので、**「誰向けか」を画面で示すものは支給バナーの
  焼き込みだけ**になった。`matches-the-ad-that-brought-them`（manual）に関わるので、
  広告のコピーと突き合わせるときにここを見ること。
