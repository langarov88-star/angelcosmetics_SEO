# Series Page Template — angelcosmetics.bg

## Кога се прилага

За `/brands/{brand-slug}/{series-slug}/` страници.

**INDEX условие:** ≥3 products + 200+ думи editorial content

---

## SEO Title
```
{Brand} {Series} — {Benefit} | Angel Cosmetics
Example: La Roche-Posay Effaclar — Козметика за Акне | Angel Cosmetics
Chars: ≤60
```

## Meta Description
```
{Series} от {Brand} — {target potребител и key benefit}.
{N} продукта. Виж пълната рутина.
Chars: 150-160
```

## H1
```
{Brand} {Series} — {benefit за целевия проблем}
Example: "La Roche-Posay Effaclar — ефективна грижа за мазна и акне кожа"
```

---

## Структура

### Блок 1: Series Description (задължителен, 150-250 думи)
```
  - Какъв проблем/нужда решава серията
  - Ключови характеристики (без да е PR текст)
  - Ключови съставки (с links към ingredient pages)
  - За кой тип кожа / кожен проблем
```

### Блок 2: Продуктите в Серията
```
Format: Product cards
Всеки с: Name, image, price, кратко описание (2 изречения), "Добави в кошница"
Ако е много голяма серия — групирай по routine step (Почистване | Лечение | Хидратация)
```

### Блок 3: Препоръчана Рутина с {Series}
```
Format: Step-by-step routine
  Сутрин:
    1. {Product from series} — как се ползва
    2. {Product from series} — как се ползва
    3. SPF (ако серията има или препоръчай external)

  Вечер:
    1. {Product from series}
    2. ...
```

### Блок 4: "Ключови Съставки"
```
2-4 key ingredients с links към ingredient pages
```

### Блок 5: "Подходящо за"
```
Links към /skin-concerns/ pages
```

### Блок 6: FAQ (3-4 Q&A)
```
Product-specific и серия-specific въпроси
Schema: FAQPage JSON-LD
```

---

## Internal Links

- [ ] Link към parent brand page → `/brands/{brand-slug}/`
- [ ] Links към relevant problem pages (2-3)
- [ ] Links към ingredient pages (2-3)
- [ ] Link back от brand page → тази series page
