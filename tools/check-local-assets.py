#!/usr/bin/env python3
"""index.html が参照しているローカルファイルが、実在して、かつ .gitignore で
除外されていないことを確かめる。

この2つは同じ症状（公開サイトでだけ404、ローカルでは最後まで気づけない）で出るのに、
原因が別なので両方見る。過去に両方踏んでいる:

  - 19歳LP:  og:image を相対パスで書いてクローラが拾わなかった
  - Y2K:     assets/* を全除外して許可リストに戻し忘れ、公開サイトでだけ画像が消えた

差分ではなく作業ツリーを見る。壊れているかどうかは、いま何を編集したかとは関係がない。
"""

import html.parser
import os
import re
import subprocess
import sys

TARGETS = ["index.html"]
# 外部URL・データURI・ページ内リンク・tel/mailto は対象外。
EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//|#|\?)", re.IGNORECASE)
ATTRS = ("src", "href", "poster", "content")


class Refs(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.found = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        for name, value in attrs:
            # content は通常説明文。ローカル資産になり得るOGのURLだけ検査する。
            if name == "content" and not (
                tag == "meta" and attributes.get("property") in ("og:image", "og:url")
            ):
                continue
            if not value:
                continue
            if name == "srcset":
                for part in value.split(","):
                    candidate = part.strip().split(" ")[0]
                    if candidate:
                        self.found.append(candidate)
            elif name in ATTRS:
                # meta[content] は og:image などの絶対URLが入る。相対で書かれていたら
                # クローラが拾わないので、そこは別の不変条件（head-basics）ではなく
                # ここで「実在するか」だけを見る。
                self.found.append(value)


def local_refs(path):
    parser = Refs()
    with open(path, encoding="utf-8") as handle:
        parser.feed(handle.read())

    out = []
    for raw in parser.found:
        ref = raw.split("?")[0].split("#")[0].strip()
        if not ref or EXTERNAL.match(ref):
            continue
        out.append(ref.lstrip("/"))
    return sorted(set(out))


def css_refs(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    out = []
    for raw in re.findall(r"url\(\s*['\"]?([^'\")]+)", text):
        ref = raw.split("?")[0].split("#")[0].strip()
        if not ref or EXTERNAL.match(ref):
            continue
        # CSS の相対パスは CSS ファイルからの相対。
        out.append(os.path.normpath(os.path.join(os.path.dirname(path), ref)))
    return sorted(set(out))


def ignored(paths):
    if not paths:
        return set()
    result = subprocess.run(
        ["git", "check-ignore", "--stdin"],
        input="\n".join(paths),
        capture_output=True,
        text=True,
    )
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def main():
    refs = []
    for target in TARGETS:
        if os.path.exists(target):
            refs.extend(local_refs(target))
    for root, _, files in os.walk("css"):
        for name in files:
            if name.endswith(".css"):
                refs.extend(css_refs(os.path.join(root, name)))

    refs = sorted(set(refs))
    if not refs:
        print("check-local-assets: 参照が0件（index.html がまだ無い）")
        return 0

    missing = [ref for ref in refs if not os.path.exists(ref)]
    excluded = sorted(ignored([ref for ref in refs if os.path.exists(ref)]))

    for ref in missing:
        print(f"存在しない: {ref}", file=sys.stderr)
    for ref in excluded:
        print(f"gitignore で除外されている（公開サイトでだけ404になる）: {ref}", file=sys.stderr)

    if missing or excluded:
        print("", file=sys.stderr)
        print("fix: パスを直すか、.gitignore の許可リストに戻す。", file=sys.stderr)
        return 1

    print(f"check-local-assets: {len(refs)} 件すべて実在し、追跡対象")
    return 0


if __name__ == "__main__":
    sys.exit(main())
