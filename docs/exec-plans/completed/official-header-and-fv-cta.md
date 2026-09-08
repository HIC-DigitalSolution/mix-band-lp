# ヘッダーを公式HPと同じにする・FVにCTA・チャイムにテロップ

- **Started:** 2026-09-08
- **Completed:** 2026-09-08
- **Rule:** 2026-09-08 の依頼者の指示（4点）
- **Completed path:** `docs/exec-plans/completed/official-header-and-fv-cta.md`

## Goal

ヘッダーが公式HP（asobibar.net）と同じ作りになり、ロゴと2ボタンから公式サイトへ遷移でき、
FVに「予約はこちら」があり、チャイムの写真にテロップが乗っている。

## Scope

- [x] **公式HPのヘッダーを実際に開いてDOMとCSSを読む**（推測しない）
- [x] ヘッダーを白地・sticky・ロゴ左・右に2ボタンへ差し替え
- [x] ロゴ → `asobibar.net`、採用情報 → `/recruit`、店内状況 → `/shops`
- [x] 白地用の暗色ロゴを作る
- [x] FVに「予約はこちら」（店舗選択ダイアログを開く）
- [x] チャイムの写真にテロップ「それはヤベェだろ」

## Non-scope

- チャイムの写真そのもの。**依頼者から撮影の方針をもらう段階。**
- 公式HPのモバイル下部固定バー（緑の「LINEのご予約はこちら」）。
  FVのCTAで代替している。

## Constraints

- **`exit-routes-not-added` を意図的に破る。**依頼者の指示なので、
  AGENTS.md に理由を書いて次の人が外さないようにする。
- テロップは**画像に焼き込まない。**文言を後から直せて、読み上げに乗るように。
- パロディの記号はジャンル一般のものだけ（`parody-stays-generic`）。
  テロップ帯は使ってよい記号。

## Acceptance

- [x] ヘッダーの色・寸法・揺れが実物のCSSと同じ値
- [x] 3つのリンクが `target="_blank" rel="noopener noreferrer"` で公式サイトへ
- [x] 白地で暗色ロゴが読める（明色版は消えることも確認）
- [x] FVのCTAが店舗選択ダイアログを開く
- [x] テロップが「4〜6 GROUPS CROSS」と重なっていない

## Verification

- [x] `node scripts/build.mjs`（非推奨警告なし）
- [x] `node scripts/harness/harness-check.mjs`
- [x] `tools/render.sh` で hero / mechanism を描画して目視
- [x] 実ブラウザ（http://localhost:3000）でリンク先・target・rel・CTAの動作

## Result

| 検証 | 実際の出力 |
| --- | --- |
| ヘッダー | `background: rgb(255,255,255)` / `position: sticky` / ロゴ `img/asobibar-logo-dark.svg` |
| リンク | `https://asobibar.net/`・`/recruit`・`/shops`、3つとも `target=_blank` `rel="noopener noreferrer"` |
| 採用情報の揺れ | `wiggler 2.5s`（公式と同じキーフレーム） |
| FVのCTA | クリックで `dialog.open === true` |
| テロップ | `それはヤベェだろ`。1回目は `4〜6` と重なったので位置を直した |
| `harness-check` | 機械判定すべて pass、`manual` 27行 |
| コンソール | エラーなし |

### 公式HPから取った値（推測ではない）

`asobibar.net` を実際に開いて、DOMと計算済みスタイルから取りました。

- ヘッダー: `bg-white` / `sticky top-0` / `padding 12px` / ロゴ高さ 20px / `href="/"`
- 採用情報: `#ffe207` + 黒文字 / 10px / 700 / padding 8px / 角丸 4px / shadow / `wiggler`
- 店内状況: `#AA8232` + 白文字 / 同じ寸法
- 予約: `#22C55E` + 白文字「LINEのご予約はこちら」。
  **PCはヘッダー下、モバイルは画面下の固定バー**（`fixed bottom-0 md:hidden`）
- 公式ロゴの文字色は `#070304`。他に `#d6006c` `#0092e5` `#ffda00` `#dc000c`

### 検証していないこと、残っているリスク

- **白いヘッダーが、暗いネオンのLPの上に乗ります。**
  公式HPと揃えた結果なので依頼どおりですが、**継ぎ目の見え方は実機で見てほしい。**
- **リンク先の実在は確認していません。**`/recruit` と `/shops` は公式HPのヘッダーから
  取ったパスで、開いて中身までは見ていない。
- FVのCTAと下のCTAで**文言が違います**（「予約はこちら」と「参加する店舗を選ぶ」）。
  行き先は同じダイアログ。揃えるかは依頼者の判断。
- **FVのCTAは下のCTAより一段小さくしています。**ページ最強面を下に残すため。
- テロップの文言は依頼者の指定。**番組名やロゴは使っていません**（`parody-stays-generic`）。
