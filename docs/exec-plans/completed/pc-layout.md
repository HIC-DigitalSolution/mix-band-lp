# PC幅（LPサイズ）のレイアウトを作る

- **Started:** 2026-09-09
- **Completed:** 2026-09-09
- **Rule:** 2026-09-09 の依頼者の指示
  （futuretrain と構造を揃える／まずLPサイズ、その後SPサイズ）
- **Completed path:** `docs/exec-plans/completed/pc-layout.md`

## Goal

PC幅で futuretrain と同じ文法の組みになっている。**節は増やしていない。**
SPの見た目は変わっていない。

## Scope

- [x] futuretrain の全体構成を**実物で**読み、MIXの6区間と突き合わせる
- [x] PC側の数値（コンテナ・字寸・並べ方）を1440幅で実測
- [x] `min-width: 900px` のレイアウトを各セクションのパーシャルに足す
- [x] SPが変わっていないことを確かめる
- [x] §10 からの逸脱を記録する

## Non-scope

- **節の追加**（What's New / Station Map / Space / Access / Credit / FAQ）。
  依頼者が「見た目の文法だけ揃える（節は増やさない）」を選択。
- SPの作り直し。**この後の工程。**

## Constraints

- **`lp-visual-knowledge` §10 から意図的に外れる。**理由を記録に残すこと。
- 支給バナー（750x583）を原寸より拡大しない。
- メディアクエリはセクションのパーシャルに書く（1対1の規約を崩さない）。

## Acceptance

- [x] PC幅でコンテナ1280px、横はみ出しなし
- [x] SP幅で見た目が変わっていない
- [x] 重なるカードの sticky が両方の幅で効く
- [x] キーアートが原寸を超えていない

## Verification

- [x] `node scripts/build.mjs`
- [x] `node scripts/harness/harness-check.mjs`
- [x] 実ブラウザ 375 と 1440 で実測
- [x] `tools/render.sh` で hero / benefits / mechanism を目視

## Result

| 検証 | 実際の出力 |
| --- | --- |
| `node scripts/build.mjs` | `Built css/style.css`（非推奨警告なし） |
| `node scripts/harness/harness-check.mjs` | 機械判定すべて pass |
| 実ブラウザ 375 | `pageW 375` / `overflow false` / sticky `top 12` 保持 / kicker 10px |
| 実ブラウザ 1440 | `pageW 1280` / `overflow false` / sticky `top 96` 保持 / kicker 58px / body 18px / keyart 720px |
| `tools/render.sh` | hero・benefits・mechanism を1300幅で描画し、横並びと字寸を目視 |
| コンソール | 両幅ともエラーなし |

### futuretrain から実測した値（1440幅）

| | |
| --- | --- |
| コンテナ | **1280px**（出現86回。次いで1440フルブリード、1224が内側） |
| 英字の節見出し | **96px**（`almaq-refined`） |
| 和文見出し | 32px（`nitalago-ruika`・傾きあり） |
| 本文 | **18px / 行間34.2px（1.9）/ 字間0.9px** |
| 2カラムのブロック | **69個** —— 横並びが基本 |
| 全体構成 | FV → コンセプト → What's New → Station Map → **Visitor Guide（重なるカード5枚）** → Space → Access → Credit → FAQ → Reservation |

**背骨はMIXと既に一致していた。**違うのはこちらが意図的に落とした節だけ
（実績・声・料金・受付時間・FAQ・店舗一覧・ギャラリー）。

### 実測（実ブラウザ）

| | SP 375 | PC 1440 |
| --- | --- | --- |
| ページ幅 | 375 | **1280** |
| 横はみ出し | なし（`scrollWidth === innerWidth`） | なし |
| 重なるカードの sticky | 効く（top 12 で保持） | 効く（top 96 で保持） |
| 英字ラベル | 10px | **58px** |
| 本文 | 13px | **18px** |
| キーアートの表示幅 | — | **720px**（原寸750を超えていない） |
| コンソール | エラーなし | エラーなし |

`node scripts/build.mjs` は警告なしで `Built css/style.css`。
`harness-check` は機械判定すべて pass。

### §10 から意図的に外れている

`lp-visual-knowledge` §10 は「PCで横に広げない。カラムはSP幅のまま、
余った幅は外周の装飾にする」と言っている。**依頼者の指示で外れた。**
共有元の知識ドキュメントは編集していない（symlink）。代わりに
`AGENTS.md` と `pc-layout-exists`（機械）／`pc-grammar-comes-from-futuretrain`（manual）に
理由付きで記録した。**戻されないため。**

### 検証していないこと、残っているリスク

- **900〜1280px の中間幅は見ていない。**タブレット横やノートPCの狭い幅で
  2カラムが窮屈になる可能性がある。
- **PCでカードの本文側に余白が出る。**写真が高さを作るので、
  文字が縦中央に浮く。futuretrain のカードは中身が多いので目立たない。
- **SPサイズの作り直しは未着手**（依頼の後半）。いまのSPは既存のまま動いている。
- 実機で見ていない。確認はブラウザのエミュレーションと qlmanage。
