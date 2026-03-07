# SEO Changelog — angelcosmetics.bg

Хронологичен лог на всички значими SEO решения. Добавяй нов запис при: taxonomy промени, URL структура промени, major indexing decisions, redirect batches, schema changes.

---

## Format

```
## [v{major}.{minor}] — YYYY-MM-DD
### Added
- Описание на добавеното
### Changed
- Описание на променено
### Fixed
- Описание на поправено
### Removed / Noindexed
- Описание на премахнато
### Redirects
- old_url → new_url (причина)
```

---

## [v1.0] — 2025-03-07

### Added
- Initial SEO governance repository setup
- Full directory structure: rules, taxonomy, templates, schema, prompts, redirects
- SEO strategy overview и onboarding documentation
- Indexing rules matrix
- Canonical rules documentation
- URL naming conventions
- Category taxonomy (Tier 1 + Tier 2)
- Brand list с initial brands
- Ingredient list с top 20 ingredients
- Problem pages list
- Keyword map (initial structure)
- On-page templates за всички page types
- JSON-LD schema templates (Product, FAQPage, BreadcrumbList, Article, Organization, HowTo)
- AI prompt library (6 prompts)
- Redirect master CSV (empty, ready for data)
- Internal linking matrix

### Notes
- Това е foundation версия — всички taxonomy entries трябва да се валидират срещу реалния site
- Brand list и ingredient list изискват попълване с реални данни от магазина
