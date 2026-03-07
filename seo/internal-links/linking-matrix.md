# Internal Linking Matrix — angelcosmetics.bg

## Принцип

Internal links:
1. Прехвърлят PageRank (link equity) между pages
2. Помагат на Google да разбере структурата и йерархията
3. Подобряват user experience — навигация между свързани теми

**Правило за orphan pages:** Всяка indexed страница трябва да има ≥1 inbound internal link.

---

## Linking Matrix по Page Type

### Home → outgoing links
| Destination | Брой | Тип |
|------------|------|-----|
| Main Categories (all) | 5-8 | Navigation |
| Top 3-5 Brand pages | 3-5 | Featured brands |
| Top 3 Problem pages | 2-3 | Editorial |
| Blog (latest articles) | 2-3 | Featured |

### Main Category → outgoing links
| Destination | Брой | Тип |
|------------|------|-----|
| Subcategories | All | Navigation |
| Relevant Problem pages | 3-5 | "Избери по нужда" section |
| Top Brand pages in category | 3-6 | "Топ брандове" section |
| Related Categories | 2-4 | Bottom |
| Blog articles (related) | 1-2 | Optional |

### Subcategory → outgoing links
| Destination | Брой | Тип |
|------------|------|-----|
| Parent Category | 1 | Breadcrumb |
| Relevant Problem pages | 2-3 | "Избери по нужда" |
| Brand pages in subcategory | 2-4 | Contextual |

### Brand Page → outgoing links
| Destination | Брой | Тип |
|------------|------|-----|
| Series pages (всички) | All | "Ключови серии" section |
| Relevant Problem pages | 2-4 | "За какъв тип кожа" |
| Ingredient pages (key) | 2-3 | "Ключови съставки" |

### Series Page → outgoing links
| Destination | Брой | Тип |
|------------|------|-----|
| Parent Brand page | 1 | Breadcrumb + contextual |
| Relevant Problem pages | 1-3 | "Подходящо за" |
| Ingredient pages | 2-3 | "Ключови съставки" |
| Product pages in series | All | Product listing |

### Problem Page → outgoing links
| Destination | Брой | Тип |
|------------|------|-----|
| Ingredient pages | 3-5 | "Ключови съставки" section |
| Product pages (curated) | 6-12 | "Препоръчани продукти" |
| Series pages | 2-4 | "Препоръчани серии" |
| Blog articles | 2-3 | "От блога" |
| Related Problem pages | 2-3 | "Виж също" |

### Ingredient Page → outgoing links
| Destination | Брой | Тип |
|------------|------|-----|
| Problem pages | 2-4 | "За кого е" section |
| Product pages (curated) | 4-8 | "Продукти с {ingredient}" |
| Related Ingredient pages | 2-3 | "Комбинира се с" / "Виж също" |
| Blog articles | 1-2 | Optional |

### Product Page → outgoing links
| Destination | Брой | Тип |
|------------|------|-----|
| Brand page | 1 | "Виж всички от {Brand}" |
| Series page | 1 | Ако продуктът е в серия |
| Category page | 1 | Breadcrumb |
| Problem pages | 1-2 | "Подходящо за" tags |
| Ingredient pages | 1-3 | "Ключови съставки" section |
| Related products | 4-8 | "Комбинирай с" (cross-sell) |

### Blog Article → outgoing links
| Destination | Брой | Тип |
|------------|------|-----|
| Problem pages | 1-2 | Contextual in text |
| Product pages | 2-4 | Contextual или "Препоръчани" |
| Ingredient pages | 1-3 | Contextual |
| Category pages | 1-2 | Contextual |
| Related Blog articles | 1-2 | "Виж също" |

---

## Link Types: Manual vs Rule-based vs AI-assisted

| Link тип | Метод |
|----------|-------|
| Navigation menu | Manual (structure) |
| Breadcrumbs | **[NATIVE Summer Cart]** |
| "Виж всички от {Brand}" на product | **[NATIVE Summer Cart]** |
| "Виж целия {Category}" | **[NATIVE Summer Cart]** |
| "Комбинирай с" (same series cross-sell) | Rule-based **[CUSTOM DEV]** |
| "Подходящо за" problem tags на products | Rule-based **[CUSTOM DEV]** |
| Editorial links в category intro | Manual |
| Editorial links в problem pages | Manual |
| Blog article → commercial pages | AI-suggested + human review |
| "Ключови съставки" с ingredient links | Manual или rule-based по tag |

---

## Depth Rules

```
Всеки продукт → достъпен в ≤3 клика от Home
Всяка problem page → достъпна от main nav или home в ≤2 клика
Ingredient pages → достъпни от problem pages + product pages
Никакви orphan pages → всяка indexed страница ≥1 inbound link
```

---

## Link Audit Schedule

| Период | Цел |
|--------|-----|
| При публикуване на нова страница | Добави ≥2 inbound links от съществуващи pages |
| Monthly | Провери за orphan pages (Screaming Frog → 0 inbound) |
| Quarterly | Full internal link audit |
