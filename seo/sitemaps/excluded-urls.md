# Excluded URLs — angelcosmetics.bg

## Цел

Документация на URL patterns, КОТОРЫЕ трябва да са:
1. Noindex (или)
2. Блокирани в robots.txt (или)
3. Изключени от sitemap

---

## Robots.txt Disallow Patterns

Добави в `/robots.txt` на Summer Cart:

```
User-agent: *
Disallow: /search
Disallow: /search/
Disallow: /*?q=*
Disallow: /*?sort=*
Disallow: /*?order=*
Disallow: /*?filter=*
Disallow: /*?page=*
Disallow: /*?ref=*
Disallow: /cart/
Disallow: /checkout/
Disallow: /account/
Disallow: /my-account/
Disallow: /wishlist/
Disallow: /admin/
Disallow: /wp-admin/

# Allow sitemaps and important files
Allow: /sitemap.xml
Allow: /sitemap_index.xml
Allow: /robots.txt

# Sitemap location
Sitemap: https://www.angelcosmetics.bg/sitemap.xml
```

**[ACTION REQUIRED]** Верифицирай с developer точните URL patterns, генерирани от Summer Cart.
Особено важно: query параметрите за sort и filter може да са различни от горните.

---

## URL Patterns → Noindex (не robots.txt, а meta noindex)

Следните page types изискват `<meta name="robots" content="noindex, follow">`:

| Pattern | Пример | Метод |
|---------|--------|-------|
| Pagination | `/face-care/page/2/` | Meta noindex |
| Thin categories | `/makeup/concealer/` (ако <10 products) | Meta noindex + canonical |
| Brand pages без editorial | `/brands/small-brand/` | Meta noindex |
| Thin series | `/brands/brand/tiny-series/` | Meta noindex |
| User account pages | `/account/orders/` | Meta noindex |

---

## Известни Проблемни URL Patterns

Документирай тук конкретни URL patterns, открити при crawl audit:

| URL Pattern | Проблем | Решение | Статус |
|-------------|---------|---------|--------|
| _[Попълни след crawl audit]_ | | | |
| _[Например: /products/?brand=X&sort=Y]_ | Filter + sort combo | Noindex + canonical | Pending |

---

## Crawl Audit Schedule

| Период | Инструмент | Цел |
|--------|-----------|-----|
| Month 1 | Screaming Frog full crawl | Baseline — намери всички indexed URLs |
| Month 3 | Screaming Frog | Провери дали noindex е приложен |
| Quarterly | Screaming Frog + GSC | Ongoing monitoring |

---

## Google Search Console Monitoring

В GSC → Coverage → Провери:
- "Valid" pages — трябва да са само желаните indexed pages
- "Excluded — noindex" — трябва да са filter/sort/search pages
- "Crawled — not indexed" — проучи защо Google не ги индексира
- "Excluded — robots.txt" — провери дали правилните patterns са блокирани
