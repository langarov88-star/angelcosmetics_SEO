#!/usr/bin/env python3
"""
Generate proper XML sitemaps with hreflang (bg / en) for angelcosmetics.bg
Input:  seo/sitemaps/sitemap 1.txt
        seo/sitemaps/sitemap 2.txt
Output: seo/sitemaps/output/sitemap-index.xml
        seo/sitemaps/output/sitemap-products.xml
        seo/sitemaps/output/sitemap-categories.xml
        seo/sitemaps/output/sitemap-static.xml
        seo/sitemaps/output/sitemap-bg-only.xml   (BG products without EN version)
"""

import re
import os
from collections import defaultdict
from datetime import date

BASE_URL = "https://angelcosmetics.bg"
TODAY = date.today().isoformat()
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

# ─── XML helpers ─────────────────────────────────────────────────────────────

SITEMAP_NS = (
    'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    '  xmlns:xhtml="http://www.w3.org/1999/xhtml"'
)

def hreflang_block(bg_url, en_url):
    """Returns the two <xhtml:link> alternate tags."""
    lines = []
    if bg_url:
        lines.append(f'    <xhtml:link rel="alternate" hreflang="bg" href="{bg_url}"/>')
    if en_url:
        lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>')
    return "\n".join(lines)

def url_entry(loc, bg_url=None, en_url=None, changefreq="weekly", priority="0.8"):
    parts = [
        "  <url>",
        f"    <loc>{loc}</loc>",
        f"    <lastmod>{TODAY}</lastmod>",
        f"    <changefreq>{changefreq}</changefreq>",
        f"    <priority>{priority}</priority>",
    ]
    if bg_url or en_url:
        parts.append(hreflang_block(bg_url, en_url))
    parts.append("  </url>")
    return "\n".join(parts)

def write_sitemap(filepath, url_blocks):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(f'<urlset {SITEMAP_NS}>\n\n')
        f.write("\n\n".join(url_blocks))
        f.write("\n\n</urlset>\n")
    print(f"  Written: {os.path.basename(filepath)} ({len(url_blocks):,} URLs)")

def write_sitemap_index(filepath, sitemap_files):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n\n')
        for fname in sitemap_files:
            f.write("  <sitemap>\n")
            f.write(f"    <loc>{BASE_URL}/sitemaps/{fname}</loc>\n")
            f.write(f"    <lastmod>{TODAY}</lastmod>\n")
            f.write("  </sitemap>\n\n")
        f.write("</sitemapindex>\n")
    print(f"  Written: {os.path.basename(filepath)}")

# ─── Parsers ─────────────────────────────────────────────────────────────────

PRODUCT_BG_RE = re.compile(r'https://angelcosmetics\.bg/product/(\d+)/[^<\s]+\.html')
PRODUCT_EN_RE = re.compile(r'https://angelcosmetics\.bg/en/product/(\d+)/[^<\s]+\.html')
CATEGORY_BG_RE = re.compile(r'https://angelcosmetics\.bg/category/(\d+)/[^<\s]+\.html')
CATEGORY_EN_RE = re.compile(r'https://angelcosmetics\.bg/en/category/(\d+)/[^<\s]+\.html')
STATIC_BG_RE = re.compile(r'https://angelcosmetics\.bg/page/\d+/[^<\s]+\.html')
STATIC_EN_RE = re.compile(r'https://angelcosmetics\.bg/en/page/\d+/[^<\s]+\.html')

def parse_sitemaps(*paths):
    products_bg = {}   # id -> url
    products_en = {}
    categories_bg = {}
    categories_en = {}
    statics_bg = set()
    statics_en = set()

    for path in paths:
        with open(path, encoding="utf-8") as f:
            content = f.read()

        for m in PRODUCT_BG_RE.finditer(content):
            pid = m.group(1)
            if pid not in products_bg:          # keep first occurrence
                products_bg[pid] = m.group(0)

        for m in PRODUCT_EN_RE.finditer(content):
            pid = m.group(1)
            if pid not in products_en:
                products_en[pid] = m.group(0)

        for m in CATEGORY_BG_RE.finditer(content):
            cid = m.group(1)
            if cid not in categories_bg:
                categories_bg[cid] = m.group(0)

        for m in CATEGORY_EN_RE.finditer(content):
            cid = m.group(1)
            if cid not in categories_en:
                categories_en[cid] = m.group(0)

        statics_bg.update(STATIC_BG_RE.findall(content))
        statics_en.update(STATIC_EN_RE.findall(content))

    return products_bg, products_en, categories_bg, categories_en, statics_bg, statics_en

# ─── Builders ────────────────────────────────────────────────────────────────

