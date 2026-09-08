# design/

2026-09-08、依頼者の指示でカンプ作業を一旦止め、Claude Codeでの実装へ移ります。
**実装基準は `mix-lp-content-design-comp-17.dc.html`** です。カンプ 01〜07 は
却下済みの記録として残しています。理由は
`../docs/exec-plans/completed/reference-sites-into-harness.md` にあります。

`../img/mix-lp-content-design-reference.pdf` と
`../img/mix-lp-content-design-reference.webp` は、実装引き継ぎ用の確認資料です。
現環境ではカンプ17の全体画像を書き出せなかったため、**既存のカンプ10 PNGから作成しており、
最新版そのものではありません。**全体の構成と配色だけを確認し、カンプ11以降の変更は
`../docs/design-docs/content-design-comp-11.md`、`content-design-comp-15.md`、
`content-design-comp-16.md`、`content-design-comp-17.md` と
`overview-motion-spec.md` を参照してください。本番HTML・CSS・JSからこのPDFとWebPを参照せず、
公開前に `img/` から外すか公開対象から除外します。

現在の実装基準は `mix-lp-content-design-comp-17.dc.html` です。カンプ11の横幅いっぱいの
FV、上部の焼き込みコピーをカットした `assets/mix-band-key-fv-crop.webp`、左上ロゴ、写真の
微細なズーム、光の呼吸、端の光線を引き継ぎ、SOUND TRIPのように大きな有機形の端へ小さな人物・波線・
乾杯の記号をSVGで1組だけ置いています。カンプ17ではFV素材の上側だけを切り出した仮写真
`assets/mix-band-chime-photo.webp` をチャイムセクションへ追加し、同心円と「4〜6」を写真の手前へ重ねています。
カンプ15ではWHAT IS MIX左下を有機形・平行な輪郭線・小さな点へ
整え、YOUR NIGHT横の斜め文字を削除しました。現在は依頼者支給の `assets/mix-toast-couple.svg` を人物モチーフへ
差し替えています。決定は `../docs/design-docs/content-design-comp-17.md` にあります。
カンプ13の大きな人物レイヤーと、調整前のカンプ14〜16は比較用として残します。

## カンプを作る人が先に読むもの

| | |
| --- | --- |
| `../AGENTS.md` | 確定情報・却下済みの案・推測で埋めてはいけない項目 |
| `../docs/design-docs/reference-sites.md` | **参考3サイトから取った技法と、支給バナーの色の実測値** |
| `../docs/design-docs/information-request-checklist.md` | ワイヤーフレームを埋めるために依頼者・店舗から知りたい情報 |
| `../docs/design-docs/content-structure-first-draft.md` | 2026-09-08の回答を反映した現在の内容構成とコピー案 |
| `../docs/design-docs/high-gal-color-guide.md` | 依頼者提示の配色ガイド（検討中） |
| `../docs/design-docs/lp-visual-knowledge.md` | 画づくりの判断基準（§番号で引く） |
| `../harness/scenarios/design-comp.yaml` | 手順の正典 |

コードでカンプを起こす前に、`../docs/design-docs/pre-code-design-blueprint.md` で
情報構造・面の役割・未決定事項を整理します。そこにある「カンプへ進む条件」が
揃うまでは、新しい `.dc.html` を作りません。

現在の内容設計は `../docs/design-docs/content-structure-first-draft.md` です。
`mix-lp-content-funnel-wireframe-10.png` は、依頼者から受け取った
`references/content-funnel-order-reference.png` の説得順をMIX LPへ対応させています。
**誰に？・キャッチ → 共感・理解 → メリット → 仕組み → 実績・証拠 → お客さまの声 →
オファー → 限定性 → CTA**の順です。

2026-09-08の回答により、次のワイヤーフレームでは実績・証拠、お客さまの声、独立した限定性を
外します。料金と受付時間も載せません。参加条件はオレンジバンドです。
店舗一覧は本文から外し、「参加する店舗を選ぶ」で開くダイアログ内だけに置きます。
店舗を選ぶと、その店舗の公式LINEへ移動します。

