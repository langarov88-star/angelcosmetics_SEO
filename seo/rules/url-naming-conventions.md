# URL Naming Conventions — angelcosmetics.bg

## Core Rules

1. **Само lowercase** — без главни букви
2. **Само дефиси** като разделители — без underscores, без spaces, без точки
3. **Без специални символи** — без &, %, #, ? в slug
4. **Без стоп думи** в slug (a, the, и, на, за) — изключение само ако е необходимо за смисъл
5. **Максимална дълбочина: 4 нива** — `/tier1/tier2/tier3/slug/`
6. **Trailing slash** — винаги (консистентност)
7. **English slugs** за категории, брандове, съставки — по-добра международна compat и по-прости URL-и
8. **Описателен, не ID-базиран** — `/face-care/serums/cerave-hydrating-serum/` не `/products/12345/`

---

## URL шаблони по page type

```
Home:
  /

Main Category:
  /{category-slug}/
  Примери:
    /face-care/
    /hair-care/
    /body-care/
    /sun-care/
    /makeup/

Subcategory:
  /{category-slug}/{subcategory-slug}/
  Примери:
    /face-care/serums/
    /face-care/moisturizers/
    /hair-care/shampoos/
    /body-care/body-lotions/

Brand:
  /brands/{brand-slug}/
  Примери:
    /brands/la-roche-posay/
    /brands/cerave/
    /brands/the-ordinary/
    /brands/vichy/

Series:
  /brands/{brand-slug}/{series-slug}/
  Примери:
    /brands/la-roche-posay/effaclar/
    /brands/la-roche-posay/cicaplast/
    /brands/cerave/moisturizing-range/

Problem/Concern:
  /skin-concerns/{concern-slug}/      (за лице)
  /hair-concerns/{concern-slug}/      (за коса)
  Примери:
    /skin-concerns/dry-skin/
    /skin-concerns/acne-prone-skin/
    /skin-concerns/anti-aging/
    /hair-concerns/hair-loss/
    /hair-concerns/dry-hair/

Ingredient:
  /ingredients/{ingredient-slug}/
  Примери:
    /ingredients/hyaluronic-acid/
    /ingredients/retinol/
    /ingredients/niacinamide/
    /ingredients/vitamin-c/
    /ingredients/salicylic-acid/

Product:
  /{category-slug}/{subcategory-slug}/{product-slug}/
  ИЛИ (ако subcategory не е в URL):
  /{category-slug}/{product-slug}/
  Примери:
    /face-care/serums/la-roche-posay-effaclar-duo-plus-40ml/
    /face-care/moisturizers/cerave-moisturizing-cream-340ml/

Blog Article:
  /blog/{article-slug}/
  Примери:
    /blog/how-to-build-a-skincare-routine/
    /blog/retinol-beginners-guide/
    /blog/best-spf-for-oily-skin/

Routine/Solution:
  /routines/{routine-slug}/
  Примери:
    /routines/anti-aging-morning-routine/
    /routines/acne-routine-for-beginners/
    /routines/dry-skin-evening-routine/
```

---

## Slug Формат за Brand Names

| Brand | Slug |
|-------|------|
| La Roche-Posay | `la-roche-posay` |
| The Ordinary | `the-ordinary` |
| Kérastase | `kerastase` |
| L'Oréal | `loreal` |
| Eau Thermale Avène | `avene` |
| CeraVe | `cerave` |
| Dr. Jart+ | `dr-jart` |
| COSRX | `cosrx` |

**Правило:** Специални символи (é, ô, +, ') → премахват се или се транслитерират. Дефис в бранд → запазва се.

---

## Slug Формат за Product Names

```
Пълно product name → slug:
  "La Roche-Posay Effaclar Duo+ 40ml" → "la-roche-posay-effaclar-duo-plus-40ml"
  "CeraVe Moisturizing Cream 340g" → "cerave-moisturizing-cream-340g"
  "The Ordinary Niacinamide 10% + Zinc 1%" → "the-ordinary-niacinamide-10-zinc-1"

Включвай в slug:
  ✅ Brand name (за SEO — помага при branded searches)
  ✅ Product name
  ✅ Size/volume (ако има варианти по размер)

Изключвай от slug:
  ❌ Специални символи (%, +, /)
  ❌ Артикли (a, the, и, на)
  ❌ Trailing numbers без смисъл
```

---

## Забранени URL Patterns (никога индексирани)

```
Забранени patterns в robots.txt:
  /search
  /*?q=*
  /*?sort=*
  /*?order=*
  /*?filter=*
  /*?page=*       (за pagination)
  /*?ref=*        (tracking)
  /*?utm_*        (UTM params)
  /cart/
  /checkout/
  /account/
  /wishlist/
  /admin/
```

---

## Промяна на URL — Процес

Никога не сменяй URL без да следваш този процес:

```
1. Добави 301 redirect в /seo/redirects/redirects-master.csv
2. PR review и одобрение от SEO Manager
3. Import redirect в Cloudflare ПРЕДИ смяна на URL
4. Смени URL в Summer Cart
5. Провери redirect работи (curl -I old_url)
6. Обнови sitemap
7. Обнови internal links към стария URL
8. Документирай в changelog.md
```
