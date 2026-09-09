// FVのCTAが画面より上へ流れている間だけ、下に追従CTAを出す（2026-09-09 の指示）。
//
// **下のCTAセクションが見えている間は出さない。**同じボタンが2つ並ぶと、
// どちらを押すのか迷わせるだけで、CVは増えない。
//
// **IntersectionObserver は使わない。**最下部から一気に最上部へ戻ると、FVのCTAは
// 「画面の上」から「画面の下」へ移るだけで交差状態が変わらず、通知が来ないので
// バーが出たままになる（2026-09-09 に実測して踏んだ）。位置から毎回計算する。
//
// JSが無い環境では `hidden` のまま出ない。**それで壊れるものは無い** ——
// FVのCTAと下のCTAはHTMLに在り、ダイアログもそのまま開く。
(() => {
  const bar = document.getElementById('sticky-cta');
  const heroCta = document.querySelector('.cta__button--hero');
  const pageCta = document.querySelector('.cta .cta__button');
  if (!bar || !heroCta || !pageCta) return;

  const update = () => {
    // FVのCTAが画面の上へ抜けきったか。
    const passedHero = heroCta.getBoundingClientRect().bottom <= 0;
    // 下のCTAが少しでも見えているか。
    const cta = pageCta.getBoundingClientRect();
    const pageCtaVisible = cta.top < window.innerHeight && cta.bottom > 0;

    const show = passedHero && !pageCtaVisible;
    if (show === !bar.hidden) return;

    bar.hidden = !show;
    // hidden を外した直後に class を付けて、transition を効かせる。
    if (show) requestAnimationFrame(() => bar.classList.add('is-in'));
    else bar.classList.remove('is-in');
  };

  // **rAFで間引かない。**間引くフラグを持たせたら、rAFが走らない状況
  // （タブが隠れている等）でフラグが立ったままになり、以後まったく更新されなくなった
  // （2026-09-09 に踏んだ）。中身は矩形2つの読み取りだけなので、そのまま呼ぶ。
  addEventListener('scroll', update, { passive: true });
  addEventListener('resize', update, { passive: true });
  update();
})();
