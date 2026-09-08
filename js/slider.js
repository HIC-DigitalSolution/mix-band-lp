// 横スライドの「現在位置の表示」と「矢印」だけ。
// 横移動そのものは CSS の scroll-snap がやる。JSが動かなくても
// カードは横スクロールで全部読める（矢印だけ出ない）。
(() => {
  for (const root of document.querySelectorAll('[data-slider]')) {
    const track = root.querySelector('.slider__track');
    const cards = [...track.children];
    const dots = [...root.querySelectorAll('[data-slider-dots] li')];
    const status = root.querySelector('[data-slider-status]');
    const prev = root.querySelector('[data-slider-prev]');
    const next = root.querySelector('[data-slider-next]');
    if (!track || cards.length === 0) continue;

    // JSが動く環境でだけ矢印を出す。
    for (const b of [prev, next]) if (b) b.hidden = false;

    let current = 0;
    const show = (i) => {
      current = Math.max(0, Math.min(cards.length - 1, i));
      dots.forEach((d, n) => d.classList.toggle('is-on', n === current));
      if (status) status.textContent = `${current + 1} / ${cards.length}`;
      if (prev) prev.disabled = current === 0;
      if (next) next.disabled = current === cards.length - 1;
    };

    // どのカードが中央に来ているかで現在位置を決める。スクロール量から
    // 割り算しない —— カード幅と余白が変わっても壊れないため。
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) {
        if (e.isIntersecting) show(cards.indexOf(e.target));
      }
    }, { root: track, threshold: 0.6 });
    for (const c of cards) io.observe(c);

    const go = (i) => {
      const target = cards[Math.max(0, Math.min(cards.length - 1, i))];
      if (target) track.scrollTo({ left: target.offsetLeft - track.offsetLeft, behavior: 'smooth' });
    };
    if (prev) prev.addEventListener('click', () => go(current - 1));
    if (next) next.addEventListener('click', () => go(current + 1));

    // 矢印キー。トラック自身が focus を取れるようにしてある。
    track.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') { e.preventDefault(); go(current + 1); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); go(current - 1); }
    });

    show(0);
  }
})();
