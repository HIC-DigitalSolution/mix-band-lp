# index.html とセクション別HTML・Sassの構成

## Goal
ルートのindex.htmlを閲覧入口にし、HTMLとSCSSをセクション別に編集できる状態にする。

## Scope
Sass導入、HTML結合、変更監視、確定事実のみの土台、README、AGENTSの現状更新。参考サイトの最終決定と食い違っていたハーネス説明値の修正。index.html追加で表面化した、画像検証が通常のmeta contentまでパス扱いする問題の修正。

## Constraints
ユーザーの今回の指示により「ビルドなし」を変更する。共有symlinkは編集しない。既存のステージ済み変更を維持する。却下済みカンプを本番に採用しない。公開しない。

## Acceptance
index.htmlとCSSを生成でき、セクションHTMLとSassの変更を検知して再生成する。出力は静的HTML/CSSで、閲覧にJSは不要。

## Verification
- [x] npm run build
- [x] npm run watchでHTML・SCSSの更新検知
- [x] ローカルHTTPでHTML・CSSの200応答とファイル一致
- [x] Quick Lookで生成ページを描画し目視（CSSを埋め込んだ検証用コピー）
- [x] python3 tools/check-local-assets.py とmeta属性の回帰確認
- [x] node scripts/harness/harness-check.mjs

## Result
Sass 1.77.8を現環境Node 20.14に合わせて固定。HTML4セクションと各SCSSをsrcに集約し、index.htmlとcss/style.cssへ出力。OSの再帰watchがEMFILEになったため500msの定期チェックに変更し再生成を確認。npmの依存監査は脆弱性0件。npm run checkは成功し、機械検査は全件合格。

manual項目は確認済み：今回の範囲は実装の構造整備。世界観・CV・流入・目標CVR・キーアート配置・CTA・公開先は未確定で、デザイン完成や公開準備完了を意味しない。白地の土台だけを実装し、装飾・アニメーション・外部リンク・フォームは追加していない。未確定事項はTODOコメント、OGの絶対URLは未設定、noindexを設定。ハーネスのhead検査はOGコメントにも一致するため、合格しても公開用メタデータの完成を示さない。

画像検証は通常の `meta content` をローカルパスから除外し、`og:image` と `og:url` の検査は維持した。

参考サイトの採用範囲も確認した。KBC創立70周年サイトからはリボンの形と浮遊の物理、FUTURE TRAINからは端点間を補間する色ランプの原則を取る。最新決定に合わせ、ランプを `#2A1030` から `#FF2D95` までの6段階にし、`#FF8A1F` は小面積のマーク色として分離した。見た目は依頼者側のデザイン確定後に実装する。
