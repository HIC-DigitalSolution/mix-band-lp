// 節に入ったら、中の要素を1つずつ遅らせて出す（2026-09-09、依頼者の指定で
// mememe-official.jp の concept セクションから取った動き）。
//
// **GSAPは入れない。**向こうは GSAP + ScrollTrigger だが、実測すると concept の文字は
// 初回に1度出るだけで、離れて戻っても再生されない（ScrollTrigger.getAll() は0件）。
// 同じ見え方は IntersectionObserver ＋ CSS transition ＋ 1行ごとの delay で足りる。
//
// **JSが無い環境では最初から見えている。**隠すのはJS側の仕事で、CSSの既定は「見える」。
// こうしないと、JSが落ちた瞬間に本文が消える。
(() => {
  const targets = document.querySelectorAll('[data-reveal]');
  if (!targets.length || !('IntersectionObserver' in window)) return;

  for (const group of targets) {
    // ここで初めて「出る前」の状態にする。
    group.classList.add('is-armed');
    const items = group.querySelectorAll(':scope > *');
    items.forEach((el, i) => el.style.setProperty('--reveal-i', i));
  }

  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-in');
      // 一度出したら監視をやめる。戻るたびに再生すると、読み返すときに邪魔になる。
      observer.unobserve(entry.target);
    }
  }, { threshold: 0.2 });

  for (const group of targets) observer.observe(group);
})();
