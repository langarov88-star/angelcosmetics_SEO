# Prompt: Internal Link Suggestions

**Version:** v1.0
**Use on:** Blog articles, Problem pages, Ingredient pages — за намиране на internal link opportunities
**Output:** Списък с anchor text + target URL предложения

---

## ПРАВИЛА ПРЕДИ УПОТРЕБА

- [ ] Имам пълния текст на страницата
- [ ] Имам актуалния `/seo/taxonomy/keyword-map.md` за reference
- [ ] Ще проверя дали всеки suggested URL реално съществува
- [ ] Максимум 5-7 AI-suggested links per страница (не всички ще се използват)

---

## PROMPT TEMPLATE

```
You are an SEO specialist for Angel Cosmetics (angelcosmetics.bg).

TASK: Suggest internal links for the following page content.

EXISTING PAGES ON THE SITE (these are the ONLY pages you can suggest):
[Paste relevant sections from /seo/taxonomy/keyword-map.md]

PAGE TYPE: [Blog Article / Problem Page / Ingredient Page]
PAGE URL: [URL of this page]
PAGE TEXT:
---
[Paste full text of the page]
---

RULES:
1. Suggest ONLY links to pages in the "EXISTING PAGES" list above
2. Maximum 7 suggestions total
3. For each suggestion: quote the exact phrase from the text where the link should go
4. Anchor text must be NATURAL in context — not forced keyword stuffing
5. Do NOT suggest linking the page to itself
6. Prioritize links that add genuine value for the reader
7. Prefer deep links (ingredient pages, problem pages) over generic category links
8. Avoid suggesting the same destination URL more than once

OUTPUT FORMAT:
1. Anchor text: "[exact phrase from text]"
   Target URL: /path/to/page/
   Reason: [1 sentence why this link adds value]

2. [next suggestion]
...
```

---

## REVIEW CHECKLIST

- [ ] Всеки suggested URL е проверен — реално съществува
- [ ] Anchor text е натурален в контекста (прочети изречението с линка)
- [ ] Не повтаряме destination URL повече от веднъж
- [ ] Links добавят стойност за читателя (не само за SEO)
- [ ] Одобрени links → добав в manual-links-log.md

---

## POST-IMPLEMENTATION

След добавяне на links:
- Запиши в `/seo/internal-links/manual-links-log.md`
- Format: `[дата] | [source URL] | [anchor] | [destination URL]`
