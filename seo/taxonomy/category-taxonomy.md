# Category Taxonomy — angelcosmetics.bg

## Правило за Таксономия

- Tier 1 = Main Categories → `/category-slug/`
- Tier 2 = Subcategories → `/category-slug/subcategory-slug/`
- Products живеят в Tier 2 (или Tier 1 ако subcategory не е нужна)
- Максимална дълбочина: 3 нива (Tier 1 / Tier 2 / Product)

---

## Пълна Категорийна Структура

### Face Care
```
/face-care/                         [INDEX — Main Category]
  /face-care/cleansers/             [INDEX — Subcategory]
  /face-care/toners/                [INDEX — Subcategory]
  /face-care/serums/                [INDEX — Subcategory]
  /face-care/moisturizers/          [INDEX — Subcategory]
  /face-care/eye-care/              [INDEX — Subcategory]
  /face-care/face-masks/            [INDEX — Subcategory]
  /face-care/exfoliants/            [INDEX — Subcategory]
  /face-care/face-oils/             [INDEX — Subcategory]
  /face-care/lip-care/              [INDEX — Subcategory, ако >10 products]
  /face-care/acne-treatments/       [INDEX — Subcategory]
  /face-care/spf-face/              [INDEX — Subcategory, или в sun-care]
```

### Body Care
```
/body-care/                         [INDEX — Main Category]
  /body-care/body-lotions/          [INDEX]
  /body-care/body-scrubs/           [INDEX]
  /body-care/body-oils/             [INDEX, ако >10 products]
  /body-care/hand-care/             [INDEX]
  /body-care/foot-care/             [INDEX, ако >10 products]
  /body-care/intimate-care/         [INDEX, ако >10 products]
  /body-care/deodorants/            [INDEX]
```

### Hair Care
```
/hair-care/                         [INDEX — Main Category]
  /hair-care/shampoos/              [INDEX]
  /hair-care/conditioners/          [INDEX]
  /hair-care/hair-masks/            [INDEX]
  /hair-care/scalp-care/            [INDEX]
  /hair-care/hair-oils/             [INDEX, ако >10 products]
  /hair-care/styling/               [INDEX]
  /hair-care/hair-color-care/       [INDEX, ако >10 products]
```

### Sun Care
```
/sun-care/                          [INDEX — Main Category]
  /sun-care/face-spf/               [INDEX]
  /sun-care/body-spf/               [INDEX]
  /sun-care/kids-spf/               [INDEX, ако >10 products]
  /sun-care/after-sun/              [INDEX, ако >10 products]
  /sun-care/self-tan/               [INDEX, ако >10 products]
```

### Makeup
```
/makeup/                            [INDEX — Main Category]
  /makeup/foundation/               [INDEX]
  /makeup/concealer/                [INDEX, ако >10 products]
  /makeup/eyes/                     [INDEX]
  /makeup/lips/                     [INDEX]
  /makeup/blush-bronzer/            [INDEX, ако >10 products]
  /makeup/setting-spray/            [INDEX, ако >10 products]
  /makeup/removal/                  [INDEX]
  /makeup/brushes-tools/            [INDEX, ако >10 products]
```

### Parfums
```
/perfumes/                          [INDEX — Main Category, ако магазинът продава]
  /perfumes/women/                  [INDEX]
  /perfumes/men/                    [INDEX]
  /perfumes/unisex/                 [INDEX, ако >10 products]
```

### Baby & Kids
```
/baby-care/                         [INDEX — Main Category, ако applicable]
  /baby-care/baby-skin/             [INDEX]
  /baby-care/baby-hair/             [INDEX, ако >10 products]
```

### Men's Care
```
/mens-care/                         [INDEX — Main Category, ако applicable]
  /mens-care/face/                  [INDEX]
  /mens-care/shaving/               [INDEX]
  /mens-care/body/                  [INDEX, ако >10 products]
```

---

## Индексиране Решения

| Условие | Решение |
|---------|---------|
| Subcategory с ≥10 products + описание | INDEX |
| Subcategory с <10 products | NOINDEX (временно) |
| Subcategory без описание | NOINDEX (добави описание → INDEX) |
| Empty category | NOINDEX или скрий от navigation |

---

## Pending Decisions

Маркирай категории, за които решението все още се обмисля:

| Category | Статус | Бележки |
|----------|--------|---------|
| /face-care/spf-face/ | ❓ PENDING | Дублира се с /sun-care/face-spf/? Реши кое е preferred |
| /makeup/setting-spray/ | ❓ PENDING | Достатъчно products? |

---

## Как се Update-ва тази таблица

1. При добавяне на нова категория → добави тук с INDEX/NOINDEX решение
2. При достигане на threshold (10+ products) → смени от NOINDEX → INDEX
3. При merge на две категории → 301 redirect от премахнатата + документирай в changelog
4. Всяка промяна → PR → SEO Manager одобрение
