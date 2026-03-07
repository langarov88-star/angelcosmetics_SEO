# Sitemap Strategy — angelcosmetics.bg

## Принцип

XML Sitemap = списък с URLs, КОТОРЫЕ искаме Google да индексира.
Ако URL е в sitemap → изпращаме сигнал: "Индексирай това."
Ако URL е noindex → НЕ трябва да е в sitemap.
Противоречие (noindex + sitemap) → confusing signal за Google.

---

## Какво ВЛИЗА в Sitemap

| Page Type | Включва ли се | Условие |
|-----------|-------------|---------|
| Home | ✅ Да | Винаги |
| Main Category pages | ✅ Да | Всички |
| Subcategory pages | ✅ Да | Само INDEX pages (≥10 products + content) |
| Brand pages | ✅ Да | Само с editorial content |
| Series pages | ✅ Да | Само INDEX series |
| Problem pages | ✅ Да | Всички публикувани |
| Ingredient pages | ✅ Да | Само с ≥200 думи |
| Product pages (active) | ✅ Да | Само active + in stock или временно OOS |
| Blog articles | ✅ Да | Всички публикувани |
| Routine pages | ✅ Да | Всички публикувани |

---

## Какво НЕ ВЛИЗА в Sitemap

| Page Type | Причина |
|-----------|---------|
| Filter URLs | Noindex |
| Sort URLs | Noindex |
| Search pages (/search?q=) | Noindex |
| Pagination (page 2+) | Noindex |
| Cart / Checkout / Account | Noindex |
| Wishlist | Noindex |
| Thin subcategories (<10 products) | Noindex |
| Brand pages без editorial content | Noindex |
| Discontinued products (301 redirect) | Не съществуват |
| Tag pages (ако са noindex) | Noindex |

---

## Sitemap Structure

Препоръчваме sitemap index с multiple sitemaps за по-добро crawl management:

```xml
sitemap_index.xml
  → sitemap-pages.xml        (Home, categories, problem, ingredient, routine)
  → sitemap-brands.xml       (Brand + series pages)
  → sitemap-products.xml     (Product pages — auto-generated от Summer Cart)
  → sitemap-blog.xml         (Blog articles)
```

**[PLATFORM CHECK]** Верифицирай как Summer Cart генерира sitemap-а. Ако е auto-generated:
- Провери дали изключва noindex pages
- Провери дали включва filter URLs (трябва да НЕ ги включва)
- Ако включва нежелани URLs → custom sitemap или custom exclusion rules

---

## Sitemap Submission

- Submit в Google Search Console: https://search.google.com/search-console
- Submit в Bing Webmaster Tools
- Достъп: `https://www.angelcosmetics.bg/sitemap.xml`
- Cloudflare: Ensure sitemap URL не е блокирана и се кешира 1 час

---

## Sitemap Maintenance

| Кога | Действие |
|------|---------|
| При нова страница (INDEX) | Добави в sitemap |
| При noindex на страница | Премахни от sitemap |
| При 301 redirect | Добави new URL, премахни old URL |
| При discontinued product | Премахни от sitemap |
| Monthly | Провери дали sitemap достъпен (HTTP 200) |
| Quarterly | Проверка GSC → Sitemaps за errors |

---

## Sitemap Priority и Changefreq

**Честа грешка:** Слагане на priority="1.0" и changefreq="daily" на всичко.
Google почти напълно игнорира тези hints. Ползвай само ако имаш специфична причина.

Ако Summer Cart генерира defaults:
- Не е критично да ги промениш
- Фокусирай се на правилните URLs в sitemap-а, не на priority/changefreq
