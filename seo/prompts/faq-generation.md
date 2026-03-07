# Prompt: FAQ Generation

**Version:** v1.0
**Use on:** Problem pages, Ingredient pages, Brand pages, Category pages
**Output:** 5-7 Q&A pairs в markdown формат

---

## ПРАВИЛА ПРЕДИ УПОТРЕБА

- [ ] Проверил съм дали страницата вече има FAQ
- [ ] Имам ясен page type и primary keyword
- [ ] Ще направя factual review на всеки отговор
- [ ] Ще направя human rewrite преди публикуване

---

## PROMPT TEMPLATE

Копирай, попълни `[INPUT]` секциите и изпрати към OpenAI:

```
You are a senior content writer for a Bulgarian cosmetics e-commerce store
called Angel Cosmetics (angelcosmetics.bg). You specialize in skincare and
haircare content.

PAGE TYPE: [Problem Page / Ingredient Page / Category Page / Brand Page]
PAGE TOPIC: [e.g., "Суха кожа" / "Ниацинамид" / "Серуми за лице"]
PRIMARY KEYWORD: [e.g., "грижа за суха кожа"]
LANGUAGE: Bulgarian

TASK: Generate 5-7 FAQ questions and answers for this page.

STRICT RULES:
1. Questions must be REAL questions that users actually ask (check Google "People Also Ask")
2. Answers must be factually accurate — no medical diagnoses, no treatment claims
3. Answers must be 50-150 words each — informative but concise
4. Do NOT mention competitor brands by name
5. Do NOT make medical claims (e.g., "cures", "treats", "heals")
6. Use practical, accessible language — not scientific jargon
7. Answers should naturally mention 1-2 ingredient names or product types
   where relevant (not forced)
8. Write in Bulgarian
9. Output format: Markdown with Q: and A: labels

CONTEXT ABOUT THE PAGE:
[Paste 2-3 sentences describing what the page covers]

TOPICS TO COVER IN FAQ (choose the most relevant 5-7):
[Paste 5-10 topic areas you want covered, e.g.:
 - Разлика между суха и обезводнена кожа
 - Как да изберем крем за суха кожа
 - SPF при суха кожа
 - Серум или крем — кое е по-важно
 - Колко пъти да мием лицето при суха кожа
]

Generate the FAQ now.
```

---

## POST-GENERATION REVIEW CHECKLIST

- [ ] Всеки отговор е фактически верен
- [ ] Няма медицински claims ("лекува", "лечи")
- [ ] Тонът е практичен, не marketing-heavy
- [ ] Въпросите са реалистични (не keyword bait)
- [ ] Отговорите са на български и добре написани
- [ ] Поне 2-3 въпроса имат natural keyword usage
- [ ] Human rewrite направен (не copy-paste от AI)
- [ ] FAQPage schema е готова за имплементация (виж /seo/schema/faqpage.json)
