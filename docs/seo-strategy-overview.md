# SEO Strategy Overview — angelcosmetics.bg

## Цел на системата

Изграждаме скалируема SEO система за angelcosmetics.bg — козметичен e-commerce магазин с множество брандове, серии, продуктови категории и специфични нужди на клиентите.

Целта НЕ е единични оптимизации. Целта е архитектура, която:
- Изгражда topical authority в нишата козметика
- Генерира organic трафик от информационни, navigational и commercial queries
- Свързва информационното и commercial съдържание в обща SEO ecosystem
- Мащабира се без да изисква индивидуална оптимизация на всеки продукт

---

## Технологичен стек

| Слой | Инструмент | Роля |
|------|-----------|------|
| Platform | Summer Cart | E-commerce — products, categories, checkout, native SEO fields |
| Governance | GitHub (този repo) | Single source of truth за SEO rules, taxonomy, templates |
| Edge | Cloudflare | Redirects, cache, performance, security |
| AI Assist | OpenAI API | Controlled content assistance — FAQ, meta, clustering |

---

## Топ 5 SEO Leverage Points

1. **Problem/need pages** — "крем за суха кожа", "грижа за акне кожа" — middle-funnel, висок volume, ниска конкуренция спрямо product pages, отлична conversion.

2. **Brand + Series pages с editorial съдържание** — brand pages само с product grid не ранкират. С 250+ думи editorial → branded + category ranking.

3. **Ingredient authority pages** — "ретинол", "ниацинамид", "хиалуронова киселина" — информационни keywords с commercial intent, идеални за internal linking.

4. **Clean URL taxonomy без duplicate paths** — Summer Cart може да генерира множество URLs за един продукт. Без canonical governance → crawl waste и cannibalization.

5. **Structured data качество** — Валидна Product schema с reviews + FAQPage на problem/ingredient pages = rich results без риск.

---

## Page Type йерархия (приоритет за SEO)

```
TIER 1 — Критични (Phase 1):
  Home
  Main Category pages
  Top 5 Problem/Concern pages
  Top 10 Brand pages

TIER 2 — Важни (Phase 2):
  Subcategory pages (с ≥10 products)
  Series pages (с ≥3 products)
  Top Ingredient pages
  Blog articles

TIER 3 — Scaling (Phase 3):
  All remaining ingredient pages
  Routine/Solution pages
  Secondary brand pages
  Long-tail blog content
```

---

## Indexing Philosophy

**Индексираме само pages, които:**
- Имат уникално, substantive съдържание
- Таргетират конкретен keyword с ясен intent
- Имат ≥1 inbound internal link
- Не създават cannibalization с друга indexed страница

**Noindex за:**
- Filter/sort/search pages
- Pagination (страница 2+)
- Thin pages без editorial content
- Discontinued products

Пълна матрица: `/seo/rules/indexing-rules.md`

---

## Content Quality Baseline

| Page Type | Минимум думи | Задължителни елементи |
|-----------|-------------|----------------------|
| Product page | 200+ | Unique description, how-to-use, skin type |
| Category intro | 150+ | Editorial, keywords, НЕ keyword stuffing |
| Problem page | 600+ | Problem definition, ingredients, routine, FAQ |
| Ingredient page | 400+ | What is, how works, who for, combinations |
| Blog article | 800+ | Informational, с links към commercial pages |
| Brand page | 250+ | History, philosophy, key ingredients, series |
| Series page | 200+ | Series benefits, skin type, routine |

---

## Implementation Phases

| Phase | Период | Фокус |
|-------|--------|-------|
| Phase 1: Foundation | Месец 1-2 | Technical cleanup, canonical, noindex, taxonomy |
| Phase 2: Scalable System | Месец 3-5 | Problem/brand/series pages, internal linking, schema |
| Phase 3: AI-Assisted Expansion | Месец 6+ | Ingredient pages, routines, content scaling |
