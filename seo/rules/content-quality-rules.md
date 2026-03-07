# Content Quality Rules — angelcosmetics.bg

## Защо има правила за качество

Google третира thin content като negative ranking signal. За e-commerce, thin content означава:
- Product descriptions копирани директно от производителя (без добавена стойност)
- Category pages само с product grid и без editorial текст
- Brand pages само с logo и list от продукти
- AI-generated content публикуван без human review

---

## Минимален Word Count по Page Type

| Page Type | Минимум | Препоръчително | Включва |
|-----------|---------|----------------|---------|
| Product description | 200 думи | 300+ думи | Editorial above-fold + how-to-use + for whom |
| Category intro | 150 думи | 250+ думи | Editorial, keywords, НЕ keyword stuffing |
| Subcategory intro | 100 думи | 150+ думи | Short editorial |
| Brand page | 250 думи | 400+ думи | History, philosophy, key ingredients, series |
| Series page | 200 думи | 300+ думи | Series benefits, skin type, routine |
| Problem/Concern page | 600 думи | 1000+ думи | Full editorial + routine + FAQ |
| Ingredient page | 400 думи | 600+ думи | What is, how works, who for, combinations |
| Blog article | 800 думи | 1200+ думи | Informational + commercial links |
| Routine page | 400 думи | 600+ думи | Curated editorial + product descriptions |

---

## Правила за Product Descriptions

### ❌ НЕ приемаме:
- Дословно копирани manufacturer descriptions
- Само ingredient list без обяснение
- Generic marketing claims без specifics ("подмладяващ крем за красива кожа")
- Машинен превод без редакция

### ✅ Изискваме добавена стойност:
```
Всеки product description трябва да включва поне:
1. Какво прави продуктът (конкретно, не generic)
2. За кого е подходящ (skin type / concern)
3. Как се използва (честота, стъпка в рутината)
4. Какво го прави различен или подходящ спрямо алтернативите
```

### Product Description Template (минимална версия):
```
[Продуктът] е [тип продукт] от [Brand], разработен за [target skin type/concern].
Съдържа [key ingredients], които [specific action].
Препоръчва се за [кой е target потребителят].
Използва се [честота] — [AM/PM/both], [стъпка в рутината].
[Един факт, който отличава продукта].
```

---

## Правила за Category и Problem Pages

### Category Intro Copy — Задължителни елементи:
1. Описание на категорията (не просто "Продукти за X")
2. Как да се избере правилният продукт за нуждите
3. Препратка към subcategories или проблемни pages
4. Primary + 1-2 secondary keywords (натурално вградени, не stuffed)

### Problem Page — Задължителна структура:
1. **Дефиниция** на проблема/нуждата (не медицинска, практична)
2. **Причини** — 3-5 bullet points
3. **Ключови съставки** с links към ingredient pages
4. **Препоръчана рутина** — конкретни стъпки
5. **Curated продукти** — 6-12, не automated listing без context
6. **FAQ** — 5-7 реални въпроси с отговори
7. **Свързани проблеми** — links към related concern pages

---

## Duplicate Content Rules

### Никога:
- Не копирай описание от конкурент (дори partialno)
- Не публикувай един и същ текст на две различни pages
- Не ползвай AI генерирано съдържание без significant rewrite
- Не синдикирай manufacturer press releases без трансформация

### За Product Variants:
```
Продукт в различни размери (50ml, 100ml, 200ml):
  → Един preferred product page (INDEX) за размера с най-висок volume
  → Останалите варианти → canonical към preferred
  → ИЛИ: Един page с размерен selector, всички варианти = canonical → main page
```

### За Seasonal/Sale Pages:
```
Black Friday landing page:
  → Публикувай преди събитието
  → След събитието: НЕ изтривай, 301 redirect → обща promotions страница
  → ИЛИ: Noindex след събитието, preserve page за следващата година
```

---

## AI Content — Quality Control Process

AI може да помага само като **first draft assist**. Следният процес е задължителен:

```
Стъпка 1: Ползвай prompt от /seo/prompts/ (НЕ импровизирани prompts)
Стъпка 2: Генерирай draft
Стъпка 3: Factual check — провери всяко твърдение
Стъпка 4: Rewrite за tone, brand voice и uniqueness
Стъпка 5: SEO review (keywords, internal links)
Стъпка 6: Final approval от content lead
Стъпка 7: Публикуване
```

**НИКОГА:** Bulk generation + директно публикуване.

---

## Thin Content Checklist (преди публикуване)

- [ ] Минималният word count е спазен за page type
- [ ] Описанието е уникално (не копирано)
- [ ] Има поне 2 internal links от/към страницата
- [ ] H1 е уникален и съдържа primary keyword
- [ ] Meta description е написана (не auto-generated)
- [ ] Ако е product page — има "за кого е" и "как се ползва"
- [ ] Ако е problem page — има FAQ блок (5+ Q&A)
- [ ] Ако е AI-assisted — human review е completed

---

## Кога да Noindex вместо да подобряваме

Ако страницата:
- Има <50 думи и няма ресурс за подобрение в следващите 30 дни → NOINDEX
- Е автоматично генерирана (filter URL, tag page) без editorial → NOINDEX
- Дублира съдържание от друга indexed страница → NOINDEX + canonical

**Принцип:** По-добре по-малко indexed pages с качествено съдържание, отколкото много thin pages.
