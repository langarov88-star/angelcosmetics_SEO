# Brand Page Template — angelcosmetics.bg

## Кога се прилага

За всички `/brands/{brand-slug}/` страници.

**INDEX условие:** 250+ думи editorial content. Само product grid без editorial = NOINDEX.

---

## SEO Title
```
{Brand Name} — Козметика | Angel Cosmetics
Example: La Roche-Posay — Козметика | Angel Cosmetics
Chars: ≤60
```

## Meta Description
```
Открий пълната гама {Brand Name} в Angel Cosmetics. {Brand positioning — 1 sentence}.
{N}+ продукта на склад.
Chars: 150-160
```

## H1
```
{Brand Name} — {brief brand positioning}
Example: "La Roche-Posay — дерматологична козметика за чувствителна кожа"
```

---

## Структура на Страницата

### Блок 1: Brand Story (задължителен)
```
Word count: 200-300 думи

Съдържание:
  - Кратка история на бранда (САМО ако е интересна, не dry PR)
  - Философия и подход
  - Ключови ценности (дерматологично тестван, dermatologist recommended, etc.)
  - За кой тип кожа/коса е подходящ

НЕ е:
  - Copy-paste от brand website
  - Marketing press release
  - Generic "brand е лидер"
```

### Блок 2: Ключови Серии
```
Format: Cards с thumbnail, name, short description
Links към series pages

Example (La Roche-Posay):
  [Effaclar — за акне и мазна кожа]
  [Cicaplast — за чувствителна и раздразнена кожа]
  [Toleriane — за свръхчувствителна кожа]
  [Anthelios — слънцезащита]
  [Lipikar — за суха и атопична кожа]
```

### Блок 3: За Какъв Тип Кожа / Проблем
```
Format: Tags или links
Links към /skin-concerns/ pages

Example:
  Подходящ за: [Чувствителна кожа] [Акне кожа] [Суха кожа] [Атопична кожа]
  → Links към concern pages
```

### Блок 4: Ключови Съставки
```
Format: 2-4 съставки с кратко описание
Links към /ingredients/ pages

Example (La Roche-Posay):
  La Roche-Posay ползва термална вода от Овернь, нежна формула без парфюми,
  дерматологично тествана. Ключови съставки: [Ниацинамид] [Салицилова киселина]
```

### Блок 5: Product Listing по Серии
```
Format: Групирани по серия sections
Или: Стандартна product grid с filter по серия

Максимум: 12-24 продукта на първа страница (pagination → noindex)
```

### Блок 6: FAQ
```
Брой: 3-4 въпроса специфични за бранда
Schema: FAQPage JSON-LD

Примерни въпроси:
  Q: Подходяща ли е La Roche-Posay за бебета?
  Q: Съдържат ли продуктите на La Roche-Posay парабени?
  Q: Каква е разликата между Effaclar и Toleriane?
```

---

## Минимален Content Checklist

- [ ] 250+ думи editorial (brand story + серии + за кого)
- [ ] H1 съдържа brand name + positioning
- [ ] Links към всички series pages (≥2 серии)
- [ ] Links към relevant /skin-concerns/ pages
- [ ] Links към ingredient pages (1-3)
- [ ] FAQ block (3+ Q&A)
- [ ] FAQPage schema
