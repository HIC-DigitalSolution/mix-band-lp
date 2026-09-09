# 背景SVGを preserveAspectRatio="none" で敷くと、節ごとに柄の太さが変わる

- **Date:** 2026-09-09
- **出どころ:** 依頼者「いつもと違う夜に物語をの背景なんか雑ですね」「全体的に背景の模様の太さが汚いです」
- **関連:** `harness/contracts/mix-lp.yaml` の `sound-trip-composition-frames-the-page`

各セクションの背景は `<svg class="art-layer" viewBox="0 0 375 <節の高さ>"
preserveAspectRatio="none">` で敷いている。**`none` は縦横を別々に引き伸ばす。**
節の実寸は viewBox の想定と一致しないので、**節ごとに違う比率で歪む。**

1440px幅で実測した歪み（縦倍率 ÷ 横倍率）——

| 節 | 歪み |
| --- | --- |
| hero | 0.64 |
| intro | 0.56 |
| **benefits** | **2.45** |
| mechanism | 0.95 |
| info | 0.83 |
| cta | 0.94 |

## なぜ「太さが汚い」に見えるのか

**同じ柄が節ごとに別の太さで出る。**0.56の節では縞が細く詰まり、2.45の節では
縞が縦へ引き伸ばされて塗りつぶしの帯になる。円は楕円になる。

`vector-effect: non-scaling-stroke` を持つ**輪郭線だけは1pxに保たれる**ので、
「線は綺麗なのに柄が汚い」という見え方になり、原因が柄そのものに見えてしまう。

## benefits が特にひどい理由

2026-09-09にカードを1枚＝画面高にして、節が 690単位 → 実寸1,807px になった。
**絵は伸ばす前提で描かれていない。**

## 教訓

**節の高さが変わったら、背景の歪みも変わる。**レイアウトを変えたら
`縦倍率 ÷ 横倍率` を測ること。1に近いかどうかだけ見ればよい。

```js
[...document.querySelectorAll('.art-layer')].map(sv=>{
  const r=sv.getBoundingClientRect(), vb=sv.getAttribute('viewBox').split(/\s+/).map(Number);
  return {節: sv.closest('section').className, 歪み: ((r.height/vb[3])/(r.width/vb[2])).toFixed(2)};
});
```
