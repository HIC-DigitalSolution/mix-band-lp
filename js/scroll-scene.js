// 導入セクションを予告編のカット割りにする（2026-09-09、依頼者の選択A）。
// やることは2つだけ —— いま何カット目かを data-cut で渡し、
// そのカットの中での進み具合を --q（0→1）で渡す。見た目は全部CSS側。
//
// **フェードしない。**カットは opacity の即時切り替え（transition なし）。
// フェードにすると上品になり、狙っている「予告編の荒さ」から離れる。
//
// **JSが無ければ `is-cuts` が付かず、1枚目の写真と全文がそのまま出る。**
// 逆にすると、JSが落ちた瞬間に導入が空になる。
//
// GSAPは使わない。参考にした mememe は canvas(WebGL) の3D世界で、そもそも別技術
// （harness: reference-motion-is-watched-not-inferred）。
(() => {
  const section = document.querySelector('.intro');
  const stage = section && section.querySelector('.intro__stage');
  if (!section || !stage) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const CUTS = section.querySelectorAll('.intro__cut').length;
  if (!CUTS) return;

  section.classList.add('is-cuts');

  let lastCut = -1;

  const update = () => {
    const rect = section.getBoundingClientRect();
    const travel = rect.height - stage.offsetHeight;
    if (travel <= 0) return;

    const p = Math.min(0.9999, Math.max(0, -rect.top / travel));
    const cut = Math.floor(p * CUTS);
    // カットの中での進み具合。写真をゆっくり寄せるのに使う（カット間は動き続ける）。
    const q = p * CUTS - cut;

    section.style.setProperty('--q', q.toFixed(4));
    if (cut !== lastCut) {
      section.dataset.cut = String(cut);
      lastCut = cut;
    }
  };

  addEventListener('scroll', update, { passive: true });
  addEventListener('resize', update, { passive: true });
  update();
})();
