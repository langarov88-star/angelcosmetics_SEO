/**
 * Cloudflare Worker — Sitemap Server for angelcosmetics.bg
 *
 * Intercepts requests to /sitemap-*.xml and serves files from R2 bucket.
 * Files in R2: sitemap-index.xml, sitemap-products.xml,
 *              sitemap-categories.xml, sitemap-static.xml, sitemap-bg-only.xml
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Only handle sitemap requests
    const SITEMAP_FILES = [
      "/sitemap-index.xml",
      "/sitemap-products.xml",
      "/sitemap-categories.xml",
      "/sitemap-static.xml",
      "/sitemap-bg-only.xml",
    ];

    // Intercept robots.txt and serve corrected version with our sitemap
    if (path === "/robots.txt") {
      const ROBOTS = `User-agent: semrushbot
Disallow: /

User-agent: dotbot
Disallow: /

User-agent: ahrefsbot
Disallow: /

User-agent: DataForSeoBot
Disallow: /

User-agent: *
Disallow: /admin/
Disallow: /ajax/
Disallow: /skins/
Disallow: /search
Disallow: /search/
Disallow: /*?q=*
Disallow: /*?sort=*
Disallow: /*?order=*
Disallow: /*?filter=*
Disallow: /*?page=*
Disallow: /*?ref=*
Disallow: /cart/
Disallow: /checkout/
Disallow: /account/
Disallow: /wishlist/

Sitemap: https://angelcosmetics.bg/sitemap-index.xml
`;
      return new Response(ROBOTS, {
        headers: {
          "Content-Type": "text/plain; charset=utf-8",
          "Cache-Control": "public, max-age=86400",
        },
      });
    }

    if (!SITEMAP_FILES.includes(path)) {
      // Pass all other requests to the origin (Summer Cart)
      return fetch(request, { redirect: "manual" });
    }

    // Strip leading slash to get R2 object key
    const key = path.slice(1);

    const object = await env.SITEMAPS.get(key);

    if (!object) {
      return new Response(`Sitemap not found: ${key}`, { status: 404 });
    }

    return new Response(object.body, {
      headers: {
        "Content-Type": "application/xml; charset=utf-8",
        "Cache-Control": "public, max-age=3600",
        "X-Robots-Tag": "noindex",
      },
    });
  },
};
