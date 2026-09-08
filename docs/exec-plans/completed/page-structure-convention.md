# ページの持ち方を規約にしてハーネスに入れる

- **Started:** 2026-09-08
- **Completed:** 2026-09-08
- **Rule:** 2026-09-08 の依頼者の指示 —— index.html に記述して、各セクションごとに
  Sass コンパイルで管理して、自分で見やすくできる形にしたい。画像は img/ に置く。
- **Completed path:** `docs/exec-plans/completed/page-structure-convention.md`

## Goal

**依頼者本人が `index.html` を開いて上から読める形**が規約として固定され、
崩したときに機械が落ちる。スタイルはセクションごとの Sass に分かれ、
本番の画像は `img/` からしか参照されない。

## Scope

- [x] `index.html` を手書きに戻す（`src/index.html` + `src/sections/*.html` の結合をやめる）
- [x] `scripts/build.mjs` を **Sass 専用**にする
- [x] `mix-lp.yaml` に機械6本・manual 2本を足す
- [x] `AGENTS.md`・`static-html.yaml` の古い記述を直す
- [x] **ハーネス監査で見つけた「偽の green」を直す**

## Non-scope

- デザインの中身。カンプは依頼者側で作成中。
- 監査で挙げた運用の判断（`design/` 24MB の扱い、active な exec-plan 5本、
  「1日限り」の契約衝突、本番画像の置き場の最終決定）。**どれも未処理のまま。**

## Constraints

- `index.html` と `css/style.css` は公開対象。**`index.html` は手書き、`css/` は生成物**という
  非対称を、契約とビルドの両方で同じに保つこと。
- 判断が要るものを機械検査に書かない。落ち続ける検査はいずれ `--no-verify` で外される。

## Acceptance

- [x] `index.html` に生成物の印（`Generated from` / `Do not edit directly`）が無い
- [x] `npm run build` が `css/style.css` だけを吐く
- [x] 新しい検査が**落ちるべきときに落ちる**ことを、実際に落として確かめた
- [x] 既存の検査を新規則が巻き添えで落としていない

## Verification

- [x] `node scripts/harness/harness-check.mjs`
- [x] `node scripts/build.mjs`
- [x] 新検査の陽性確認（`url()` で `design/` を参照させて FAIL させる → 戻して pass）

## Result

| 検証 | 実際の出力 |
| --- | --- |
| `node scripts/build.mjs` | `Built css/style.css`。`index.html` は触られない |
| `harness-check`（規則追加後） | 機械判定すべて pass、`manual` **26行**（21 → 26） |
| 陽性確認 | `src/scss/_tokens.scss` に `url("../design/assets/…")` を足す → `production-images-live-in-img` が FAIL。戻すと pass |
| 巻き添え | 無し。`head-basics` は書き換え後も pass（実タグが4つとも在る） |

### 足した不変条件

| id | 型 | 見ているもの |
| --- | --- | --- |
| `index-html-is-written-by-hand` | forbidden-content | `index.html` に生成物の印が無い |
| `styles-are-per-section-sass` | required-content | `style.scss` が `sections/` を `@use` している |
| `css-is-compiled-not-handwritten` | required-content | `css/*.css` に生成の見出し行が在る |
| `sass-change-ships-its-css` | companion-required | `src/scss/` を変えたら `css/*.css` も同じ差分に居る |
| `production-images-live-in-img` | forbidden-content | `url()` / `src=` / `href=` が `design/` を指さない |
| `image-files-live-in-img` | forbidden-path | 画像がルート・`src/`・`css/` に置かれない |
| `og-image-and-index-before-release` | manual | 公開前に og:image・og:url・noindex 解除 |
| `page-structure-is-readable-by-the-client` | manual | 規約の言葉の版と、その理由 |

### 直した「偽の green」

**`head-basics` が `og:image` を要求していたのに pass していた。**
`index.html` に `<meta property="og:image">` は1つも無く、通っていた理由は
`<!-- TODO(依頼者確認): … og:image / og:url の絶対URLを設定し… -->` という
**コメントに文字列が入っていたから**だった。素の文字列で `required_patterns` を書いた設計ミスで、
**契約自身が禁じている「何も検査していない green」**になっていた。

直し方: 判定を**タグの形**にした（`property="og:title"` / `<html lang=`）。
**公開時にだけ真になる og:image と og:url は manual に移した** ——
開発中ずっと落ち続ける機械検査は、いずれ `--no-verify` で外されるため。

### 途中で直したこと

**最初に書いた `production-images-live-in-img` は乱暴すぎた。**
`design/` という文字列を全面禁止にしたので、`src/scss/_tokens.scss` の
「最終決定は design/mix-lp-comp-07.dc.html」という**出どころのコメントで落ちた。**
→ 禁じるのを**参照の形だけ**（`url()` と `src=`/`href=`/`poster=`/`srcset=`/`content=`）に絞った。
**決定の出どころをコメントに書くのは正しい行為で、それを罰する検査は間違い。**

### 検証していないこと、残っているリスク

- **`.dc.html` のカンプは `\.html$` に一致する。**`static-html.yaml`（pre-push）が
  カンプ14枚をHTML構文チェックにかける。**まだ push していないので、実際に通るかは未確認。**
- **`index.html` が手書きになったので、閉じ忘れを見てくれるものが減った。**
  pre-push の構文チェックだけが頼り。
- `image-files-live-in-img` は **`.svg` も画像として扱う。**アイコンをコンポーネント的に
  `src/` へ置きたくなったら、この規則とぶつかる。
- **監査で挙げた残り4件は未処理**（`design/` 24MB、active な exec-plan 5本、
  「1日限り」の契約衝突、`img/mix-band-key.webp` と `design/assets/mix-band-key-fv-crop.webp` の
  どちらを本番にするか）。
