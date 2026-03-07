# Onboarding Guide — SEO Team

Добре дошъл в SEO governance repo на angelcosmetics.bg. Тази страница е за нови team members.

---

## Ролите в системата

| Роля | Отговорности |
|------|-------------|
| **SEO Manager** | Owns taxonomy, keyword decisions, indexing decisions, content briefs, PR approvals |
| **Developer** | Имплементира schema, canonical, noindex rules, custom SEO features в Summer Cart |
| **Content Editor** | Пише по templates, ползва AI prompts за draft assist, минава editorial review |

---

## Стъпка по стъпка: Как работи системата

### 1. Искаш да добавиш нова страница?

```
1. Провери дали страницата вече съществува в taxonomy/keyword-map.md
2. Провери дали primary keyword не се припокрива с друга страница
3. Създай content brief от template: /seo/templates/content-briefs/BRIEF-TEMPLATE.md
4. Запази го в /seo/templates/content-briefs/active/BRIEF-{slug}-{date}.md
5. Открий GitHub Issue: "New page: {slug}"
6. Открий PR след като brief е одобрен
7. Добави страницата в /seo/taxonomy/keyword-map.md след публикуване
```

### 2. Искаш да сложиш redirect?

```
1. Добави redirect в /seo/redirects/redirects-master.csv
2. Формат: old_url,new_url,type,reason,date,author
3. Открий PR с label "redirect"
4. SEO Manager одобрява
5. Developer/SEO imports в Cloudflare Bulk Redirects
6. Тествай с redirect checker
```

### 3. Искаш да използваш AI за съдържание?

```
1. Прочети /seo/prompts/README.md
2. Избери подходящия prompt от /seo/prompts/
3. Генерирай draft — НИКОГА не публикувай директно
4. Human review задължителен преди публикуване
5. AI output → editing → final version
```

### 4. Искаш да промениш SEO rule?

```
1. Открий GitHub Issue: "Rule change: {описание}"
2. Обсъди с SEO Manager
3. Направи промяната в съответния файл в /seo/rules/
4. Открий PR → SEO Manager review → merge
```

---

## Ключови файлове, които трябва да познаваш

| Файл | Защо е важен |
|------|-------------|
| `/seo/rules/indexing-rules.md` | Кои pages са index vs noindex |
| `/seo/taxonomy/keyword-map.md` | Master list: page → primary keyword |
| `/seo/redirects/redirects-master.csv` | Всички 301 redirects |
| `/seo/templates/content-briefs/BRIEF-TEMPLATE.md` | Шаблон за нови pages |
| `/seo/rules/canonical-rules.md` | Canonical logic |
| `/docs/platform-notes-summercart.md` | Какво може и не може Summer Cart |

---

## Основни правила

1. **Никога не push-вай директно в `main`** — винаги PR
2. **Никога не публикувай AI content без human review**
3. **Никога не сменяй URL без да добавиш 301 redirect**
4. **Преди нова страница — провери за keyword cannibalization**
5. **Schema промени → задължително тестване с Google Rich Results Test**

---

## Инструменти

- **Google Search Console** — трафик, индексиране, coverage errors
- **Google Rich Results Test** — валидиране на schema
- **Schema.org Validator** — https://validator.schema.org
- **Screaming Frog** (или ahrefs/semrush) — crawl audit
- **Cloudflare Dashboard** — cache rules, redirects, analytics
