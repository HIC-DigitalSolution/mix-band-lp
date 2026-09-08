# harness-check が green でも、シナリオは壊れていることがある

- **Date:** 2026-09-08
- **どこで:** `harness/scenarios/design-comp.yaml` と `harness/scenarios/static-html.yaml`
- **気づいた場所:** 最初のコミット。**pre-commit フックに止められて初めて分かった**

## 何が起きたか

`harness/scenarios/design-comp.yaml` に手順を足した。文章を強調しようとして
行頭を `**` で始めた ——

```
  - **描画して自分の目で見る。tools/render.sh <file> [幅] で PNG にする。**…
```

**YAML はこれをエイリアス記法（`*`）と解釈する。**このYAMLサブセットのパーサは
フロースタイルとエイリアスを受けないので、**定義ファイルごと読み込めなくなった。**

そのあと `harness/scenarios/static-html.yaml` にも手順を足したが、
**そちらの steps はマップ形式**（`name` / `run` / `cwd` / `env`）で、
文字列の手順を混ぜたので同じく読み込めなくなった。
説明を `hint:` に書いたら、それも `steps` では許されないキーだった
（`hint` が使えるのは `requires` の項目）。

## なぜ気づかなかったか

**`harness-check` はコントラクトしか読まない。シナリオを読むのは `harness-run` だけ。**

つまり ——

| | 読むもの | 壊れたシナリオに気づくか |
| --- | --- | --- |
| `node scripts/harness/harness-check.mjs` | `harness/contracts/` | **気づかない** |
| `node scripts/harness/harness-run.mjs --stage <段>` | `harness/scenarios/` | 落ちる |

セッション中ずっと `harness-check` を走らせて
「機械判定すべて pass」を見ていたが、**その間シナリオは1つも読み込めていなかった。**
`harness-self-test` シナリオ（`harness/` を触ったら engine のテストと全定義のロードを
確かめる）は、**そのシナリオ自身がロードできないので走れない。**

## 教訓

**`harness/` を触ったら `harness-check` だけでなく `harness-run --stage pre-commit` も走らせる。**
定義のロードを確かめるのはそちらだけ。

**YAMLの行頭に `*` や `&` を置かない。**置くならシングルクォートで囲む。
強調の `**` は文中に入れる分には問題ないが、**行頭に来ると別の意味になる。**

**steps の形式はシナリオごとに違う。**混ぜられない ——

- `design-comp.yaml` / `workflow.yaml`（`stage: manual`）: **文字列の並び**
- `static-html.yaml` / `harness-self-test.yaml`（実行段）: **マップの並び**（`name` / `run` / `cwd` / `env`）

## 直したもの

- `design-comp.yaml` の当該行をシングルクォートで囲み、
  **囲む理由をその行自身に書いた**（次に足す人が同じ罠に落ちないように）
- `static-html.yaml` の手順を `name` + `run` のマップに直し、説明はYAMLコメントへ移した
