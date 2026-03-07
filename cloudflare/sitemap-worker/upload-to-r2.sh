#!/bin/bash
# Upload sitemap XML files to Cloudflare R2
# Requires: wrangler CLI (`npm install -g wrangler`)
# Run from: cloudflare/sitemap-worker/

BUCKET="angelcosmetics-sitemaps"
SITEMAPS_DIR="../../seo/sitemaps/output"

FILES=(
  "sitemap-index.xml"
  "sitemap-products.xml"
  "sitemap-categories.xml"
  "sitemap-static.xml"
  "sitemap-bg-only.xml"
)

for file in "${FILES[@]}"; do
  echo "Uploading $file..."
  wrangler r2 object put "$BUCKET/$file" \
    --file "$SITEMAPS_DIR/$file" \
    --content-type "application/xml"
done

echo "Done. Files uploaded to R2 bucket: $BUCKET"
