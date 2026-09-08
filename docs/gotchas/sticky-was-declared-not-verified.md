# position:sticky は「宣言」ではなく「張り付くか」を測る

- **Date:** 2026-09-08
- **どこで:** `.site-header`（`src/scss/sections/_header.scss`）と `.page`（`_base.scss`）

## 何が起きたか

ヘッダーに `position: sticky; top: 0` を書き、実ブラウザで確認して
「`headerSticky: "sticky"`」を得たので**効いていると報告した。**

**効いていなかった。**900pxスクロールしたらヘッダーも -900px へ流れていった。

原因は `.page` の `overflow: hidden`。
**祖先に `overflow: hidden`（または `auto` / `scroll`）があると、
sticky はその要素をスクロールコンテナとして扱う。**
`.page` は自分ではスクロールしないので、sticky は何にも張り付かず、
ただ一緒に流れる。

## なぜ気づかなかったか

**`getComputedStyle(el).position` を読んだだけだった。**
それは「宣言が生きているか」しか答えない。**張り付くかは別の話。**

正しい測り方 ——

```js
const before = el.getBoundingClientRect().top;   // 0
window.scrollTo(0, 900);
const after  = el.getBoundingClientRect().top;   // 効いていれば 0 のまま
```

## 同じ日に踏んだ、同じ形の間違い

**タップ領域も「値を読んで満たしていると思った」だけだった。**
`padding` と `margin` の負値、`::after` の `inset` で当たり判定を広げたが、
**広がったかは `elementFromPoint` で実際に当てないと分からない。**

```js
const el = document.elementFromPoint(cx, cy + 16);
target.contains(el) || el === target   // これで初めて「押せる」が言える
```

## もう1つ: ブラウザのキャッシュ

直したのに `boxH` が古い値のままだった。
`python3 -m http.server` は `Last-Modified` を返すので、**ブラウザが304で古いCSSを使う。**
測る前に読み直させる ——

```js
const l = link.cloneNode(); l.href = 'css/style.css?t=' + Date.now();
link.after(l); link.remove();
```

**「直したのに変わらない」ときは、まず自分の測定が古いものを見ていないか疑う。**

## 教訓

**振る舞いは、振る舞いで測る。**
プロパティの値・要素の寸法・宣言の存在は、どれも「効いている」の証明にならない。
`output-is-rendered-and-seen` は描画の話だが、**同じことが挙動にも当てはまる。**