def build_product_blocks(products_bg, products_en):
    """Paired products (BG+EN) and BG-only."""
    paired = []
    bg_only = []

    all_ids = sorted(set(products_bg) | set(products_en), key=int)

    for pid in all_ids:
        bg_url = products_bg.get(pid)
        en_url = products_en.get(pid)

        if bg_url and en_url:
            # BG entry
            paired.append(url_entry(bg_url, bg_url=bg_url, en_url=en_url,
                                     changefreq="weekly", priority="0.8"))
            # EN entry
            paired.append(url_entry(en_url, bg_url=bg_url, en_url=en_url,
                                     changefreq="weekly", priority="0.8"))
        elif bg_url:
            # BG-only — no EN version exists
            bg_only.append(url_entry(bg_url, bg_url=bg_url,
                                      changefreq="weekly", priority="0.6"))
        # EN-only products (shouldn't exist per our analysis but handle gracefully)
        elif en_url:
            paired.append(url_entry(en_url, en_url=en_url,
                                     changefreq="weekly", priority="0.6"))

    return paired, bg_only

def build_category_blocks(categories_bg, categories_en):
    all_ids = sorted(set(categories_bg) | set(categories_en), key=int)
    blocks = []

    for cid in all_ids:
        bg_url = categories_bg.get(cid)
        en_url = categories_en.get(cid)

        if bg_url:
            blocks.append(url_entry(bg_url, bg_url=bg_url, en_url=en_url,
                                     changefreq="daily", priority="0.9"))
        if en_url:
            blocks.append(url_entry(en_url, bg_url=bg_url, en_url=en_url,
                                     changefreq="daily", priority="0.9"))

    return blocks

def build_static_blocks(statics_bg, statics_en):
    """Match static pages by slug (last path segment)."""
    bg_by_slug = {u.rsplit("/", 1)[-1]: u for u in statics_bg}
    en_by_slug = {u.rsplit("/", 1)[-1]: u for u in statics_en}

    all_slugs = sorted(set(bg_by_slug) | set(en_by_slug))
    blocks = []

    for slug in all_slugs:
        bg_url = bg_by_slug.get(slug)
        en_url = en_by_slug.get(slug)

        if bg_url:
            blocks.append(url_entry(bg_url, bg_url=bg_url, en_url=en_url,
                                     changefreq="monthly", priority="0.5"))
        if en_url:
            blocks.append(url_entry(en_url, bg_url=bg_url, en_url=en_url,
                                     changefreq="monthly", priority="0.5"))

    return blocks

# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    script_dir = os.path.dirname(__file__)
    sm1 = os.path.join(script_dir, "sitemap 1.txt")
    sm2 = os.path.join(script_dir, "sitemap 2.txt")

    print("Parsing sitemaps...")
    products_bg, products_en, categories_bg, categories_en, statics_bg, statics_en = \
        parse_sitemaps(sm1, sm2)

    print(f"  BG products:   {len(products_bg):,}")
    print(f"  EN products:   {len(products_en):,}")
    print(f"  BG categories: {len(categories_bg):,}")
    print(f"  EN categories: {len(categories_en):,}")
    print(f"  BG static pages: {len(statics_bg)}")
    print(f"  EN static pages: {len(statics_en)}")

    print("\nBuilding sitemap blocks...")
    product_blocks, bg_only_blocks = build_product_blocks(products_bg, products_en)
    category_blocks = build_category_blocks(categories_bg, categories_en)
    static_blocks = build_static_blocks(statics_bg, statics_en)

    print(f"  Product URL entries (paired):  {len(product_blocks):,}")
    print(f"  BG-only product entries:       {len(bg_only_blocks):,}")
    print(f"  Category URL entries:          {len(category_blocks):,}")
    print(f"  Static page entries:           {len(static_blocks):,}")

    print("\nWriting files...")
    out = OUTPUT_DIR

    write_sitemap(f"{out}/sitemap-products.xml", product_blocks)
    write_sitemap(f"{out}/sitemap-categories.xml", category_blocks)
    write_sitemap(f"{out}/sitemap-static.xml", static_blocks)

    if bg_only_blocks:
        write_sitemap(f"{out}/sitemap-bg-only.xml", bg_only_blocks)

    sitemap_files = ["sitemap-products.xml", "sitemap-categories.xml", "sitemap-static.xml"]
    if bg_only_blocks:
        sitemap_files.append("sitemap-bg-only.xml")

    write_sitemap_index(f"{out}/sitemap-index.xml", sitemap_files)

    print(f"\nDone. Total URL entries: "
          f"{len(product_blocks) + len(bg_only_blocks) + len(category_blocks) + len(static_blocks):,}")
    print(f"Output: {out}/")

if __name__ == "__main__":
    main()
