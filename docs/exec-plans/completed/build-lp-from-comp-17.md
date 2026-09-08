# カンプ17から本番LPを実装する

- **Started:** 2026-09-08
- **Completed:** 2026-09-08
- **Rule:** `harness/scenarios/design-comp.yaml` の最後の段
  （カンプは成果物ではなく、決定が成果物。本番HTMLはそのあと）
- **Completed path:** `docs/exec-plans/completed/build-lp-from-comp-17.md`

## Goal

`design/mix-lp-content-design-comp-17.dc.html` の6区間が `index.html` と
セクションごとの Sass として実装され、機械判定が全部 pass する。

## Scope

- [x] カンプを**画素ではなくソースで**読み、コピー・構造・装飾の座標を写す
- [x] 本番で使う素材を `design/assets/` から `img/` へ移す
- [x] `index.html` を手書きで6区間 + フッター + 店舗選択ダイアログ
- [x] `src/scss/sections/` を8枚（hero / intro / benefits / mechanism / info / cta / footer / dialog）
- [x] 店舗選択ダイアログの開閉（`js/store-dialog.js`）
- [x] **セクションごとに描画して自分の目で見る**
- [x] `tools/render.sh` の欠陥を2つ直す

## Non-scope

- 店舗名と公式LINE URL（支給待ち）。`TODO(依頼者確認)` のまま。
- og:image / og:url / noindex 解除（公開先が未定。manual の
  `og-image-and-index-before-release` が毎回出す）。
- 料金・入店時刻・年齢確認・キャンセル規定。**行ごと出していない。**
- 目標CVR。カンプA3の決定どおり「公開後の公式LINE遷移率を基準値として取得」。

## Constraints

- **`index.html` は手書き**、`css/` は Sass の生成物（2026-09-08 の規約）。
- 本番から `design/` を参照しない。画像は `img/`。
- 依頼者が取り下げた言い回しを事実として書かない。

## Acceptance

- [x] 6区間が 対象 → 体験 → 価値 → 仕組み → 開催情報 → 公式LINE の順で並ぶ
- [x] べた塗りのネオンピンクは「参加する店舗を選ぶ」だけ
- [x] オレンジは火花・点・細線・罫だけ。広い色面に使っていない
- [x] 動きは `prefers-reduced-motion: reduce` で全部止まる
- [x] 全セクションを描画して、カンプ17と見比べた

## Verification

- [x] `node scripts/build.mjs`
- [x] `node scripts/harness/harness-check.mjs`
- [x] HTML構文チェック（pre-push の step1 相当）を**リポジトリ内の全HTMLに**
- [x] `python3 tools/check-local-assets.py`
- [x] セクションごとの描画確認（`tools/render.sh`）

## Result

| 検証 | 実際の出力 |
| --- | --- |
| `node scripts/build.mjs` | `Built css/style.css`（17,161 bytes）。`index.html` は触られない |
| `harness-check` | 機械判定すべて pass、`manual` 27行 |
| HTML構文 | **18ファイル中0件の問題。**カンプ `.dc.html` も全部通る（pre-push が巻き込むので確認した） |
| `check-local-assets.py` | 6件すべて実在し、追跡対象 |
| 描画確認 | hero / intro / benefits / mechanism / info / cta / dialog の7枚を個別に描画し、カンプ17と一致を確認 |
| `image-budget` | 3ファイルとも400KB以内（FVクロップ 147KB / チャイム写真 69KB / ロゴ 3.5KB） |

### 途中で検査に2回止められた（どちらも正しい作動）

1. **`production-images-live-in-img`** が `src/scss/_tokens.scss` の
   「最終決定は design/…」という**出どころのコメント**で落ちた。
   → 規則が乱暴すぎた。禁じるのを**参照の形だけ**（`url()` と
   `src=`/`href=`/`poster=`/`srcset=`/`content=`）に絞った。
2. **`no-superseded-or-invented-facts`** が `index.html` の**私が書いた説明コメント**で落ちた。
   alt から取り下げ済みの言い回しを外した理由を書いたのだが、
   その説明文の中に当の語を書いていた。
   → **規則は緩めなかった。**目的は「本番HTMLにその語を残さない」なので、
   コメントの方を AGENTS.md 参照に書き換えた。正典を二重に書かない方が筋も通る。

### FVの alt について

支給バナーには開催頻度の言い回しが焼き込まれているが、依頼者が取り下げたもので、
実際は日〜木曜日限定。**写っている文字をそのまま alt に書くと、
読み上げ利用者にだけ誤情報が届く。**その一句だけ外し、理由を HTML のコメントに残した。
`key-art-is-a-supplied-banner`（焼き込みは全部 alt に入れる）と
`no-superseded-or-invented-facts` が衝突する箇所で、**後者を優先した。**

### tools/render.sh を2つ直した

- **一時ファイルを別ディレクトリに置いていたので、相対参照の画像が全部404**だった。
  カンプ17を最初に描画したとき画像が欠けており、**「確認したつもり」になっていた。**
  → 一時ファイルを元ファイルと同じディレクトリに置くようにした。
- **縦に長いページは1枚にすると縮んで何も判断できない。**
  → 第3引数で縦分割できるようにした。ただし qlmanage は
  **極端に縦長な文書を1枚に収めきれない**ので、
  今回はセクションごとの確認用ファイルを作って個別に描画した。

### 検証していないこと、残っているリスク

- **実ブラウザでの表示は未確認。**確認はすべて qlmanage（WebKit）。
  この環境のヘッドレスChromeは45秒で返ってこない（原因未特定）。
  **`<dialog>` の `showModal()` と `::backdrop` は qlmanage では確認できていない。**
  ダイアログは `open` 属性を付けた確認用ファイルで見た。
- **実機のSP幅（375〜430px）での確認はしていない。**確認は430px固定。
- **店舗リンクは `href="#"`。**支給後に置き換える。いまは `noindex`。
- **`img/` にカンプの資料が2つ入っている**
  （`mix-lp-content-design-reference.pdf` 318KB、`…-reference.webp` 183KB）。
  `img/` は公開対象なので、**このままだと社内向けの決定事項が公開先からダウンロードできる。**
  `design/` へ移すべきだが、依頼者がその場所を指したので動かしていない。
- `img/mix-band-key.webp`（元の支給バナー）は**どこからも参照していない。**
  FVは `mix-band-key-fv-crop.webp` を使っている。
