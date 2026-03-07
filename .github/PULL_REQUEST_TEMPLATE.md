# SEO Change — Pull Request Checklist

## Описание на промяната
<!-- Какво се променя и защо? -->

## Тип промяна
- [ ] Нова страница / page type
- [ ] Промяна в taxonomy / URL структура
- [ ] Redirect (добавяне / промяна)
- [ ] Schema update
- [ ] Template update
- [ ] AI prompt update
- [ ] Rules update
- [ ] Друго: ___________

---

## SEO Checklist

### Ако се добавя нова страница или page type:
- [ ] Дефиниран е primary keyword (уникален, без cannibalization)
- [ ] Страницата е добавена в `/seo/taxonomy/keyword-map.md`
- [ ] Index/noindex решение е документирано в `/seo/rules/indexing-rules.md`
- [ ] Canonical е дефиниран (ако е нужен)
- [ ] Internal links от/към страницата са добавени в `/seo/internal-links/linking-matrix.md`
- [ ] Schema type е определен (Product / FAQ / Article / etc.)

### Ако се сменя URL:
- [ ] 301 redirect е добавен в `/seo/redirects/redirects-master.csv`
- [ ] Redirect е тестван (не loop, не chain)
- [ ] Всички internal links към стария URL са обновени или планирани
- [ ] Sitemap е обновен

### Ако се добавя redirect:
- [ ] old_url и new_url са точни (без trailing slash грешки)
- [ ] Redirect type е 301 (не 302, освен ако не е временен)
- [ ] Reason е попълнен в CSV
- [ ] Не създава redirect chain (A→B→C)

### Ако се обновява schema:
- [ ] JSON-LD е валиден (тествай на https://validator.schema.org)
- [ ] Google Rich Results Test е проверен
- [ ] Цени и наличност са актуални (за Product schema)

### Ако се обновява taxonomy:
- [ ] Cannibalization риск е проверен
- [ ] `keyword-map.md` е обновен
- [ ] Засегнатите breadcrumbs са проверени

---

## Тествано от
- [ ] SEO Manager: ________________
- [ ] Developer (ако има technical changes): ________________

## Deployment notes
<!-- Какво трябва да се направи след merge? (напр. import в Cloudflare, обновяване в Summer Cart, etc.) -->
