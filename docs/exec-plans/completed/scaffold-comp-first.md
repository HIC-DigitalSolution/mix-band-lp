# カンプ先行で始めるための骨組みを入れる

- **Started:** 2026-09-07
- **Rule:** [docs/exec-plans/README.md](../README.md)
- **Completed path:** `docs/exec-plans/completed/scaffold-comp-first.md`

## 目的

空のディレクトリだった `MIX交流上等バンドLP/` を、**カンプから着手できる状態**にする。
ハーネス（判定）・hook（強制）・カンプの手順・引き継ぐべき事実が、
**会話ではなくリポジトリに載っている**状態が完了条件。

## スコープ

- [x] 共有ハーネスを **symlink で参照**（依頼者の選択。`asb_lp_Y2K` と同じ構成）
- [x] `harness/contracts/mix-lp.yaml` — このLP固有の不変条件（機械7・manual6）
- [x] `harness/scenarios/design-comp.yaml` — カンプを起こす順番（`manual`）
- [x] `harness/scenarios/static-html.yaml` — 公開前の構文・404チェック（`pre-push`）
- [x] `tools/check-local-assets.py` — 参照先の実在と gitignore 除外を見る
- [x] `AGENTS.md` — Y2K から引き継ぐ事実・却下済みの案・配色の方向
- [x] `.claude/`（settings / agents / skills / launch）と `.codex/`
- [x] `.githooks/` と `sh scripts/install-hooks.sh`
- [x] `git init`

## 非スコープ

- **カンプそのもの。**まだ1枚も起こしていない
- **本番HTML。**1行も無い
- **前提（CV1つ・ペルソナと流入文脈・目標CVR）の決定。**依頼者と決めるもので、
  骨組みの仕事ではない。`AGENTS.md`「まだ決まっていないこと」に空欄として置いた
- 共有元（`Job/LP`）側の `.gitignore` と `AGENTS.md` の更新。**別の計画で行う**
  （共有元は別リポジトリで、`19歳LP` のときも別計画にしている）

## 制約

- **雛形（`~/Desktop/template/`）は共有元より古い。** `harness-git.mjs` の
  symlink 共有対応（`harness/.shared-source` の判別）が入る前、`lp-design.yaml` に
  §10 の視覚ルールが入る前、`lp-visual-knowledge.md` が存在する前の版だった。
  **雛形を丸ごとコピーすると、古いエンジンで始まる。**共有ぶんは共有元から取り、
  雛形にしか無いもの（hook・ツール固有設定）だけを実ファイルで持つ。
  **なお雛形は作業中に Desktop から消えた**（移動か削除。追跡していない）。
  hook とツール固有設定は、消える前に読んだ内容から書き戻している
- **symlink 側を編集すると全プロジェクトに効く。**`.claude/settings.json` の `deny` で
  主要な経路（`scripts/harness/**`・共通 contracts・共通 docs）を塞いだ。
  塞いでいない経路（`Bash` 経由の書き込みなど）は残る
- **`lp-design.yaml` は共有ぶんで、全て `manual`。**カンプ段階のLPでは、
  この9〜10行が採点表そのものになる。減らさない
- 機械判定は「意味」を見られない。**カンプが良いかどうかは1行も判定していない**

## 受け入れ条件

- [x] `node scripts/harness/harness-check.mjs` が起動し、契約4本を読み込む
- [x] dead link が0本
- [x] `PROJECT_ROOT` が共有元ではなくこのプロジェクトに解決される
      （共有元も `harness/` を持っているので、ここを間違えると
      「差分なし・全部pass」の顔で何も見ないまま通る）
- [x] pre-commit が呼ぶ経路（`harness-check --staged`）で、骨組みの差分に対して
      `exec-plan-required` と `exec-plan-shape` が pass する。**実コミットはしていない**
- [x] `[manual]` の行に、Y2K で踏んだ穴（参考の実物・パロディの線引き・却下済み）が出る

## 検証項目

