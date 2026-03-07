# Category Page Template — angelcosmetics.bg

## Кога се прилага

За всички Tier 1 Main Category и Tier 2 Subcategory страници.

**INDEX условие:** ≥10 products + editorial intro copy (150+ думи)

---

## SEO Title
```
{Category Name} | Онлайн Козметика | Angel Cosmetics
Chars: ≤60
```

## Meta Description
```
Открий {N}+ {category} от водещи дерматологични брандове. {Benefit statement}.
Безплатна доставка над {X}лв.
Chars: 150-160
```

## H1
```
{Category Name} — {short benefit modifier}
Example: "Серуми за лице — хидратация, изглаждане и сияние"
Правило: H1 трябва да съдържа primary keyword. Не е идентично с title.
```

---

## Структура на Страницата

### Блок 1: Editorial Intro (задължителен)
```
Word count: 150-250 думи
Позиция: Над product listing

Съдържание:
  - Какво е категорията (описателно, практично)
  - За кого са тези продукти
  - Какви резултати дават
  - Как да се избере правилният продукт

НЕ включва:
  - Keyword stuffing
  - Generic marketing ("открийте перфектния продукт")
  - Дублиране на H1
```

### Блок 2: Subcategory Navigation (само за Tier 1)
```
Format: Grid с cards
Всяка subcategory card: Name + короткo описание + link
Пример за /face-care/:
  [Серуми] [Кремове] [Почистващи] [Маски] [Пилинги] [Масла за лице]
```

### Блок 3: "Избери по нужда" Navigation
```
Format: Хоризонтален скролируем ред или grid
Links към relevant problem pages:
  "За суха кожа" → /skin-concerns/dry-skin/
  "За акне кожа" → /skin-concerns/acne-prone-skin/
  "За чувствителна кожа" → /skin-concerns/sensitive-skin/
  "Анти-ейджинг" → /skin-concerns/anti-aging/
```

### Блок 4: Топ Брандове в Категорията
```
Format: Brand logos или text links
Пример за /face-care/serums/:
  La Roche-Posay | CeraVe | The Ordinary | Vichy | Bioderma
  [links към /brands/{brand-slug}/]
```

### Блок 5: Product Listing (native Summer Cart)
```
Sort options: Препоръчани / Цена / Нови
Filter: По бранд, тип кожа, съставка (filter URLs → noindex)
Pagination: noindex на page 2+
```

### Блок 6: "Как да изберем" Section (желателен)
```
Word count: 150-250 думи
Позиция: Под product listing или като expandable accordion
Съдържание:
  - Практически съвети за избор в тази категория
  - Какво да търсим в съставките
  - Tips по skin type
```

### Блок 7: FAQ Block
```
Брой Q&A: 3-5
Format: Accordion
Schema: FAQPage JSON-LD
Въпроси трябва да са реални въпроси, не keyword bait
```

### Блок 8: Related Categories
```
Format: Links
Example за /face-care/serums/:
  "Виж също: Кремове за лице | Тонери | Маски за лице"
```

---

## Internal Links Checklist

- [ ] Subcategory links (Tier 1 → Tier 2)
- [ ] Brand links (топ 3-5 бранда в категорията)
- [ ] Problem page links (2-4 relevant concerns)
- [ ] Related category links (bottom of page)
- [ ] Blog article links (ако има релевантни — 1-2)

---

## Пример — Реализация за /face-care/serums/

```
Title: Серуми за лице | Онлайн Козметика | Angel Cosmetics
H1:    Серуми за лице — хидратация, изглаждане и anti-aging

[Intro 200 думи — какво е серумът, видове, как да избереш]

[Subcategories: Хидратиращи | Анти-ейджинг | За акне | Brightening]

[Избери по нужда: Суха кожа | Акне | Бръчки | Пигментация]

[Топ брандове: La Roche-Posay | CeraVe | The Ordinary | Vichy]

[Product listing — 12 per page]

[Как да изберем серум — 200 думи]

[FAQ: 4 въпроса]

[Виж също: Кремове за лице | Тонери | Маски]
```
