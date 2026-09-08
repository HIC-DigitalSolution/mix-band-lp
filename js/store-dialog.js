// 店舗選択ダイアログの開閉だけ。
// 本文に店舗一覧を置かず、CTAの操作後だけ出す（カンプ17 A2 の決定）。
(() => {
  const dialog = document.getElementById('store-dialog');
  if (!dialog || typeof dialog.showModal !== 'function') return;

  // JS が動く環境でだけボタンを有効にする。動かなければ何も起きない。
  for (const button of document.querySelectorAll('[data-open-dialog]')) {
    button.addEventListener('click', () => dialog.showModal());
  }
  for (const button of dialog.querySelectorAll('[data-close-dialog]')) {
    button.addEventListener('click', () => dialog.close());
  }

  // 背景（::backdrop）を押したら閉じる。dialog 要素自身がその領域を受け取る。
  dialog.addEventListener('click', (event) => {
    if (event.target === dialog) dialog.close();
  });
})();
