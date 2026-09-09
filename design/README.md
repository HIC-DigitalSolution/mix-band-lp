# design/

**2026-09-09、依頼者の指示でカンプを全部削除しました。**残しているのは
**依頼者支給の原本だけ**です。ここはもうカンプの置き場ではなく、素材の置き場です。

| ファイル | 何か |
| --- | --- |
| `assets/MIX-BAND-PC-1920x1080.png` | PC用キーアートの支給原本（2026-09-09 支給）。本番は `img/mix-band-key-pc.webp`（q86・305KB） |
| `assets/MIX-BAND-750x627-uncropped.webp` | SP用キーアートの未クロップ版。上部の一句を落としたものが本番の `img/mix-band-key-fv-crop.webp` |
| `assets/MIXBAND-CHIME01.png` | 1902x827。ここから `img/mix-band-chime02.webp` と `img/night-0{1,2,3}.webp` を切り出した |
| `assets/MIXBAND-02.png` | 1902x827。タイトル焼き込みの無い別カット。**現在は未使用** |
| `assets/asobibar-logo-light.svg` | 明色ロゴの支給原本。本番のヘッダーは白地なので `img/asobibar-logo-dark.svg` を使う |

## 消したもの

`mix-lp-comp-01〜07.dc.html`（却下済み）、`mix-lp-content-design-comp-08〜17.dc.html`
と描画PNG、配色スタディ04〜07、ワイヤーフレーム08〜10、`references/`、
`assets/ribbon-sprite.svg` と `assets/ribbon-gen.py`、
`../img/mix-lp-content-design-reference.{pdf,webp}`。

**カンプにしか無かった知識は、消す前にハーネスへ移しました。**
`../harness/contracts/mix-lp.yaml` の —

- `banner-measurements-decide-the-cta` —— バナーの実測（赤〜橙78.8% / ピンク4.5%）と、
  CTAをオレンジにしない理由、ランプ01〜06の役割
- `japanese-headings-cap-at-24px-on-sp` —— 375px幅で26pxは折り返して崩れた
- `ribbon-vocabulary-if-it-ever-returns` —— 3回作り直して得た形の語彙（不採用）
- `content-funnel-order-and-what-was-dropped` —— 説得順と、落とした節の理由
- `comps-were-deleted-implementation-is-the-reference` —— いまの基準は本番コード

各カンプの決定そのものは `../docs/design-docs/content-design-comp-08〜17.md` に残っています。
**古い文書（`../AGENTS.md`、`../docs/design-docs/pre-code-design-blueprint.md`、
完了済みの exec-plan）はまだ削除済みファイルのパスを書いています。見に行かないでください。**

## いまの基準

**本番の `../index.html` と `../src/scss/` です。**画を見たいときは
`../tools/render.sh index.html <出力幅> <分割数> <ビューポート幅> <高さ> <オフセット>`
で描きます（`../docs/gotchas/qlmanage-renders-at-its-own-size.md`）。

画を変えるときは、canvas を作り直すのではなく、決定を `../docs/design-docs/` へ書き、
`../harness/contracts/mix-lp.yaml` の不変条件を更新してから本番を触ります。
