# WebPのアルファは CSS マスクとして効かない（要素ごと消える）

- **Date:** 2026-09-09
- **出どころ:** 導入セクションの試作で、ロゴの形に写真を抜こうとして踏んだ
- **関連:** `harness/contracts/mix-lp.yaml` の `output-is-rendered-and-seen`

`mask-image: url(logo.webp)` を指定すると、**computed値は正しく入るのに、
要素が完全に消える。**エラーも警告も出ない。

```
CSS.supports('mask-image','url(a.png)')  → true
getComputedStyle(el).maskImage           → url("http://.../mix-logo.webp")
getComputedStyle(el).maskSize            → 1253px
実際の描画                                → 真っ暗（何も出ない）
```

**PNG に差し替えたら直った。**マスク用は「白いシルエット＋元のアルファ」の
PNGを別に書き出す（色は使われないので、853x216 で 7KB に収まった）。

```python
from PIL import Image
im = Image.open('logo.png').convert('RGBA')
mask = Image.new('RGBA', im.size, (255,255,255,0))
mask.putalpha(im.getchannel('A'))
mask.save('img/logo-mask.png', optimize=True)
```

## 気づくのが遅れた理由

**computed値だけ見て「効いている」と判断した。**
`CSS.supports` が true で、`maskImage` にURLが入っていたので通ったと思い込み、
描画を確認しないまま組み上げた。真っ暗な画面を見て初めて気づいた。

`docs/gotchas/read-the-css-not-the-artwork.md` と同じ間違いで、
**「宣言が入っていること」と「描画されていること」は別**。

## 教訓

**マスク・フィルタ・ブレンドを入れたら、必ず一度スクリーンショットを撮る。**
これらは失敗しても例外を投げず、要素が静かに消えるだけ。
切り分けは「マスクを外して描画されるか」を見るのが速い。
