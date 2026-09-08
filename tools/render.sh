#!/bin/sh
# HTML / SVG を画像に起こして、自分の目で見るための開発用ヘルパ。
#
# **カンプやHTMLを人に見せる前に、必ずこれを通して描画を見る。**
# 2026-09-07、描画を確認せずに publish して2回続けて差し戻した
# （docs/gotchas/read-the-css-not-the-artwork.md）。
#
# 使い方: tools/render.sh <file.html|file.svg> [幅]
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

qlmanage -t -s "$W" -o "$TMP" "$TARGET" >/dev/null 2>&1 || true
SHOT="$TMP/$(basename "$TARGET").png"
[ -s "$SHOT" ] || { echo "描画に失敗した: $SRC" >&2; exit 1; }
cp "$SHOT" "$OUT"

if [ "$SLICES" -gt 1 ]; then
  DIMS="$(python3 -c "
import struct,sys
d=open(sys.argv[1],'rb').read(33)
w,h=struct.unpack('>II', d[16:24]); print(w,h)" "$OUT")"
  IW="$(echo "$DIMS" | cut -d' ' -f1)"
  IH="$(echo "$DIMS" | cut -d' ' -f2)"
  SH=$(( IH / SLICES ))
  i=1
  while [ "$i" -le "$SLICES" ]; do
    OFF=$(( (i - 1) * SH ))
    sips -c "$SH" "$IW" --cropOffset "$OFF" 0 "$OUT" --out "$OUT_DIR/$NAME-$i.png" >/dev/null 2>&1
    echo "$OUT_DIR/$NAME-$i.png"
    i=$(( i + 1 ))
  done
  exit 0
fi

echo "$OUT"
