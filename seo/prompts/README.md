# AI Prompt Library — angelcosmetics.bg

## Принципи за AI Употреба

Всички prompts в тази директория са:
- **Версионирани** — промени минават през PR
- **Rule-based** — съдържат строги ограничения
- **Контролирани** — output минава human review ПРЕДИ публикуване

### Какво AI може да прави:
- First draft assist за FAQ blocks
- Meta description варианти (за избор)
- Category intro copy структура
- Semantic keyword clustering
- Internal link suggestions
- Content refresh препоръки

### Какво AI НЕ прави:
- Не публикува съдържание директно
- Не генерира медицински claims
- Не прави bulk generation без review
- Не замества editorial judgment

---

## Налични Prompts

| Файл | Употреба |
|------|---------|
| `faq-generation.md` | Генериране на FAQ Q&A за problem/ingredient/category pages |
| `meta-description.md` | Варианти на meta descriptions |
| `category-intro-copy.md` | First draft за category intro copy |
| `semantic-clustering.md` | Групиране на keywords по intent и topic |
| `internal-link-suggest.md` | Предложения за internal links от article text |
| `content-refresh.md` | Анализ и препоръки за обновяване на съдържание |

---

## Workflow за Ползване на Prompts

```
1. Избери подходящия prompt файл
2. Попълни INPUT секцията с реални данни за страницата
3. Изпрати към OpenAI (ChatGPT / API)
4. Запази output в /seo/internal-links/ai-link-suggestions/ (за link suggestions)
   или директно в content brief (за copy suggestions)
5. ЗАДЪЛЖИТЕЛЕН human review:
   a. Factual accuracy check
   b. Tone и brand voice check
   c. SEO rules check (cannibalization, keyword usage)
6. Approved output → предай на content editor за final version
7. НИКОГА не publish директно от AI output
```

---

## Версионен Log на Prompts

| Версия | Дата | Промяна |
|--------|------|---------|
| v1.0 | 2025-03-07 | Initial prompt library |