対象は20〜30代の男女。来店前の期待は「いつもと違う刺激」「関係が動くきっかけ」
「非日常」です。開催期間は2026年10月1日〜31日、日〜木曜日限定です。
画像上の英語は識別ラベルで、本番コピーではありません。日本語の内容は
`../docs/design-docs/pre-code-design-blueprint.md` の「内容ファネル・ワイヤーフレーム10」を正とします。
HTML・Sass・JSには未反映です。

依頼者指定の必須訴求は **「恋愛リアリティ体験」「最大4〜6組」「日〜木曜日限定」** の3点です。
支給バナー内の小さい焼き込み文字だけに頼らず、FV直下で短く見せたうえで、イベント理解・
仕組み・開催情報の各セクションへ1点ずつ割り当てます。開催情報では
2026年10月1日〜31日と「日〜木曜日限定」を同じ面に置きます。

`mix-lp-content-wireframe-09.png` は参考図を反映する前の構成です。
`mix-lp-mobile-wireframe-08.png` は内容を入れる前の構成元です。

採用した配色方向は `mix-lp-cohesive-neon-color-study-06.png` です。
2026-09-08、依頼者が「このデザインが一番良かった」と判断しました。
濃紫→電気的な紫→ラズベリーピンクを主な流れにし、淡いピンクの面で本文を読ませます。
CTAはネオンピンク、オレンジは小さな火花・点・細線だけです。

`mix-lp-orange-complement-color-study-07.png` は比較用の記録です。チャイム面を広い
ブルーバイオレットにし、オレンジの光を一度だけ大きく置きましたが、カンプ08の確認後に
比較06へ戻す判断が出ました。

`mix-lp-exciting-color-study-05.png` は見直し前の比較です。広いコバルトブルー、
ネオンピンク、オレンジが同じ強さで競合し、サイバーゲーム寄りに見えました。

比較元の静止デザインカンプは `mix-lp-yankee-neon-visual-comp-03.png` です。
構成ベースを `on-the-trip.com/sound-trip` とし、広い紫の地、境界へ食い込むピンクの形、
端だけのゼブラ、チャイムの同心円、大小の光だまり、情報カード、濃紫へ戻るCTA面を
ヤンキーネオンの質感でつないでいます。FVの白い面は750 × 627pxの支給キーアート比率です。
HTML・CSSには未反映です。

`mix-lp-banner-aligned-color-study-04.png` は、支給バナーとの不一致を直すための
**未確定の配色比較**です。構成は03のまま、濃紺と青い店内光を増やし、
マゼンタと白い面を減らしています。依頼者確認前なので、現在の配色決定とハーネスは変えていません。

`mix-lp-sound-trip-structure-direction-02.png` は、質感を足す前の構成検討です。

`mix-lp-yankee-neon-direction-01.png` は構成更新前の記録です。
そこから残したのは配色の役割と、リボンを使わない判断です。

## 実装側で確定できたこと（数字が出ているもの）

- **CTAはオレンジにしない。** 支給バナーの高彩度画素は**赤〜橙で 78.8%**、
  **ピンク・マゼンタは 4.5%**。オレンジのCTAはバナーの
  「全員オレンジバンド」バッジと**同じピルが2つ並ぶ**（仮置き中もこの衝突は起きる）。
- **CTAが最強面である根拠は彩度ではない。**「べた塗りの面積」と、周囲で同じ色を面に使わないこと。
- **日本語の見出しは 375px 幅で 24px が上限**（26pxだと12文字で折り返して崩れた）。
- **リボンの形**は `assets/ribbon-sprite.svg`（生成器は `assets/ribbon-gen.py`）に記録していますが、
  **2026-09-07の新しい設計では不採用の方向です。新しいカンプへ流用しません。**
  実物の素材画像から取った語彙 —— 針状のテーパー／色違いの平行な束／
  幅の広い端の返し／太い帯の波打つ下辺／裏面は後ろから覗く細い筋。
  **3回作り直した結果です**（①太さ一定の管 ②破った紙 ③バラバラの弧 → ④束）。
  使わない場合は消してかまいません。

## 作ったものを見るとき

`tools/render.sh <file> [幅]` で PNG になります。**縦に長いページは全体だと縮んで
判断できないので、FVだけ切り出して描画する**のが早いです。
