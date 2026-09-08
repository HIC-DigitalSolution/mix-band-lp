# GitHub Pages が「building」のまま進まない

- **Date:** 2026-09-08
- **どこで:** `HIC-DigitalSolution/mix-band-lp` の初回 Pages ビルド

## 何が起きたか

Pages を `main` / ルートで有効にしたら、`status: building` のまま止まった。
`created_at` と `updated_at` が同じ時刻から動かず、ビルド履歴も1件だけ。
サイトは 404 を返し続けた。

## 原因（の第一候補）

**GitHub Pages の既定ビルダーは Jekyll を通す。**
このリポジトリには Jekyll が扱えないものが2種類ある ——

1. **外を指す symlink が15本。**`scripts/harness → ../../scripts/harness` など、
   共有元を参照している。**クローン先では切れたリンクになる。**
   Jekyll はサイトのソース外を指すシンボリックリンクを追わない。
2. **アンダースコア始まりのパス。**`src/scss/_tokens.scss` など。
   Jekyll は `_` 始まりを特別扱いする。

## 直し方

**リポジトリのルートに空の `.nojekyll` を置く。**
これで Pages は Jekyll を通さず、ファイルをそのまま配信する。

静的HTMLを Pages で出すなら、**最初から置いておくのが正しい。**
Jekyll を使っていないのに Jekyll を通す理由がない。

## 教訓

**「Pages を有効にした」と「配信されている」は別。**
`status` が `built` になり、実際に `curl` で 200 が返るまで確認する。
`building` のまま数分動かないときは、**待つのではなく原因を疑う。**
