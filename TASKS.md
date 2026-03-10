# SECTION 14: PRIORITIZED ACTION LIST — Първите 20 Задачи
### angelcosmetics.bg — SEO & DEV Roadmap

> Последна актуализация: 2026-03-10

---

## Легенда
🔴 СЕГА | 🟡 WEEK 2 | 🟠 MONTH 1 | ⚫ MONTH 2

| Статус | Значение |
|--------|----------|
| ✅ | Завършена |
| 🔄 | В процес |
| ⏳ | Чака предпоставка |
| ☐ | Не е започната |

---

## 🔴 СЕГА — Критични задачи

| # | Задача | Тип | Impact | Effort | Статус |
|---|--------|-----|--------|--------|--------|
| 1 | **Audit на текущи indexed pages** — намери дубликати, thin pages, filter URLs | SEO | HIGH | LOW | ⏳ Чака GSC |
| 2 | **Robots.txt** — disallow search, filter, sort параметри | DEV | HIGH | LOW | ✅ Завършена |
| 3 | **Noindex** на filter/sort/search result pages | DEV | HIGH | LOW | ✅ Завършена |
| 4 | **XML Sitemap** — провери и изчисти (само indexed pages) | SEO + DEV | HIGH | LOW | ✅ Завършена |
| 5 | **GitHub repo setup** — structure, initial docs, taxonomy | SEO + DEV | HIGH | MEDIUM | ✅ Завършена |
| 6 | **Cloudflare cache rules** — setup per page type | CLOUDFLARE | HIGH | MEDIUM | ✅ Завършена |
| 7 | **Canonical tags** — product pages, category variants | DEV | HIGH | MEDIUM | ✅ Завършена |

---

## 🔴 CLOUDFLARE PERFORMANCE — Сесия 2026-03-08

| # | Задача | Тип | Impact | Effort | Статус |
|---|--------|-----|--------|--------|--------|
| 6a | **Cloudflare Pro upgrade** — план $20/мес активиран | CLOUDFLARE | HIGH | LOW | ✅ Завършена |
| 6b | **Cache Rules (6 правила)** — BYPASS cart/checkout/account/wishlist + search/filters; CACHE static (1г), products (24ч), categories (12ч), homepage (2ч) | CLOUDFLARE | HIGH | MEDIUM | ✅ Завършена |
| 6c | **Polish + WebP** — автоматична компресия и конвертиране на снимки (~60% по-малки) | CLOUDFLARE | HIGH | LOW | ✅ Завършена |
| 6d | **Super Bot Fight Mode** — блокиране на ~63k бот заявки/ден (США, Китай, др.) | CLOUDFLARE | HIGH | LOW | ✅ Завършена |
| 6e | **Cache Hit Rate мониторинг** — провери Analytics след 48ч, цел: >75% | CLOUDFLARE | HIGH | LOW | ⏳ Чака 48ч |

---

## 🟡 WEEK 2

| # | Задача | Тип | Impact | Effort | Статус |
|---|--------|-----|--------|--------|--------|
| 8 | **Product schema validation** за всички product pages | DEV | HIGH | MEDIUM | ✅ Завършена |
| 9 | **URL taxonomy** документация в GitHub | SEO | HIGH | MEDIUM | ✅ Завършена |
| 10 | **Top 5 category pages** — добави editorial intro copy | CONTENT | HIGH | MEDIUM | ☐ |

---

## 🟠 MONTH 1

| # | Задача | Тип | Impact | Effort | Статус |
|---|--------|-----|--------|--------|--------|
| 11 | **Top 10 brand pages** — добави editorial content (250+ думи) | CONTENT | HIGH | HIGH | ☐ |
| 12 | **Redirects master CSV** — документирай всички съществуващи 301-и | SEO | MEDIUM | LOW | ☐ |
| 13 | **Cloudflare Bulk Redirects** — import от CSV | CLOUDFLARE | MEDIUM | LOW | ☐ |
| 14 | **Top 5 Problem Pages** — пълен content и internal links | CONTENT + SEO | HIGH | HIGH | ☐ |
| 15 | **Breadcrumb schema** на всички page types | DEV | MEDIUM | MEDIUM | ☐ |

---

## ⚫ MONTH 2

| # | Задача | Тип | Impact | Effort | Статус |
|---|--------|-----|--------|--------|--------|
| 16 | **Organization + WebSite schema** на Home | DEV | MEDIUM | LOW | ☐ |
| 17 | **FAQPage schema** — имплементирай на Problem + ingredient pages | DEV | MEDIUM | MEDIUM | ☐ |
| 18 | **Content brief template** в GitHub | SEO | MEDIUM | LOW | ☐ |
| 19 | **AI prompt library** — FAQs, meta desc, category, copy | AI / OPENAI | MEDIUM | MEDIUM | ☐ |
| 20 | **Keyword map** — документирай primary KW за всяка важна page | SEO | HIGH | MEDIUM | ☐ |

---

## Прогрес

\`\`\`
Завършени:  12 / 25  (48%)
В процес:    0 / 25
Чакащи:     13 / 25

── Cloudflare сесия 2026-03-08 ──────────────────────────
✅ Pro план активиран
✅ 6 Cache Rules конфигурирани (BYPASS + CACHE)
✅ Polish + WebP включен
✅ Super Bot Fight Mode активиран (~63k бота/ден блокирани)
⏳ Cache Hit Rate проверка → след 48ч (цел: >75%)

── SEO сесия 2026-03-10 ─────────────────────────────────
✅ Task 9: URL taxonomy документация → seo/taxonomy/url-taxonomy.md
\`\`\`
