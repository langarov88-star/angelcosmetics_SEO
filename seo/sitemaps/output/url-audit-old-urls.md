# Одит на стари URL-и — angelcosmetics.bg

**Дата:** 2026-03-07
**Общо стари URL-и в sitemap:** 726

---

## Резюме

| Тип | Брой | SEO Риск | Препоръка |
|-----|------|----------|-----------|
| Стари продуктови `.html` URL-и | 223 | 🔴 Висок — дубликати | 301 Redirect → `/product/ID/slug.html` |
| Стари продуктови URL-и без `.html` | 465 | 🔴 Висок — дубликати | 301 Redirect → `/product/ID/slug.html` |
| Стари категорийни URL-и | 38 | 🟡 Среден | 301 Redirect → `/category/ID/slug.html` или noindex |

**Ключов проблем:** Всички тези URL-и са в sitemap, но Google може да ги индексира като самостоятелни страници — дублирано съдържание с новите `/product/ID/` URL-и.

---

## Тип 1: Стари продуктови URL-и с `.html` (223)

**Характеристики:**
- Структура: `angelcosmetics.bg/slug-на-продукта.html`
- Произход: URL формат преди миграция към Summer Cart
- Риск: Ако нямат 301 redirect, Google вижда 2 версии на един продукт

**Действие:**
1. Провери дали имат 301 redirect → ако да, ИЗКЛЮЧИ от sitemap
2. Ако нямат redirect → добави redirect, после изключи от sitemap

**Пример записи:**
```
https://angelcosmetics.bg/JOICO/innerjoi.html
https://angelcosmetics.bg/academie.html
https://angelcosmetics.bg/adaptirashta-se-osnova-za-grim-gosh-primer-skin-adaptor-chameleon-30ml.html
https://angelcosmetics.bg/alfaparf/cellula-madre.html
https://angelcosmetics.bg/alfaparf/sdl-style-care-stilizanti.html
https://angelcosmetics.bg/alfaparf/sdl-sunshine.html
https://angelcosmetics.bg/alterna-caviar-multiplying-volume-izumitelen-obem.html
https://angelcosmetics.bg/alterna-caviar-replenishing-moisture-udarna-hidratatsia.html
https://angelcosmetics.bg/alterna.html
https://angelcosmetics.bg/alterna/caviar-clinical-densifying-po-gasta-i-zdrava-kosa.html
... (213 още)
```

---

## Тип 2: Стари продуктови URL-и без `.html` (503 от ~439 са продукти)

**Характеристики:**
- Структура: `angelcosmetics.bg/brand-product-name` (без разширение)
- Вероятно: slug URL-и от стара платформа или бранд landing pages

**Действие:**
1. Провери HTTP статус на 20-30 примера
2. Ако → 301: изключи от sitemap
3. Ако → 200 с различно съдържание: добави canonical към `/product/ID/`
4. Ако → 404: изключи веднага от sitemap

**Пример записи (продукти):**
```
https://angelcosmetics.bg/
https://angelcosmetics.bg/
https://angelcosmetics.bg/3deluxe-professional
https://angelcosmetics.bg/Biolage-Professional-Color-Last
https://angelcosmetics.bg/Biolage-Professional-Full-Density 
https://angelcosmetics.bg/Biolage-Professional-Hydra-Source
https://angelcosmetics.bg/Biolage-Professional-Scalp-Sync 
https://angelcosmetics.bg/Biolage-Professional-Volume-Bloom
https://angelcosmetics.bg/Brelil-Anti-Hair-Loss-Terapiq-protiv-kosopad
https://angelcosmetics.bg/Brelil-Hair-Express-za-uskoren-rastej
```

---

## Тип 3: Стари категорийни URL-и (~64)

**Характеристики:**
- Структура: `angelcosmetics.bg/shampoani`, `/balsam-za-kosa` и т.н.
- Смесени: BG slug-ове за категории, EN slug-ове за категории

**Действие:**
1. Ако имат `/category/ID/` еквивалент → 301 redirect
2. Ако са активни landing pages → canonical + noindex или остави но изключи от sitemap

**Пример:**
```
https://angelcosmetics.bg/ampuli-za-kosa
https://angelcosmetics.bg/balsam-za-kosa
https://angelcosmetics.bg/chi-styling
https://angelcosmetics.bg/dush-gel
https://angelcosmetics.bg/echosline-styling
https://angelcosmetics.bg/glineni-maski-za-litse
https://angelcosmetics.bg/grija-za-kojata
https://angelcosmetics.bg/hidratirasha-maska-za-kosa
https://angelcosmetics.bg/hidratirashi-ampuli-za-kosa
https://angelcosmetics.bg/hidratirashti-maski-za-litse
```

---

## Специален проблем: 275 BG URL-и в EN sitemap

В `sitemap 2.txt` (EN sitemap) са открити 275 URL-а БЕЗ `/en/` префикс:

```
https://angelcosmetics.bg/hair-shampoos   ← BG URL в EN sitemap!
https://angelcosmetics.bg/conditioners
https://angelcosmetics.bg/category/242/promotional-offers.html
```

**Проблем:** Google Search Console третира EN sitemap-а като EN ресурс.
BG URL-ите в него объркват crawlera — може да получат грешно hreflang.

**Решение:** Изчисти EN sitemap — остави само `/en/...` URL-и.

---

## Checklist за developer

- [ ] Провери HTTP статус на 30 random стари URL-и (curl batch)
- [ ] Потвърди дали Summer Cart автоматично прави 301 за стари URL-и
- [ ] Ако не → добави redirect rules в `.htaccess` или nginx config
- [ ] Изчисти EN sitemap от BG URL-и (275 броя)
- [ ] Изключи всички стари URL-и от sitemap след верификация
- [ ] Провери GSC Coverage за тези URL-и след промените