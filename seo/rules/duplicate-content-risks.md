# Duplicate Content Risks — angelcosmetics.bg

## Познати рискове и решения

---

### Risk 1: Множество Product URLs

**Проблем:** Summer Cart може да генерира product достъпен от множество paths едновременно:
```
/face-care/serums/product-slug/
/brands/la-roche-posay/product-slug/
/product-slug/
```

**Последствие:** Google избира кой URL да ранкира (вероятно грешния). Link equity се размива.

**Решение:**
- Дефинирай preferred URL pattern (вижда `/seo/rules/canonical-rules.md`)
- Canonical tags на всички secondary paths → preferred URL
- **[ACTION]** Верифицирай с developer колко URLs генерира Summer Cart за един продукт

---

### Risk 2: Filter URL Explosion

**Проблем:** Филтриране по бранд, тип кожа, цена, съставка генерира уникални URLs:
```
/face-care/serums/?brand=la-roche-posay
/face-care/serums/?skin_type=dry
/face-care/serums/?brand=la-roche-posay&skin_type=dry
```

**Последствие:** Hundreds-thousands от thin URLs. Crawl budget waste. Diluted signals.

**Решение:**
- Всички filter URLs → noindex, follow
- Canonical filter URLs → parent category
- Robots.txt: `Disallow: /*?filter=*`, `Disallow: /*?brand=*` (ако нямаме dedicated brand pages)
- **Изключение:** Само ако filter combo има high search volume И нямаме dedicated page

---

### Risk 3: Sort URL Duplication

**Проблем:**
```
/face-care/serums/?sort=price_asc
/face-care/serums/?sort=price_desc
/face-care/serums/?sort=newest
```
Едно и също съдържание, различни URLs.

**Решение:**
- Всички sort URLs → noindex, follow
- Canonical → unsorted category URL
- Robots.txt: `Disallow: /*?sort=*`

---

### Risk 4: Product Size/Variant Duplicates

**Проблем:** Един продукт в 3 размера = 3 отделни pages с почти идентично съдържание:
```
/face-care/moisturizers/cerave-cream-50ml/
/face-care/moisturizers/cerave-cream-250ml/
/face-care/moisturizers/cerave-cream-460ml/
```

**Решение:**
- Избери preferred variant (най-популярен размер) → INDEX
- Останалите variants → canonical → preferred
- **ИЛИ:** Един page с variant selector → всички canonicalize → main page
- **[CUSTOM DEV]** Изисква implementation в Summer Cart

---

### Risk 5: Manufacturer Description Duplication

**Проблем:** Стотици e-commerce сайтове продават едни и същи продукти с идентично manufacturer description.

**Последствие:** Google devalues duplicate content. Ranking за product descriptions намалява.

**Решение:**
- Задължителна editorial добавена стойност на всяка product page
- Manufacturer description = база, НЕ final copy
- Вижда: `/seo/rules/content-quality-rules.md`

---

### Risk 6: Blog → Category Cannibalization

**Проблем:** Blog article "Най-добрите серуми за суха кожа" и category page `/face-care/serums/` таргетират сходни keywords.

**Последствие:** Google не знае коя страница да ранкира. И двете губят позиции.

**Решение:**
- Blog: таргетира listicle/comparison intent ("кой е най-добрият...")
- Category: таргетира navigational/commercial intent ("серуми за лице")
- Различни H1, meta title и primary keywords
- Blog links към category → signal hierarchy

---

### Risk 7: Problem Page → Category Cannibalization

**Проблем:** `/skin-concerns/dry-skin/` и `/face-care/moisturizers/` и двете се борят за "крем за суха кожа".

**Решение:**
- Moisturizers category таргетира: "хидратиращи кремове", "кремове за лице"
- Dry skin concern page таргетира: "грижа за суха кожа", "продукти за суха кожа"
- Ясна диференциация в H1, title, intro copy

---

### Risk 8: Pagination Duplicates

**Проблем:** `/face-care/serums/page/2/` — идентична structure като page 1, само различни продукти.

**Решение:**
- Pagination pages 2+ → noindex, follow
- Canonical pagination 2+ → страница 1
- **ИЛИ:** Infinite scroll (без pagination URLs)

---

### Risk 9: Seasonal/Sale Landing Pages

**Проблем:** Black Friday 2024 landing page стои live след събитието с 200+ OK, но outdated съдържание.

**Решение:**
- След събитие: 301 redirect → `/promotions/` или noindex
- НЕ изтривай страницата напълно (губиш inbound links)
- Запази URL за следващата година

---

## Cannibalization Check Process

Преди да публикуваш нова страница, провери:

```
1. Отвори /seo/taxonomy/keyword-map.md
2. Търси primary keyword на новата страница
3. Ако keyword е вече assigned на друга страница → СТОП
4. Диференцирай: различни angle, intent, H1
5. ИЛИ: Merge съдържанието в съществуващата страница
6. ИЛИ: Решение от SEO Manager
```
