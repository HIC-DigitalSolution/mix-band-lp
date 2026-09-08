// Sass だけをコンパイルする。
//
// **index.html は生成しません。**手で書いて、そのまま読めるようにしてあります
// （2026-09-08 の依頼者の指示。harness/contracts/mix-lp.yaml の
//  index-html-is-written-by-hand / styles-are-per-section-sass）。
//
// スタイルはセクションごとに src/scss/sections/_<名前>.scss に分け、
// src/scss/style.scss が @use でまとめて、css/style.css に1枚で吐きます。
import { writeFile, mkdir, readdir, stat } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { compile } from 'sass';

const root = new URL('../', import.meta.url);
const file = (path) => new URL(path, root);

async function build() {
  const { css } = compile(fileURLToPath(file('src/scss/style.scss')), { style: 'expanded' });
  await mkdir(file('css/'), { recursive: true });
  await writeFile(
    file('css/style.css'),
    `/* Generated from src/scss/style.scss. Do not edit directly. */\n${css}\n`,
  );
  console.log('Built css/style.css');
}

async function fingerprint(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const parts = [];
  for (const entry of entries.sort((a, b) => a.name.localeCompare(b.name))) {
    const url = new URL(entry.name + (entry.isDirectory() ? '/' : ''), directory);
    if (entry.isDirectory()) parts.push(await fingerprint(url));
    else {
      const info = await stat(url);
      parts.push(`${url.pathname}:${info.mtimeMs}:${info.size}`);
    }
  }
  return parts.join('\n');
}

await build();
if (process.argv.includes('--watch')) {
  let previous = await fingerprint(file('src/scss/'));
  console.log('Watching src/scss/ — Ctrl+C to stop');
  // 再帰watchがEMFILEになる環境でも使えるよう、500ms間隔で変更を確認する。
  async function poll() {
    try {
      const next = await fingerprint(file('src/scss/'));
      if (next !== previous) {
        previous = next;
        await build();
      }
    } catch (error) {
      console.error(error.message);
    } finally {
      setTimeout(poll, 500);
    }
  }
  setTimeout(poll, 500);
}
