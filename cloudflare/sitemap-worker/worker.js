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

    if (!SITEMAP_FILES.includes(path)) {
      // Pass all other requests to the origin (Summer Cart)
      return fetch(request);
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
