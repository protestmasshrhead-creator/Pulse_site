#!/usr/bin/env python3
"""Собрать sitemap.xml и robots.txt по готовым страницам сайта.

Запускать из корня репозитория после пересборки языковых версий:

    python3 _i18n/tools/sitemap.py

Обходит все каталоги с index.html, кроме служебных (.git, _i18n).
"""
import os

SITE = 'https://pulse-call.com'
SKIP = {'.git', '_i18n', 'node_modules'}


def pages(root):
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP]
        if 'index.html' in filenames:
            rel = os.path.relpath(dirpath, root)
            found.append('/' if rel == '.' else '/' + rel.replace(os.sep, '/') + '/')
    return sorted(found, key=lambda u: (u.count('/'), u))


def main():
    root = os.getcwd()
    urls = pages(root)

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    lines += ['  <url><loc>%s%s</loc></url>' % (SITE, u) for u in urls]
    lines.append('</urlset>')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write('User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % SITE)

    print('sitemap.xml: %d URL' % len(urls))


if __name__ == '__main__':
    main()
