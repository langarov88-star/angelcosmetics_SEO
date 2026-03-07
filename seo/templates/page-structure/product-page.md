# Product Page Template — angelcosmetics.bg

## Кога се прилага

За всички product pages в Summer Cart.

**INDEX условие:** Продуктът е наличен + editorial description (200+ думи)
**За discontinued продукти:** 301 redirect

---

## SEO Title
```
{Product Name} | {Brand} | Angel Cosmetics
Example: CeraVe Хидратиращ Лосион 236ml | CeraVe | Angel Cosmetics
Chars: ≤60

Ако продуктът е дълъг:
  {Short Product Name} {Size} | {Brand} | Angel Cosmetics
```

## Meta Description
```
{Product Name} от {Brand} — {1 изречение benefit}. {Skin type}.
Поръчай онлайн с бърза доставка от Angel Cosmetics.
Chars: 150-160
```

## H1
```
{Product Name} — {short descriptor}
Example: "CeraVe Хидратиращ Лосион — нежна хидратация с керамиди"
```

---

## Структура на Страницата

### Блок 1: Buy Box (native Summer Cart)
```
Елементи:
  - Product images (multiple angles)
  - Price (с/без промоция)
  - Size/variant selector (ако приложимо)
  - Add to cart button
  - Stock status
  - Delivery info ("Доставка до 2-3 работни дни")
  - Trust signals (returns policy, secure payment)
```

### Блок 2: Editorial Product Description (задължителен)
```
Word count: 200-300 думи
Позиция: Под или до buy box (в tab или expander)

СТРУКТУРА:
1. Opening paragraph (50-80 думи):
   Какво е продуктът, за кого е, какъв ефект дава.
   НЕ е копирана manufacturer description.

2. Ключови ефекти (bullet list, 3-5 точки):
   - Конкретни benefiti (не generic "за красива кожа")
   - Базирани на реални съставки

3. За кого е (50-80 думи):
   Skin type, concerns, кога е НЕ подходящ.

4. Как се използва (40-60 думи):
   Стъпка, честота, AM/PM, количество.
```

### Блок 3: Ingredient Highlights
```
Format: 2-4 key ingredients с кратко описание + link към ingredient page
НЕ е пълен INCI список (него слагаме отделно)

Example:
  **Хиалуронова киселина** — задържа влагата в кожата
    → [Научи повече за хиалуроновата киселина](/ingredients/hyaluronic-acid/)
  **Керамиди** — възстановяват кожната бариера
    → [Научи повече за керамидите](/ingredients/ceramides/)
```

### Блок 4: "Подходящо за" Tags
```
Format: Clickable tags → links към /skin-concerns/ pages

Example:
  Подходящо за: [Суха кожа] [Нормална кожа] [Чувствителна кожа]
  → Links към concern pages
```

### Блок 5: "Как се използва" Section
```
Format: Стъпки или short paragraph
Позиция: Tab или accordion

Съдържание:
  - Количество за нанасяне
  - Начин на нанасяне
  - Честота (сутрин/вечер/и двете)
  - Стъпка в рутината (след тонер, преди крем, etc.)
  - Специални инструкции ако има
```

### Блок 6: Пълен INCI Ingredient List
```
Format: Accordion (collapsed by default)
Съдържание: Пълен INCI ingredient list
За потребители, които проверяват алергени
```

### Блок 7: "Комбинирай с" Cross-sell (rule-based)
```
Логика:
  1. Продукти от СЪЩАТА серия (приоритет)
  2. Complementary products по routine step
     (ако е серум → покажи подходящ крем)
  3. От СЪЩИЯ бранд

НЕ е:
  - "Клиентите купиха и" (на this stage)
  - Random related products

[CUSTOM DEV] Изисква tag-based rule в Summer Cart
```

### Блок 8: Customer Reviews
```
Native Summer Cart functionality
Schema: AggregateRating в Product JSON-LD
Минимум: Покажи дори 0 reviews (с форма за писане)
```

### Блок 9: FAQ (желателен)
```
Брой: 2-3 product-specific Q&A
Schema: FAQPage JSON-LD (ако са ≥2)

Примери:
  Q: Може ли CeraVe Хидратиращ Лосион да се ползва под фон дьо тен?
  Q: Подходящ ли е за акне кожа?
```

### Блок 10: "Виж всички продукти на {Brand}"
```
Format: Link с anchor text
→ /brands/{brand-slug}/
```

---

## SEO Rules за Product Pages

### Duplicate content prevention:
- Ако един продукт е в множество категории → canonical → preferred URL
- Ако продуктът е в различни размери → canonical variant → preferred size
- НЕ copy-paste manufacturer description

### Out-of-stock products:
- Временно изчерпан → Запази INDEX, добави "временно изчерпан" UI
- Discontinued → 301 redirect → closest alternative или category

### Schema:
- Product schema задължителен (вижда /seo/schema/product.json)
- Проверявай с Google Rich Results Test след имплементация
