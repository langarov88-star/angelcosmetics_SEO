# Summer Cart — Platform SEO Notes

## Какво е Summer Cart

Summer Cart е Bulgarian SaaS e-commerce платформа. Тези notes документират нейните native SEO capabilities и ограничения, за да не предполагаме функционалност, която не съществува.

**ВАЖНО:** Тази документация трябва да се верифицира с конкретната версия/конфигурация на инсталацията на angelcosmetics.bg. Маркирани са неща, които изискват проверка.

---

## Native SEO Features (Използвай директно)

### ✅ Потвърдени native features

| Feature | Статус | Notes |
|---------|--------|-------|
| Custom meta title per page | Native | Достъпно в admin за product, category, brand, blog pages |
| Custom meta description per page | Native | Достъпно в admin |
| URL slug customization | Native | Провери дали е само slug или пълен path |
| XML Sitemap auto-generation | Native | **Верифицирай:** дали изключва noindex pages |
| Robots.txt access | Native | Достъпен за редактиране от admin |
| Breadcrumb navigation | Native | **Верифицирай:** дали генерира schema markup |
| Blog module | Native | Поддържа blog articles |
| Category pages | Native | Tier 1 и Tier 2 категории |
| Brand pages | Native | Brand listings |
| Product tags/labels | Native | За "Ново", "Промоция" и подобни |
| 301 redirects | Native (ограничено) | Прости случаи — Cloudflare за bulk |

### ⚠️ Неверифицирано — изисква проверка

| Feature | Какво да провериш |
|---------|-------------------|
| Canonical tag support | Per-page canonical или само глобален? |
| Noindex per page | Може ли да се сложи noindex на конкретна страница? |
| Filter URL handling | Генерира ли уникални URLs при филтриране? |
| Pagination canonical | Слага ли canonical на page 2+? |
| Schema markup output | Какъв JSON-LD генерира нативно? Валиден ли е? |
| Hreflang | Нужно ли е в бъдеще? |

---

## Custom Development Layer

Следните функции НЕ са native и изискват custom development:

### [CUSTOM DEV] Задължителни за SEO системата

```
1. FAQ block per page type
   - Summer Cart вероятно няма модул за FAQ blocks per page
   - Решение: Custom template section или ACF-like field в admin

2. FAQPage schema JSON-LD
   - Auto-генерация от FAQ съдържанието
   - Inject в <head> per page

3. Ingredient tag system
   - Products tagged с ingredients (e.g., "retinol", "niacinamide")
   - Ingredient pages пулят products по тази tag

4. Skin concern tag system
   - Products tagged по skin concern (e.g., "oily-skin", "anti-aging")
   - Problem pages пулят products по concern tag

5. Noindex на filter/sort URLs
   - Ако Summer Cart не поддържа — необходим е template modification
   - Алтернатива: Cloudflare Worker за X-Robots-Tag header

6. Advanced canonical per URL type
   - Per-page canonical за filter combinations
   - Ако не е native — custom template hook

7. Problem/Routine pages (Landing pages)
   - Ако Summer Cart няма flexible content builder
   - Решение: Custom page type или static HTML inject

8. JSON-LD schema inject per page type
   - Product, FAQPage, BreadcrumbList, Article, HowTo
   - Ако native schema е невалиден — custom override в templates
```

---

## Какво НЕ Трябва да се Пипа директно в Платформата

| Действие | Риск | Алтернатива |
|----------|------|-------------|
| Смяна на URL структурата без redirect plan | Загуба на link equity, 404 errors | Redirect first, после URL смяна |
| Изключване на native sitemap без замяна | Googlebot не намира pages | Подготви нов sitemap преди |
| Промяна на canonical logic глобално | Може да афектира всички pages | Тествай на staging |
| Директна редакция на robots.txt без review | Може да noindex важни pages | PR review задължителен |

---

## Препоръчан Workflow: Platform + Custom Dev

```
Summer Cart Native           Custom Dev Layer
─────────────────           ─────────────────
Meta title/desc fields   →  Попълват се по templates от GitHub
URL slugs               →  По taxonomy rules от GitHub
Product data            →  Тагнати с ingredient/concern tags [CUSTOM]
Native breadcrumbs      →  + BreadcrumbList schema [CUSTOM]
Native product data     →  + Product JSON-LD [CUSTOM validate/override]
Blog module             →  + Article schema [CUSTOM]
Native redirects        →  За прости 301-и; bulk → Cloudflare
```

---

## Въпроси за Developer (Проверка)

Преди имплементация на SEO системата, developer трябва да отговори на:

1. Каква е пълната URL структура, генерирана от Summer Cart за products?
   - Имаме ли `/category/brand/product` и `/product` едновременно?

2. Генерира ли Summer Cart session IDs или query параметри в URLs?

3. Каква schema markup генерира нативно — и валидна ли е?

4. Може ли да се добавят custom meta tags (noindex, canonical) per page?

5. Какъв е механизмът за custom template injection (за schema JSON-LD)?

6. Поддържа ли платформата staging environment за тестване?
