# Redirect Rules — angelcosmetics.bg

## Принцип

Redirects са необратими от SEO гледна точка — един 301 redirect прехвърля link equity, но изтрива историята на стария URL за Google. Затова трябва да са планирани, документирани и тествани преди прилагане.

**Source of truth:** `/seo/redirects/redirects-master.csv`

---

## Кога се прави 301 Redirect

| Ситуация | Действие |
|----------|---------|
| Продукт е discontinued (спрян завинаги) | 301 → близък продукт или категория |
| URL структура се сменя | 301 → нов URL |
| Категория се rename | 301 → нов slug |
| Два продукта се merge | 301 → surviving product |
| Seasonal page след събитие | 301 → /promotions/ или noindex |
| Бранд промени официалното си название | 301 → нов brand slug |
| Typo в slug се коригира | 301 → corrected URL |

## Кога се прави 302 Redirect (временен)

| Ситуация | Действие |
|----------|---------|
| A/B тест на нова URL структура | 302 (не прехвърля equity) |
| Временна maintenance страница | 302 |
| Продуктова страница по времена работа | 302 |

**По default: 301. 302 само при ясна причина.**

---

## Кога НЕ се прави Redirect

| Ситуация | Правилното действие |
|----------|-------------------|
| Временно изчерпан продукт | Запази page + INDEX + "временно изчерпан" UI |
| Page с ниски rankings | Подобри съдържанието, не redirect |
| Duplicate content | Canonical tag, не redirect (освен ако ще премахнеш страницата) |
| Blog article с малко трафик | Подобри или noindex, не redirect |

---

## Redirect Chain Prevention

**Redirect chain:** A → B → C (три хопа)

Google следва redirect chains, но губи equity с всеки hop. PageSpeed и crawl budget страдат.

**Правило:** При добавяне на нов redirect:
1. Провери дали new_url вече е в old_url колоната
2. Ако да → обнови до финалната дестинация (A → C директно)
3. Никога не redirect-вай към redirect

---

## Workflow за Добавяне на Redirect

```
1. Идентифицирай нуждата от redirect
2. Определи: 301 или 302?
3. Открий PR в GitHub:
   - Добави ред в redirects-master.csv
   - Попълни всички полета (old_url, new_url, type, reason, date, author)
4. SEO Manager review и одобрение
5. Тест преди production:
   curl -I https://www.angelcosmetics.bg{old_url}
   → Очакван резултат: HTTP 301 с Location header → new_url
6. Import в Cloudflare Bulk Redirects
7. Verify след import
8. Обнови internal links, които сочат към old_url
9. Обнови sitemap ако е нужно
```

---

## Cloudflare Bulk Redirects Import

**Формат за Cloudflare:**

Cloudflare Bulk Redirects изисква пълни URLs (с домейн):

```
Cloudflare format:
  Source URL: https://www.angelcosmetics.bg/old-path/
  Target URL: https://www.angelcosmetics.bg/new-path/
  Status Code: 301
  Preserve query string: No (по default)
  Include subpaths: No (по default, освен ако искаш wildcard)
```

**Import процес:**
1. Вземи `redirects-master.csv`
2. Премахни comment редовете (# lines)
3. Добави домейна към URLs (или ползвай import скрипт)
4. Import в Cloudflare → Traffic → Bulk Redirects → Create Bulk Redirect List

---

## Redirect Monitoring

Проверявай регулярно:
- Google Search Console → Coverage → "Page with redirect" — трябва да намалява
- Screaming Frog crawl → намери redirect chains
- GSC → Crawl stats → намали ли се crawl of redirected URLs

---

## Archive

Retired redirects (URL вече не съществува или е преминала в друг redirect):
- Не изтривай от CSV
- Смени status → `retired`
- В края на годината → move to `/seo/redirects/archive/redirects-{YYYY}.csv`
