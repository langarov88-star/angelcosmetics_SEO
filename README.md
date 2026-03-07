# angelcosmetics_SEO — SEO Governance Repository

Single source of truth за цялата SEO система на **angelcosmetics.bg**.

Този repo съдържа всички SEO rules, templates, taxonomy, schema markup, AI prompts и redirect governance. Той НЕ е кодова база — той е оперативен наръчник за SEO manager, developer и content team.

---

## Структура

```
angelcosmetics_SEO/
├── docs/                          # Документация и onboarding
├── seo/
│   ├── rules/                     # SEO правила (indexing, canonical, URL, quality)
│   ├── taxonomy/                  # Категории, брандове, ingredients, keyword map
│   ├── templates/                 # On-page templates по page type
│   │   ├── page-structure/        # Пълна структура за всеки page type
│   │   └── content-briefs/        # Content brief templates
│   ├── schema/                    # JSON-LD structured data templates
│   ├── prompts/                   # OpenAI prompt library (controlled, versioned)
│   ├── redirects/                 # Redirect governance (source of truth)
│   ├── sitemaps/                  # Sitemap strategy и excluded URLs
│   └── internal-links/            # Internal linking matrix и logs
└── .github/
    └── PULL_REQUEST_TEMPLATE.md   # SEO change checklist за PR reviews
```

---

## Как да работим с repo-то

### За SEO Manager
- Всяко SEO решение (noindex, redirect, нова taxonomy страница) се документира тук преди имплементация
- Промените минават през Pull Request — не се push-ват директно в `main`
- При нова page → създай content brief в `/seo/templates/content-briefs/active/`

### За Developer
- Schema JSON-LD templates са в `/seo/schema/` — имплементирай в Summer Cart templates
- Redirect CSV е в `/seo/redirects/redirects-master.csv` — това е source of truth за Cloudflare Bulk Redirects
- Canonical и indexing rules са в `/seo/rules/` — спазвай при custom development

### За Content Team
- Page structure templates са в `/seo/templates/page-structure/` — спазвай структурата
- AI prompts са в `/seo/prompts/` — ползвай само за draft assist, задължителен human review
- Content brief template е в `/seo/templates/content-briefs/BRIEF-TEMPLATE.md`

---

## Branching Strategy

```
main          → Approved, production SEO rules (защитен branch)
develop       → Работа в прогрес
feature/*     → feature/new-ingredient-pages, fix/redirect-cleanup
```

**Всяка промяна → Pull Request → SEO Manager review → merge в main**

---

## Versioning

- Git tags за major taxonomy промени: `v1.0`, `v2.0`
- Minor updates: `v1.1`, `v1.2`
- Changelog: `/docs/changelog.md`

---

## Технологичен стек

| Слой | Роля |
|------|------|
| **Summer Cart** | E-commerce платформа — products, categories, checkout |
| **GitHub (този repo)** | SEO governance — rules, templates, taxonomy, prompts |
| **Cloudflare** | Edge layer — redirects, cache, performance, security |
| **OpenAI** | Controlled assist — FAQ drafts, meta suggestions, clustering |

---

## Контакти и ownership

- SEO Manager: _[добави имейл]_
- Developer: _[добави имейл]_
- Content Lead: _[добави имейл]_
