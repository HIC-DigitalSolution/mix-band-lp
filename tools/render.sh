#!/bin/sh
# HTML / SVG を画像に起こして、自分の目で見るための開発用ヘルパ。
#
# **カンプやHTMLを人に見せる前に、必ずこれを通して描画を見る。**
# 2026-09-07、描画を確認せずに publish して2回続けて差し戻した
# （docs/gotchas/read-the-css-not-the-artwork.md）。
#
# 使い方: tools/render.sh <file> [出力幅] [分割数] [ビューポート幅] [ビューポート高]
#   出力は tmp/render/<name>.png（tmp/ は .gitignore 済み）
#
# 経路は qlmanage（QuickLook / WebKit）。**この環境のヘッドレスChromeは戻ってこない**
# ——フィルタの有無に関係なく45秒で打ち切られることを確認済み。原因は未特定。
#
# 注意: これは実行されるスクリプトです。hook と同じ基準でレビューしてください。
set -eu
SRC="${1:?usage: tools/render.sh <file> [width] [slices]}"
W="${2:-1500}"
# 縦に長いページは、全体を1枚にすると縮んで何も判断できない。
# slices を渡すと、その枚数に縦分割して <name>-1.png … を出す。
SLICES="${3:-1}"
# ビューポート幅。**メディアクエリはこの幅で評価される。**
# qlmanage は自前の幅で描画してから縮小するので、-s の値では効かない
# （2026-09-09 に踏んだ。PC用の分岐を入れた途端、SPの確認が全部PC表示になっていた）。
# 指定すると、その幅の iframe に入れてから描画する。
VIEW_W="${4:-}"
# iframe の高さ。**足りないとページの下が黙って切れる**（2026-09-09、PC幅の確認で
# 4000px 固定のまま下半分を見落とした）。ページの実高さを渡すこと。
VIEW_H="${5:-4000}"
# 表示を開始する縦位置。**qlmanage は高さ1400px前後で描画を打ち切る**ので、
# 縦に長いページは VIEW_H を画面1枚分にして OFFSET を送りながら帯で見る
# （2026-09-09、5600pxのPCページを1枚で出そうとしてFVしか写らなかった）。
OFFSET="${6:-0}"
OUT_DIR="tmp/render"; mkdir -p "$OUT_DIR"
NAME="$(basename "$SRC" | sed 's/\.[^.]*$//')"
OUT="$OUT_DIR/$NAME.png"
SRC_DIR="$(cd "$(dirname "$SRC")" && pwd)"
TMP="$(mktemp -d)"
WRAP="$SRC_DIR/.render-$$.tmp.html"
trap 'rm -rf "$TMP"; rm -f "$WRAP"' EXIT

case "$SRC" in
  *.svg) cp "$SRC" "$TMP/r.svg"; TARGET="$TMP/r.svg" ;;
  *)
    # Artifact形式の .dc.html は doctype も charset も持たない。
    # 付けずに描画すると **UTF-8 が化けて、見たつもりで何も読めない。**
    { printf '<!doctype html><html lang="ja"><head><meta charset="utf-8">'
      printf '<meta name="viewport" content="width=device-width,initial-scale=1">'
      printf '<style>html,body{margin:0}img{max-width:100%%}</style></head><body>'
      cat "$SRC"
      printf '</body></html>'; } > "$WRAP"
    TARGET="$WRAP" ;;
esac

if [ -n "$VIEW_W" ]; then
  FRAME="$SRC_DIR/.render-frame-$$.tmp.html"
  trap 'rm -rf "$TMP"; rm -f "$WRAP" "$FRAME"' EXIT
  printf '<!doctype html><meta charset="utf-8"><body style="margin:0;background:#241c20">' > "$FRAME"
  printf '<div style="width:%spx;height:%spx;overflow:hidden;position:relative">' \
    "$VIEW_W" "$VIEW_H" >> "$FRAME"
  printf '<iframe src="%s" width="%s" height="%s" scrolling="no" style="border:0;display:block;position:absolute;top:-%spx"></iframe></div>' \
    "$(basename "$TARGET")" "$VIEW_W" "$(( OFFSET + VIEW_H ))" "$OFFSET" >> "$FRAME"
  printf '</body>' >> "$FRAME"
  TARGET="$FRAME"
fi

qlmanage -t -s "$W" -o "$TMP" "$TARGET" >/dev/null 2>&1 || true
SHOT="$TMP/$(basename "$TARGET").png"
[ -s "$SHOT" ] || { echo "描画に失敗した: $SRC" >&2; exit 1; }
cp "$SHOT" "$OUT"

if [ "$SLICES" -gt 1 ]; then
  # **sips の --cropOffset は使わない。**`--cropOffset 0 0` は左上ではなく中央を切り、
  # 非ゼロのときだけ左上からの絶対座標になる（2026-09-09 に PIL と突き合わせて確定）。
  # 1枚目だけ中央が出るという分かりにくい壊れ方をするので、分割は tools/slice.py に任せる。
  python3 "$(dirname "$0")/slice.py" "$OUT" "$OUT_DIR" "$NAME" "$SLICES"
  exit 0
fi

echo "$OUT"
