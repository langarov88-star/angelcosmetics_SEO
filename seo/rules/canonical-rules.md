# Canonical Rules — angelcosmetics.bg

## Принцип

Canonical тагът казва на Google: "Тази URL е предпочитаната версия на това съдържание."

Правилото е просто: **Всяка indexed страница трябва да има self-canonical. Всяка duplicate/variant страница трябва да има canonical към preferred URL.**

---

## Canonical Matrix по URL тип

| URL тип | Canonical сочи към | Метод |
|---------|-------------------|-------|
| Preferred product URL | Self canonical | Native Summer Cart |
| `/category/brand/product/` | → `/preferred-product-url/` | Custom или Cloudflare |
| `/brand/product/` | → `/preferred-product-url/` | Custom или Cloudflare |
| Filter URL (`?brand=x`) | → Parent category URL | Custom/template |
| Sort URL (`?sort=price`) | → Same page без sort param | Custom/template |
| Pagination page 2+ | → Page 1 (base URL) | Native или custom |
| Search results | → Self (но noindex) | Native |
| Subcategory | Self canonical | Native |
| Brand page | Self canonical | Native |
| Blog article | Self canonical | Native |

---

## Preferred Product URL

Трябва да дефинираш ЕДИН preferred URL pattern за product pages. Избери и документирай:

**Опция A (препоръчана):**
```
/face-care/serums/la-roche-posay-effaclar-duo-plus/
```
Category slug + Product slug

**Опция B:**
```
/products/la-roche-posay-effaclar-duo-plus/
```
Generic /products/ prefix + product slug

**[ACTION REQUIRED]** Верифицирай с developer какъв URL Summer Cart генерира нативно и дефинирай preferred pattern. Запиши решението тук.

**Избран preferred URL pattern:** _[попълни след верификация с developer]_

---

## Duplicate Product URL сценарии

Summer Cart може да генерира product, достъпен от множество paths:

```
Scenario 1:
  /face-care/serums/product-slug/        ← PREFERRED (canonical target)
  /brands/la-roche-posay/product-slug/   ← canonical → preferred
  /product-slug/                         ← canonical → preferred

Scenario 2 (tracking параметри):
  /product-slug/?utm_source=newsletter   ← canonical → /product-slug/ (без params)
  /product-slug/?ref=homepage            ← canonical → /product-slug/ (без params)
```

---

## WWW vs non-WWW

Трябва да е един стандарт. Препоръчително: `https://www.angelcosmetics.bg`

```
Cloudflare → Page Rule или Redirect Rule:
  http://angelcosmetics.bg/* → https://www.angelcosmetics.bg/$1 (301)
  http://www.angelcosmetics.bg/* → https://www.angelcosmetics.bg/$1 (301)
  https://angelcosmetics.bg/* → https://www.angelcosmetics.bg/$1 (301)
```

**[ACTION REQUIRED]** Верифицирай текущия setup и дали е консистентен.

---

## Trailing Slash

Избери едно и бъди консистентен:

**Препоръка:** С trailing slash за categories и pages, без trailing slash за files.

```
✅ /face-care/serums/
✅ /brands/la-roche-posay/
✅ /blog/how-to-build-skincare-routine/
❌ /face-care/serums (без trailing slash → 301 → с trailing slash)
```

**[ACTION REQUIRED]** Верифицирай какво генерира Summer Cart и настрой Cloudflare redirect rule за консистентност.

---

## Как да имплементираш Canonical

### HTML метод (preferred):
```html
<link rel="canonical" href="https://www.angelcosmetics.bg/face-care/serums/product-slug/" />
```

### HTTP Header метод (backup чрез Cloudflare):
```
Link: <https://www.angelcosmetics.bg/face-care/serums/product-slug/>; rel="canonical"
```

---

## Грешки, Които да Избягваш

| Грешка | Последствие |
|--------|-------------|
| Self-canonical, но URL не съвпада точно (http vs https, www vs non-www) | Canonical игнориран |
| Canonical от noindex page | Contradiction — Google игнорира canonical |
| Canonical chain (A→B→C) | Google следва само direct canonicals |
| Canonical към 404 страница | Crawl error |
| Различни canonical на мобилна и desktop версия | Confusion |
| Canonical към redirect | Следва redirect, губи се signal |
