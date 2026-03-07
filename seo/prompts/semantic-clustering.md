# Prompt: Semantic Keyword Clustering

**Version:** v1.0
**Use on:** Keyword research — за групиране на keywords по topic и intent
**Output:** JSON с clusters, intent, page type suggestions

---

## КОГА ДА ПОЛЗВАШ

- При нов batch от keyword research (GSC export, Ahrefs/Semrush export)
- При проверка дали съществуващите pages покриват keyword space
- При планиране на нови page types

---

## PROMPT TEMPLATE

```
You are a technical SEO specialist for Angel Cosmetics (angelcosmetics.bg),
a Bulgarian cosmetics e-commerce store.

TASK: Cluster the following keywords by search intent and topical group.

EXISTING PAGES (to avoid suggesting duplicates):
[Paste list from /seo/taxonomy/keyword-map.md — URLs and primary keywords]

KEYWORDS TO CLUSTER:
[Paste list of 20-100 keywords from keyword research tool]

CLUSTER RULES:
1. Group by BOTH intent (informational/commercial/navigational) AND topic
2. For each cluster: suggest the page type that should target it
   (Category / Subcategory / Brand / Series / Problem / Ingredient / Blog / Routine)
3. Flag clusters that overlap with EXISTING PAGES (potential cannibalization)
4. Flag clusters with HIGH search volume (priority)
5. Do NOT suggest creating pages that already exist in the existing pages list

OUTPUT FORMAT (JSON):
{
  "clusters": [
    {
      "cluster_name": "string",
      "intent": "informational|commercial|navigational|mixed",
      "suggested_page_type": "string",
      "suggested_url": "string",
      "monthly_volume_estimate": "high|medium|low",
      "keywords": ["keyword1", "keyword2"],
      "conflicts_with_existing": "URL of conflicting page OR null",
      "priority": "high|medium|low"
    }
  ]
}
```

---

## REVIEW CHECKLIST СЛЕД CLUSTERING

- [ ] Проверих всеки suggested URL спрямо `/seo/taxonomy/keyword-map.md`
- [ ] Идентифицирах cannibalization рискове
- [ ] Приоритизирах clusters по impact (volume × intent match)
- [ ] НЕ съм добавил директно в keyword-map.md без SEO Manager одобрение
- [ ] Записал съм findings в GitHub Issue за обсъждане

---

## ВАЖНО

AI clustering е точка на старт, не финален answer.
SEO Manager трябва да валидира всеки cluster срещу:
- Business priorities (кои продукти/категории са важни за магазина)
- Реален search volume (от GSC или keyword tool)
- Реалистична implementation effort
