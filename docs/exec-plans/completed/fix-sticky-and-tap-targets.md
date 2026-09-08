# sticky が効いていなかったのを直し、タップ領域を44pxにする

- **Started:** 2026-09-08
- **Completed:** 2026-09-08
- **Rule:** `docs/design-docs/lp-visual-knowledge.md` §10 の寸法確認（タップ領域44px）
- **Completed path:** `docs/exec-plans/completed/fix-sticky-and-tap-targets.md`

## Goal

実機に近い幅（375 / 390 / 430）で、ヘッダーが**実際に張り付き**、
押せる要素が**実際に44pxの当たり判定を持つ**。どちらも測って確かめてある。

## Scope

- [x] `.page` の `overflow: hidden` を外す（sticky が無効化されていた原因）
- [x] ヘッダーのロゴ・採用情報・店内状況、ダイアログの閉じるボタンの当たり判定を44pxへ
- [x] **見た目を変えない**（公式HPと同じ寸法を保つ）
- [x] 375 / 390 / 430 の3幅で横はみ出しとダイアログの収まりを測る
- [x] 支給された2枚目のチャイム写真を表示サイズのWebPにする

## Non-scope

- **物理端末での確認。**この環境に Xcode が無く（`/Library/Developer/CommandLineTools` のみ）
  iOSシミュレータが使えない。確認はブラウザの実寸エミュレーション。
- チャイム写真をどちらのテイクにするかの決定。**依頼者の判断待ち。**

## Constraints

- ヘッダーの見た目は公式HP（asobibar.net）と同じ寸法を保つ。
- 装飾のはみ出しは各セクションが自分で clip している前提を壊さない。

## Acceptance

- [x] 900pxスクロールしてもヘッダーの `top` が 0 のまま
- [x] 375 / 390 / 430 で `documentElement.scrollWidth === innerWidth`
- [x] ヘッダーの3リンクが、視覚中心から上下 ±16px の点で**実際に当たる**
- [x] ダイアログが縦に収まり、店舗行が44px以上

## Verification

- [x] `node scripts/build.mjs`
- [x] `node scripts/harness/harness-check.mjs`
- [x] 実ブラウザ（http://localhost:3000）で幅を変えて実測

## Result

| 検証 | 実際の出力 |
| --- | --- |
| sticky（修正前） | 900pxスクロールで `headerTop = -900`。**張り付いていなかった** |
| sticky（修正後） | `headerAfterScroll900 = 0` / `sticksCorrectly: true`（375・430の両方） |
| `.page` の overflow | `hidden` → `visible` |
| 横はみ出し | 375 / 390 / 430 すべて `scrollWidth === innerWidth`。**0** |
| タップ領域（修正前） | ロゴ 236×**20** / 採用情報・店内状況 56×**26** / 閉じる 36×36 |
| タップ領域（修正後） | ロゴの box が **44**。チップは見た目26pxのまま、**±16px の点で当たることを `elementFromPoint` で確認** |
| ダイアログ | 358×416（top 410 / bottom 826、844の中）。店舗行 320×**52**。縦に収まる |
| ページ全長 | 3255px（390幅） |
| チャイム写真02 | 1902x827 / 1947KB → **1000x435 / 35KB**。原本は `design/assets/MIXBAND-02.png` |

### 見た目を変えずに当たり判定だけ広げた方法

- ロゴ: `padding-block: 12px; margin-block: -12px`（背景が透明なので見た目は不変）
- チップ: `position: relative` + `::after { inset: -9px -6px }`
  （背景の大きさは26pxのまま、当たり判定だけ44pxへ）
- 閉じるボタン: `::after { inset: -4px; border-radius: 50% }`

### この作業で踏んだ間違い

**「宣言を読んで効いていると報告した」** ——
`getComputedStyle(el).position === 'sticky'` を見て効いていると書いたが、
祖先の `overflow: hidden` で無効化されていた。
**振る舞いは振る舞いで測る**（スクロールさせて `top` を見る）。
同じ形の間違いをタップ領域でもやりかけた（寸法を読むだけでは「押せる」は言えない。
`elementFromPoint` で当てる）。記録は
`docs/gotchas/sticky-was-declared-not-verified.md`。

**測定が古いCSSを見ていた。**`python3 -m http.server` は `Last-Modified` を返すので
ブラウザが304で古い方を使う。直したのに数値が変わらないときは、
まず自分の測定を疑う。

### 検証していないこと、残っているリスク

- **物理端末で見ていない**（Xcode不在でシミュレータも使えない）。
  LAN経由で `http://192.168.1.72:3000/` が届くことは確認済みなので、**実機はそこから見られる**。
- **sticky が効くようになったので、白いヘッダーがスクロール中ずっと画面上端に残る。**
  これが許容できるかは実機で見て判断してほしい。効いていなかった間は分からなかった点。
- **チャイム写真が2枚ある。**現在使っているのは01（私服・暖かい）。
  02（スーツ・反応が強い・4人全員のバンドが見える）は入れてあるが未使用。
