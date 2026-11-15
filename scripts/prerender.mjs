// Inject the server-rendered homepage into dist/index.html after `vite build`.
import { readFileSync, writeFileSync, rmSync } from 'node:fs';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const root = resolve(import.meta.dirname, '..');
const { render } = await import(pathToFileURL(resolve(root, 'dist-ssr/entry-server.js')).href);
const file = resolve(root, 'dist/index.html');
const html = readFileSync(file, 'utf8');
const marker = '<div id="root"></div>';
if (!html.includes(marker)) throw new Error('root marker not found in dist/index.html');
writeFileSync(file, html.replace(marker, `<div id="root">${render()}</div>`));
rmSync(resolve(root, 'dist-ssr'), { recursive: true, force: true });
console.log('Prerendered homepage into dist/index.html');
