# Content Brief Template

## Инструкции за попълване

Копирай този файл, попълни всички полета и запази като:
`/seo/templates/content-briefs/active/BRIEF-{page-slug}-{YYYY-MM-DD}.md`

Örnek: `BRIEF-dry-skin-concern-2025-03-07.md`

---

# BRIEF: {Page Title}

## Мета информация

| Поле | Стойност |
|------|---------|
| **URL** | `/{path}/` |
| **Page Type** | Category / Brand / Series / Problem / Ingredient / Blog / Routine |
| **Приоритет** | HIGH / MEDIUM / LOW |
| **Дата на brief** | YYYY-MM-DD |
| **SEO Manager** | [Имe] |
| **Content Editor** | [Имe] |
| **Target publish date** | YYYY-MM-DD |

---

## SEO Данни

| Поле | Стойност |
|------|---------|
| **Primary Keyword** | |
| **Monthly Search Volume** | (от GSC или keyword tool) |
| **Search Intent** | Informational / Commercial / Navigational / Mixed |
| **Secondary Keywords** | keyword1, keyword2, keyword3 |
| **Current Ranking** | (ако страницата съществува) |

### Keyword Cannibalization Check
- [ ] Primary keyword проверен в `/seo/taxonomy/keyword-map.md`
- [ ] Не се припокрива с: {посочи страниците ако има близки}

---

## On-Page SEO

| Елемент | Стойност |
|---------|---------|
| **SEO Title** | (≤60 chars) |
| **Meta Description** | (150-160 chars) |
| **H1** | |
| **URL slug** | |

---

## Content Scope

**Цел на страницата:**
(Какво трябва да постигне — конверсия, information, navigation)

**Target потребител:**
(Кой ще търси тази страница и с какво намерение)

**Tone of Voice:**
(Практичен, educational, не медицински, не marketing-heavy)

---

## Структура на Страницата

Опиши конкретните секции, базирани на page type template:

```
1. {Секция 1} — {~X думи}
2. {Секция 2} — {~X думи}
3. {Секция 3} — {~X думи}
...
```

**Минимален word count:** _____ думи
**Препоръчан word count:** _____ думи

---

## Конкурентен Анализ

| URL | Какво правят добре | Какво можем да направим по-добре |
|-----|--------------------|----------------------------------|
| {competitor URL 1} | | |
| {competitor URL 2} | | |

---

## Internal Linking

### Links ОТ тази страница (outgoing):

| Anchor Text | Destination URL | Type |
|------------|----------------|------|
| | | Manual / Rule-based |

### Links КЪМ тази страница (incoming) — планирани:

| Source Page | Anchor Text |
|------------|------------|
| | |

---

## Schema Markup

| Schema Type | Задължителен |
|-------------|-------------|
| BreadcrumbList | Да |
| FAQPage | ☐ Да / ☐ Не |
| Product | ☐ Да / ☐ Не |
| Article | ☐ Да / ☐ Не |
| HowTo | ☐ Да / ☐ Не |

---

## FAQ Въпроси (за FAQPage schema)

Предложи 5-7 реални въпроса, базирани на "People Also Ask" и реални търсения:

1.
2.
3.
4.
5.

---

## AI Assist (ако се ползва)

- [ ] Prompt използван: `/seo/prompts/{prompt-file}.md`
- [ ] AI output е в: `/seo/internal-links/ai-link-suggestions/`
- [ ] Human review: ☐ Pending / ☐ Completed
- [ ] Factual check: ☐ Pending / ☐ Completed

---

## Approval Checklist (преди публикуване)

- [ ] Word count ≥ минималния за page type
- [ ] Primary keyword в: Title, H1, first 100 думи
- [ ] Meta description попълнена и уникална
- [ ] Minimum 2 internal links (outgoing)
- [ ] Поне 1 inbound internal link е планиран/добавен
- [ ] Schema markup е определена и имплементирана
- [ ] Keyword map е обновен
- [ ] URL е добавен в sitemap (ако е нова страница)
- [ ] SEO Manager: ☐ Одобрен
- [ ] Developer: ☐ Имплементиран
- [ ] Published: ☐ LIVE / Дата: ___________
