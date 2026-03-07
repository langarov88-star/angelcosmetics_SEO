# Indexing Rules — angelcosmetics.bg

## Принцип

Индексираме само pages, които:
1. Имат уникално, substantive съдържание
2. Таргетират конкретен keyword с ясен search intent
3. Имат поне 1 inbound internal link
4. НЕ създават keyword cannibalization с друга indexed страница

---

## Master Index/Noindex Matrix

| Page Type | Решение | Условие за INDEX | Условие за NOINDEX |
|-----------|---------|------------------|--------------------|
| Home | **INDEX** | Винаги | — |
| Main Category | **INDEX** | Винаги | — |
| Subcategory | **INDEX** | ≥10 products + уникало описание (150+ думи) | <10 products ИЛИ без описание |
| Brand Page | **INDEX** | Има editorial content (250+ думи) | Само product grid, без описание |
| Series Page | **INDEX** | ≥3 products + описание (200+ думи) | <3 products ИЛИ без описание |
| Problem/Concern Page | **INDEX** | Има content (600+ думи) | Без substantive content |
| Ingredient Page | **INDEX** | ≥200 думи оригинален текст | Под прага или duplicate от друга страница |
| Product Page (active) | **INDEX** | Продуктът е наличен | — |
| Product Page (temp. изчерпан) | **INDEX** + canonical | Очаква се да се върне | — |
| Product Page (discontinued) | **301 redirect** | — | Спрян завинаги → redirect към category |
| Blog Article | **INDEX** | ≥600 думи, оригинален content | Duplicate, thin, или syndicated без добавена стойност |
| Routine/Solution Page | **INDEX** | Curated editorial content | Автоматично генерирана без editorial |
| Search Results Page | **NOINDEX** | Никога | Винаги noindex |
| Filter URLs | **NOINDEX** | Само ако имат HIGH search volume И нямаме dedicated page | Винаги noindex по default |
| Sort URLs | **NOINDEX** | Никога | Винаги noindex |
| Pagination (page 2+) | **NOINDEX** | — | Всички pagination pages |
| Tag Pages | **NOINDEX** | — | Ако не са editorial |
| Cart/Checkout/Account | **NOINDEX** | — | Винаги noindex |
| Wishlist | **NOINDEX** | — | Винаги noindex |

---

## Специални случаи

### Изчерпани продукти

```
Временно изчерпан (очаква се да се върне):
  → Запази INDEX
  → Добави "временно изчерпан" UI message
  → НЕ маха от sitemap
  → НЕ слагай 301 redirect

Permanent discontinued (спрян завинаги):
  → 301 redirect към:
     1. Близък заместителен продукт (предпочитано)
     2. Серията страница
     3. Brand страницата
     4. Category страницата
  → Добави в redirects-master.csv
```

### Filter URLs — Изключения

По default: всички filter URLs → NOINDEX

Може да се индексира само ако:
- Комбинацията има документиран search volume (>500 monthly searches)
- НЕ съществува dedicated page за тази комбинация
- Съдържа поне 20 products
- Одобрено от SEO Manager с документация

Пример: `/face-care/?brand=the-ordinary` може да се индексира АКО нямаме `/brands/the-ordinary/` page. АКО имаме → NOINDEX + canonical към brand page.

### Subcategory Edge Cases

```
Subcategory с 5-9 products:
  → По default NOINDEX
  → Изключение: Ако subcategory-та е high search volume и
    продуктите са много специфични (напр. /face-care/face-oils/)
  → Решение изисква SEO Manager одобрение

Subcategory с >10 products но без описание:
  → ВРЕМЕННО noindex
  → Добави в TODO list за content
  → INDEX след добавяне на описание
```

---

## Как се прилага Noindex в Summer Cart

### Option 1: Native meta robots tag (ако платформата поддържа)
```html
<meta name="robots" content="noindex, follow">
```

### Option 2: HTTP Header чрез Cloudflare Worker (ако native не е налично)
```
X-Robots-Tag: noindex, follow
```

### Option 3: Robots.txt (за URL patterns — не за individual pages)
```
# В robots.txt
Disallow: /search
Disallow: /search?*
User-agent: *
Disallow: /*?sort=*
Disallow: /*?filter=*
```

**[CUSTOM DEV]** Верифицирай кой метод е приложим за Summer Cart конфигурацията.

---

## Sitemap Rules

Sitemap ТРЯБВА да съдържа само INDEX pages.

Никога в sitemap:
- Noindex pages
- Filter/sort/search URLs
- Pagination pages (page 2+)
- 301 redirect destinations ако source е вече индексирана → само destination
- Pages с canonical към различна URL

Проверяй sitemap на: https://search.google.com/search-console
