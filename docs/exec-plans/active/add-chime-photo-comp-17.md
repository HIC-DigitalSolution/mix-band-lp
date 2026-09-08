# チャイムセクションへFV写真を差し込むカンプ17

- **Started:** 2026-09-08
- **Rule:** `harness/scenarios/design-comp.yaml`, `harness/contracts/mix-lp.yaml`
- **Completed path:** `docs/exec-plans/completed/add-chime-photo-comp-17.md`

## Goal

チャイムセクションにFVと同じ店内・人物の空気を持つ仮写真を差し込み、写真と同心円の重なりで「物語が動く」
瞬間を表現する。新しい写真が支給されたら差し替えられる構造にする。

## Scope

- [x] カンプ16を複製し、カンプ17として編集する
- [x] FV素材の上側326pxを `mix-band-chime-photo.webp` として切り出し、チャイム面へ横長に配置する
- [x] 濃紫のオーバーレイ、同心円、細いオレンジ線のレイヤー順を決める
- [x] A3決定ボード、設計文書、README、AGENTSへ追加内容を記録する

## Non-scope

- 新しい写真素材の生成・撮影・購入
- FVの構図、支給された乾杯SVG、WHAT IS MIX左下、YOUR NIGHTの変更
- 本番の `src/index.html`、`src/sections/`、Sass、JSへの実装

## Constraints

- 写真は現段階の仮置きで、最終素材の支給後に差し替えられること
- 焼き込みタイトルが写真面へ露出しない上側326pxのトリミングを採用すること
- 写真は本文の可読性を落とさず、同心円と「4〜6」の情報を手前に残すこと
- オレンジは既存のチャイム光と細線に限定し、広い面へ広げないこと

## Acceptance

- [x] カンプ17のチャイムセクションに写真面が1枚だけ存在する
- [x] 写真の上に暗いオーバーレイ、同心円、「4〜6」が重なっている
- [x] 写真の焼き込みタイトルを表示範囲から外す設計をA3と設計文書で追跡できる
- [ ] 375pxのHTTPブラウザ表示で、写真のトリミング・文字の可読性・横スクロールを確認する

## Verification

- [x] `node scripts/harness/harness-check.mjs`（all machine-verified invariants passed。manual 24行は人の確認待ち）
- [x] HTMLParserでカンプ17を解析する（298 start-tags / errorsなし）
- [x] `git diff --check`（問題なし）
- [ ] 375px実寸のHTTPブラウザ表示（環境上の制限により未確認）

## Result

カンプ17へチャイム写真を追加し、同心円と「4〜6」を写真の手前へ残した。`harness-check.mjs` は
all machine-verified invariants passed（manual 24行）、HTMLParserは298 start-tags / errorsなし、
`git diff --check`も問題なしだった。HTTP経路の375px表示が未確認のため、焼き込みタイトルの露出と
写真・本文の重なりには目視確認が残る。
