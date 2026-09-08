# public にして GitHub Pages で確認用リンクを出す

- **Started:** 2026-09-08
- **Completed:** 2026-09-08
- **Rule:** 2026-09-08 の依頼者の指示（GPTに見てもらうためのリンクをGitで出す／public にする）
- **Completed path:** `docs/exec-plans/completed/publish-pages.md`

## Goal

`https://hic-digitalsolution.github.io/mix-band-lp/` が 200 を返し、
CSS・画像・JS がすべて引ける。**配信されるのは公開用のファイルだけ。**

## Scope

- [x] リポジトリを public にする（依頼者の明示指示）
- [x] Pages を有効にする
- [x] ビルドが落ちる原因を特定する
- [x] 公開用ファイルだけを配信するワークフローを置く
- [x] 逸脱（自動デプロイ）を AGENTS.md に記録する

## Non-scope

- **本番公開。**`noindex` の解除、`og:image` / `og:url`、独自ドメインはやらない。
- 店舗リンクと未確定事項の穴埋め。

## Constraints

- **`--dereference` する tar に symlink を渡さない。**
- 組み込みの `pages-build-deployment` と自作ワークフローを二重に走らせない。
- `noindex` を外さない。

## Acceptance

- [x] ビルドの失敗原因が**推測ではなくログで**特定されている
- [x] サイトが 200 を返す
- [x] `docs/` と `design/` がサイトとして配信されていない

## Verification

- [x] `gh run view --log-failed` で実際のコマンドとエラーを読む
- [x] `curl` で `/` と全アセットの HTTP コードを確認
- [x] `node scripts/harness/harness-check.mjs`

## Result

| 検証 | 実際の出力 |
| --- | --- |
| 1回目（`ce97be8`） | `errored` — "Page build failed."。**待てば終わるものではなかった** |
| 2回目（`b33d9cb`・`.nojekyll` 追加） | 同じく失敗。**`.nojekyll` は Jekyll 用で、落ちていた段が違った** |
| 実際の失敗箇所 | `Upload artifact`。コマンドは `tar --dereference --hard-dereference -cvf artifact.tar --exclude=.git --exclude=.github .` |
| 原因 | **`--dereference` が symlink の実体を辿ろうとする。**このリポジトリの15本は共有元（外）を指していて、クローン先に存在しない。ファイル一覧を吐いた直後に exit 1 |
| 直し方 | 公開用ファイルだけを `_site` に組んで配信するワークフロー。symlink も `docs/` も `design/` も渡さない |

### 最初の見立ては外れていた

**「Jekyll が symlink とアンダースコアを嫌っている」と判断して `.nojekyll` を置いたが、外れだった。**
失敗していたのは Jekyll の段ではなく、その前の tar の段。
**API の `error.message` が "Page build failed." としか言わないので、
`gh run view --log-failed` で実コマンドを読むまで分からなかった。**
`.nojekyll` 自体は静的サイトに置いて正しいので残している。

### 検証していないこと、残っているリスク

- **このワークフローは main への push で自動デプロイする。**
  AGENTS.md の「push/deploy は自動で走らせない」から意図的に外れている。理由は同ファイルに記録した。
- **`configure-pages` の `enablement: true` が実際に配信元を切り替えるかは、初回実行で確認する。**
  切り替わらないと、組み込みの `pages-build-deployment` が並走して落ち続ける。
- **リポジトリは public。**サイトに出ないだけで、`docs/` の社内向け記録・カンプ・支給素材は
  リポジトリとしては誰でも読める。**履歴にも残っているので、後から消しても辿れる。**
