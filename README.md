# ミックス交流上等バンド LP

**ページの入口はルートの `index.html`。編集するファイルは `src/` にまとめています。**
現在は確定済みの情報だけを置いた実装用の土台です。デザインは依頼者側で作成中です。

見た目を実装する前に `harness/scenarios/design-comp.yaml` の順番で確認します。
参考にするのは、KBC創立70周年サイトから取ったリボンの形・浮遊の物理と、
FUTURE TRAINから取った1本の色ランプによる遷移です。数値と採用範囲は
`docs/design-docs/reference-sites.md`、最新の配色決定は同資料の§3と
却下済みカンプに残していましたが、2026-09-09 にカンプごと削除しました。理由は `harness/contracts/mix-lp.yaml` の `rejected-directions-not-reproposed` にあります。

## ファイル構成

```text
index.html                 生成されたページ
css/style.css              Sassから生成されたCSS
img/                       支給画像
src/
  index.html               head・ページ全体・セクションの順番
  sections/
    hero.html              ファーストビュー
    about.html             イベントの仕組み
    schedule.html          開催日
    footer.html             フッター
  scss/
    style.scss             SCSSの読み込み入口
    _tokens.scss           共通変数
    _base.scss             共通スタイル
    sections/              セクションごとのSCSS
scripts/build.mjs          HTML結合・Sassコンパイル・変更監視
design/                    依頼者支給の素材原本（カンプは2026-09-09に削除）
docs/                      判断の記録
harness/・tools/            既存の検証ツール
```

## 開発

Node.js 20以上とPython 3を使用します。

```sh
npm ci
npm run build
npm run serve
```

ブラウザで http://localhost:8770/ を開きます。
編集しながら反映する場合は、別ターミナルで `npm run watch` を起動してください。
HTML・SCSSの保存で再生成されます。ブラウザは手動で再読み込みしてください。

## セクションの追加・並べ替え

1. `src/sections/` に `faq.html` などを作成します。
2. `src/index.html` の表示したい位置に `<!-- include: faq -->` を追加します。
3. `src/scss/sections/_faq.scss` を作り、`src/scss/style.scss` に `@use 'sections/faq';` を追加します。
4. `npm run build` を実行します。

HTMLはビルド時に結合されるため、表示時のJavaScriptやfetchは不要です。
`index.html` と `css/style.css` は生成物としてソースと一緒に管理します。直接の修正は次のビルドで上書きされます。
公開には生成したHTML・CSSと参照画像を使います。

## 確認

```sh
npm run check
```

ハーネスの `[manual]` は別途人が確認する項目です。共有ハーネスのシンボリックリンクの前提は `AGENTS.md` を参照してください。
未確定項目はHTMLコメントに `TODO(依頼者確認)` として残しています。公開先・OG画像の絶対URL・CTA・デザインを確定してから公開します。現在は `noindex` を設定しています。
