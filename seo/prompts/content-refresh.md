# Prompt: Content Refresh

**Version:** v1.0
**Use on:** Стари blog articles или pages с declining rankings
**Output:** Анализ на outdated секции + конкретни препоръки за update

---

## КОГА ДА ПОЛЗВАШ

- Page е >12 месеца стара и rankings са паднали
- GSC показва declining impressions или CTR
- Продуктите или съставките в съдържанието са се сменили
- Нова информация е налична (нов product launch, нови research)

---

## PROMPT TEMPLATE

```
You are a content strategist for Angel Cosmetics (angelcosmetics.bg),
a Bulgarian cosmetics e-commerce store.

TASK: Analyze the following page content and suggest specific updates
to improve its SEO relevance and freshness.

PAGE URL: [URL]
PAGE TYPE: [Blog Article / Problem Page / Ingredient Page]
DATE PUBLISHED: [YYYY-MM-DD]
CURRENT DATE: [YYYY-MM-DD]
PRIMARY KEYWORD: [keyword]

CURRENT CONTENT:
---
[Paste full current page content]
---

CONTEXT (provide what you know):
- Products mentioned that are now discontinued: [list or "none"]
- New relevant products to add: [list or "none"]
- New information in this category: [describe or "none"]
- Current search intent for primary keyword: [how users search for this now]

ANALYSIS RULES:
1. Identify SPECIFIC outdated sections (quote the exact text)
2. Suggest what should REPLACE or UPDATE each section
3. Identify missing sections that would improve the page
4. Check for: outdated product mentions, outdated ingredient info,
   missing FAQ questions that are now common, missing internal links
5. Do NOT suggest adding sections for the sake of it — only genuinely valuable additions
6. Do NOT suggest changing the page's primary topic

OUTPUT FORMAT:
### Outdated Sections:
1. [Quote exact text] → [Suggested update]

### Missing Sections:
1. [Section name] → [Why it's needed] → [Brief content outline]

### Internal Link Opportunities:
1. [Anchor text suggestion] → [Target page]

### FAQ to Add:
1. Q: [question] — A: [brief answer]

### Summary: Is this a MINOR update (quick edit) or MAJOR rewrite?
```

---

## REVIEW CHECKLIST

- [ ] Проверих фактическата точност на AI предложенията
- [ ] Проверих дали suggested products реално са налични в магазина
- [ ] Не съм приел AI предложение без fact-check
- [ ] Content editor е направил final rewrite
- [ ] SEO Manager е одобрил промените
- [ ] `dateModified` в Article schema е обновена след refresh
