# URL Taxonomy — angelcosmetics.bg

> Последна актуализация: 2026-03-10
> Автор: SEO Team

Този документ е **master reference** за пълната URL архитектура на angelcosmetics.bg.
Покрива всички page types, техните URL patterns, indexing статус и content изисквания.

**Свързани документи:**
- Правила за slug формат → [`/seo/rules/url-naming-conventions.md`](../rules/url-naming-conventions.md)
- Категорийна структура → [`/seo/taxonomy/category-taxonomy.md`](category-taxonomy.md)
- Keyword allocation → [`/seo/taxonomy/keyword-map.md`](keyword-map.md)
- Redirects → [`/seo/redirects/redirects-master.csv`](../redirects/redirects-master.csv)

---

## 1. URL Архитектура — Обзор

```
angelcosmetics.bg/
│
├── [Product Categories]
│   ├── /face-care/
│   ├── /body-care/
│   ├── /hair-care/
│   ├── /sun-care/
│   ├── /makeup/
│   └── /perfumes/ | /baby-care/ | /mens-care/
│
├── [Brand Hub]
│   └── /brands/{brand-slug}/
│       └── /brands/{brand-slug}/{series-slug}/
│
├── [Editorial / Discovery]
│   ├── /skin-concerns/{concern-slug}/
│   ├── /hair-concerns/{concern-slug}/
│   ├── /ingredients/{ingredient-slug}/
│   └── /routines/{routine-slug}/
│
├── [Blog]
│   └── /blog/{article-slug}/
│
└── [Utility — NOINDEX]
    ├── /search
    ├── /cart/
    ├── /checkout/
    ├── /account/
    ├── /wishlist/
    └── /*?filter=* | *?sort=* | *?page=* | ...
```

**Максимална URL дълбочина: 4 нива** (tier1/tier2/tier3/product/)

---

## 2. Page Types — Пълна Таблица

| Page Type | URL Pattern | Индексиране | Приоритет в Sitemap |
|-----------|-------------|-------------|---------------------|
| Home | `/` | ✅ INDEX | 1.0 |
| Main Category | `/{category}/` | ✅ INDEX | 0.9 |
| Subcategory | `/{category}/{subcategory}/` | ✅ INDEX (ако ≥10 products + описание) | 0.8 |
| Product | `/{category}/{subcategory}/{product-slug}/` | ✅ INDEX | 0.7 |
| Brand Hub | `/brands/{brand-slug}/` | ✅ INDEX (с editorial content) | 0.8 |
| Brand Series | `/brands/{brand-slug}/{series-slug}/` | ✅ INDEX (ако ≥5 products) | 0.6 |
| Skin Concern | `/skin-concerns/{concern-slug}/` | ✅ INDEX | 0.8 |
| Hair Concern | `/hair-concerns/{concern-slug}/` | ✅ INDEX | 0.8 |
| Ingredient | `/ingredients/{ingredient-slug}/` | ✅ INDEX | 0.7 |
| Routine | `/routines/{routine-slug}/` | ✅ INDEX | 0.6 |
| Blog Article | `/blog/{article-slug}/` | ✅ INDEX | 0.6 |
| Blog Index | `/blog/` | ✅ INDEX | 0.7 |
| Concerns Index | `/skin-concerns/` | ✅ INDEX | 0.7 |
| Ingredients Index | `/ingredients/` | ✅ INDEX | 0.7 |
| Search Results | `/search` | ❌ NOINDEX | — |
| Filter/Sort URLs | `/*?filter=*`, `/*?sort=*` | ❌ NOINDEX | — |
| Pagination | `/*?page=*` | ❌ NOINDEX | — |
| Cart / Checkout | `/cart/`, `/checkout/` | ❌ NOINDEX | — |
| Account / Wishlist | `/account/`, `/wishlist/` | ❌ NOINDEX | — |
| UTM / Tracking | `/*?utm_*`, `/*?ref=*` | ❌ NOINDEX | — |

---

## 3. URL Patterns — Детайлно по Тип

### 3.1 Product Pages

```
Pattern:  /{category-slug}/{subcategory-slug}/{product-slug}/
Alt:      /{category-slug}/{product-slug}/         (ако subcategory не участва в URL)

Примери:
  /face-care/serums/la-roche-posay-effaclar-duo-plus-40ml/
  /face-care/moisturizers/cerave-moisturizing-cream-340ml/
  /hair-care/shampoos/kerastase-bain-satin-1-250ml/
  /sun-care/body-spf/la-roche-posay-anthelios-spf50-200ml/
```

**Slug включва:** brand + product name + size (ако има размери)
**Canonical:** self-referencing canonical на всяка product page

---

### 3.2 Category Pages

```
Tier 1 — Main Category:
  /{category-slug}/

  /face-care/
  /body-care/
  /hair-care/
  /sun-care/
  /makeup/
  /perfumes/
  /baby-care/
  /mens-care/

Tier 2 — Subcategory:
  /{category-slug}/{subcategory-slug}/

  /face-care/cleansers/
  /face-care/serums/
  /face-care/moisturizers/
  /face-care/eye-care/
  /face-care/face-masks/
  /face-care/exfoliants/
  /face-care/face-oils/
  /face-care/acne-treatments/
  /face-care/toners/

  /body-care/body-lotions/
  /body-care/body-scrubs/
  /body-care/hand-care/
  /body-care/deodorants/

  /hair-care/shampoos/
  /hair-care/conditioners/
  /hair-care/hair-masks/
  /hair-care/scalp-care/
  /hair-care/styling/

  /sun-care/face-spf/
  /sun-care/body-spf/

  /makeup/foundation/
  /makeup/eyes/
  /makeup/lips/
  /makeup/removal/
```

**Indexing threshold:** ≥10 products + editorial описание (≥100 думи) → INDEX