- [x] `node scripts/harness/harness-check.mjs`
- [x] `node scripts/harness/harness-run.mjs --stage pre-push --dry-run`
- [x] `node --test scripts/harness/lib/*.test.mjs`（共有エンジンが壊れていないこと）
- [x] `for l in $(find . -type l); do [ -e "$l" ] || echo "DEAD: $l"; done` が何も出さない
- [x] `python3 tools/check-local-assets.py`
- [x] `python3 -c "import glob,html.parser ..."`（HTML構文チェックの手順が動くこと）
- [x] `sh scripts/install-hooks.sh` のあと `git config core.hooksPath` が `.githooks` を指す
- [x] `git add -A` のあと `node scripts/harness/harness-check.mjs --staged`
- [x] 検査範囲（prefix）が正しいこと。日本語のディレクトリ名で実測する

## 検証結果

2026-09-07 実行。

| 検証 | 結果 |
| --- | --- |
| `harness-check.mjs` | 契約4本を読み込み、機械判定は全て pass。`manual` 18行 |
| `harness-run.mjs --stage pre-push --dry-run` | `static-html-scenario` を認識。骨組みの差分には HTML/CSS が無いため skip |
| `node --test scripts/harness/lib/*.test.mjs` | 下記のとおり |
| dead link | 0本 |
| `check-local-assets.py` | 「参照が0件（index.html がまだ無い）」で 0 終了 |
| HTML構文チェック | ダミー1枚を置いて `html ok: 1 件` |
| `install-hooks.sh` | `core.hooksPath` → `<project>/.githooks`。**出力の注意文は誤り**（下記） |
| `harness-check --staged`（34ファイル） | `exec-plan-required` = structural change detected, exec-plan found。`exec-plan-shape` = required sections present。機械判定は全て pass |
| 検査範囲 | `files=33`／`scope=` 行なし = prefix 空 = リポジトリ全体 = このプロジェクト。**正しい** |

### 途中で見つけて直したこと

- **`deny` の床が、手順書に書いたコマンドを塞いでいた。**dead link の確認に
  `find . -type l ! -exec test -e {} \; -print` と書いたが、`deny` には
  `Bash(find * -exec*)` がある（任意実行の経路なので塞ぐのが正しい）。
  **塞いだ経路を手順書が指していると、次の人が必ず詰まる。**`AGENTS.md`・
  Codex の checker・Claude の checker の3か所をループ形に直した:
  `for l in $(find . -type l); do [ -e "$l" ] || echo "DEAD: $l"; done`
- **`install-hooks.sh` の注意文が、同じパスを2回出して「サブディレクトリだ」と言う。**
  原因はディレクトリ名の「バ」で、`pwd` が NFC・git が NFD を返すため文字列比較が
  落ちること。**動作は正しい**（hooksPath も検査範囲も実測で確認）。
  実体は共有元にあるので直していない。
  [docs/gotchas/nfd-path-breaks-string-compare.md](../../gotchas/nfd-path-breaks-string-compare.md)

### 検証していないこと、残っているリスク

- **カンプの良否は1行も検証していない。**このハーネスが見ているのは、
  仮文言の混入・404・容量・head の欠落・取り下げ済みの数字だけ。
  **「面白いか」「参考に似ているか」は `manual` の18行が全部で、判定するのは人**
- **`static-html-scenario` はまだ一度も本番の対象で走っていない。**HTML が無いので、
  実際に走るのは最初の `index.html` を push するときが初回になる
- **`design/` に置く `.dc.html` も `**/*.html` の対象に入る。**カンプが増えると
  pre-push の構文チェックがカンプまで見る。壊れたカンプで push が止まる可能性があるが、
  対象から外すと本番HTMLの確認漏れの経路ができるので、そのままにしている
- **共有元が無い環境ではこのプロジェクトは動かない。**symlink 構成を選んだ結果で、
  復旧手順は `AGENTS.md` に書いた。**別マシンでの復旧は試していない**
- **雛形（`~/Desktop/template/`）が消えたことは追跡していない。**次に新規LPを生やす人が
  種を見つけられない可能性がある。共有元の `AGENTS.md` は雛形の場所を指しているので、
  そこも直す必要があるが、**この計画のスコープ外**（共有元側の変更として別に行う）
- **実コミットをしていないので、hook 経由（`git commit`）での実行は未検証。**
  検証したのは hook が呼ぶのと同じ `harness-check --staged` の経路。
  **hook スクリプト自体の起動は、最初のコミットが初回になる**
- **共有元の `.gitignore` にこのディレクトリを入れていない。**入れるまで、共有元で
  `git add .` を打つと**中身ではなく gitlink 1本**が記録される
  （`19歳LP` で同じことを直した記録が共有元の完了計画にある）。**次の作業**