---

### 3.3 Brand Pages

```
Brand Hub:
  /brands/{brand-slug}/

  /brands/la-roche-posay/
  /brands/cerave/
  /brands/the-ordinary/
  /brands/vichy/
  /brands/kerastase/
  /brands/loreal/

Brand Series:
  /brands/{brand-slug}/{series-slug}/

  /brands/la-roche-posay/effaclar/
  /brands/la-roche-posay/cicaplast/
  /brands/la-roche-posay/toleriane/
  /brands/cerave/moisturizing-range/
```

**Изисквания за INDEX:** editorial content ≥250 думи + ≥5 products
**Без editorial content → NOINDEX до добавяне на copy**

---

### 3.4 Problem / Concern Pages

```
Skin Concerns:
  /skin-concerns/{concern-slug}/

  /skin-concerns/dry-skin/
  /skin-concerns/acne-prone-skin/
  /skin-concerns/anti-aging/
  /skin-concerns/sensitive-skin/
  /skin-concerns/oily-skin/
  /skin-concerns/hyperpigmentation/
  /skin-concerns/rosacea/
  /skin-concerns/eczema/
  /skin-concerns/dark-circles/
  /skin-concerns/large-pores/

Hair Concerns:
  /hair-concerns/{concern-slug}/

  /hair-concerns/hair-loss/
  /hair-concerns/dry-hair/
  /hair-concerns/oily-scalp/
  /hair-concerns/damaged-hair/
  /hair-concerns/dandruff/

Concerns Index:
  /skin-concerns/
  /hair-concerns/
```

**Минимален content:** 500+ думи, definition + causes + ingredients + products + FAQ

---

### 3.5 Ingredient Pages

```
Pattern:  /ingredients/{ingredient-slug}/

  /ingredients/hyaluronic-acid/
  /ingredients/retinol/
  /ingredients/niacinamide/
  /ingredients/vitamin-c/
  /ingredients/salicylic-acid/
  /ingredients/ceramides/
  /ingredients/aha-bha/
  /ingredients/peptides/
  /ingredients/azelaic-acid/

Index:
  /ingredients/
```

**Минимален content:** 300+ думи, какво прави + за кого е + продукти с него

---

### 3.6 Routine Pages

```
Pattern:  /routines/{routine-slug}/

  /routines/anti-aging-morning-routine/
  /routines/acne-routine-for-beginners/
  /routines/dry-skin-evening-routine/
  /routines/spf-daily-routine/
  /routines/sensitive-skin-routine/
```

**Цел:** middle-funnel, commercial intent + internal links към products

---

### 3.7 Blog Pages

```
Blog Index:
  /blog/

Blog Article:
  /blog/{article-slug}/

  /blog/how-to-build-a-skincare-routine/
  /blog/retinol-beginners-guide/
  /blog/best-spf-for-oily-skin/
  /blog/cerave-vs-la-roche-posay/
```

---

## 4. Canonical Strategy

| Ситуация | Canonical |
|----------|-----------|
| Нормална страница | Self-referencing (`<link rel="canonical" href="URL на страницата/">`) |
| Filter/Sort variant | Canonical → parent category URL |
| Product с варианти (размер/цвят) | Canonical → основната product URL |
| Pagination (`?page=2`) | Canonical → page 1 ИЛИ noindex |
| Duplicate brand page | Canonical → preferred URL |

**Canonical файл:** [`/seo/rules/canonical-rules.md`](../rules/canonical-rules.md)

---

## 5. Забранени URL Patterns

Следните URL patterns са блокирани в `robots.txt` и получават `noindex`:

```
/search
/cart/
/checkout/
/account/
/wishlist/
/admin/
/*?q=*
/*?sort=*
/*?order=*
/*?filter=*
/*?page=*
/*?ref=*
/*?utm_*
```

**Robots.txt файл:** [`/seo/rules/indexing-rules.md`](../rules/indexing-rules.md)

---

## 6. Internal Linking Логика

Всяка page type трябва да сочи към:

| Page Type | Links TO |
|-----------|----------|
| Product page | Brand hub, Category, 2-3 свързани products, Ingredient pages |
| Category page | Subcategories, Top products, Related concerns |
| Brand page | Brand series, Top products, Related categories |
| Concern page | Ingredient pages, Product pages (6-12), Related concerns, Blog |
| Ingredient page | Concern pages, Product pages с тази съставка |
| Blog article | Product pages, Category, Concern or Ingredient pages |

**Linking matrix:** [`/seo/internal-links/linking-matrix.md`](../internal-links/linking-matrix.md)

---

## 7. Процес при Промяна на URL

> ⚠️ Никога не сменяй URL без да следваш целия процес:

```
1. Добави 301 redirect → /seo/redirects/redirects-master.csv
2. PR review и одобрение от SEO Manager
3. Import redirect в Cloudflare ПРЕДИ смяна на URL
4. Смени URL в Summer Cart
5. Провери: curl -I https://angelcosmetics.bg/old-url/  → трябва 301
6. Обнови sitemap
7. Обнови internal links към стария URL
8. Документирай в docs/changelog.md
```

---

## 8. Нови URL Типове — Checklist

При добавяне на нов page type или нова страница:

- [ ] URL следва конвенциите в `url-naming-conventions.md`
- [ ] Добавена е в `keyword-map.md` с primary keyword
- [ ] Добавена е в sitemap (ако INDEX)
- [ ] Canonical tag е имплементиран
- [ ] Internal links от поне 3 свързани pages
- [ ] Category taxonomy е обновен (ако е category)
- [ ] Brand list е обновен (ако е brand)
- [ ] Changelog е обновен

---

*За въпроси → виж `docs/seo-strategy-overview.md` или отвори GitHub Issue.*
