#!/usr/bin/env python3
"""Generate the possjonah.com book pages (hub, landing pages, one page per book).

Run from the repo root:  python3 scripts/gen_books.py
Writes static HTML into public/. Images live in public/img/books/ (WebP).
Buy buttons go straight to Amazon (tag possjonah-20); nothing is sold on this site.
"""
import json, html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
from books_data import BOOKS, BILINGUAL, BILINGUAL_SLUG, PRICE_DATE, amz
import books_content as C

ROOT = os.path.join(os.path.dirname(__file__), "..", "public")
SITE = "https://possjonah.com"
LASTMOD = "2026-11-18"

def dims(rel):
    im = Image.open(os.path.join(ROOT, "img", "books", rel + ".webp"))
    return im.size

def img(rel, alt, eager=False, cls=""):
    w, h = dims(rel)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="/img/books/{rel}.webp" width="{w}" height="{h}" '
            f'alt="{html.escape(alt, quote=True)}" {load} decoding="async">')

def fig(rel, alt, caption):
    return f'<figure>{img(rel, alt)}<figcaption>{caption}</figcaption></figure>'

def gallery(items):
    return '<div class="gallery">' + "".join(fig(*i) for i in items) + "</div>"

def buy(asin, label="Buy on Amazon", alt=False):
    cls = "buy alt" if alt else "buy"
    return (f'<a class="{cls}" href="{amz(asin)}" rel="sponsored noopener" '
            f'target="_blank">{label}</a>')

def price_line(b):
    return (f'<p class="price">{b["fmt"]} ${b["price"]} <span>Amazon price on {PRICE_DATE}; '
            f'Amazon shows the current price at checkout.</span></p>')

def book_url(key):
    return f"/{BOOKS[key]['slug']}.html"

def card(key, note=None):
    b = BOOKS[key]
    note = note or b["blurb"]
    alt = f'{b["short"]} by Poss Jonah, {b["fmt"].lower()} cover'
    return (f'<article class="card">'
            f'<a href="{book_url(key)}" class="cimg">{img("covers/"+b["cover"], alt)}</a>'
            f'<h3><a href="{book_url(key)}">{html.escape(b["short"])}</a></h3>'
            f'<p class="meta">{b["genre"]} · {b["pages"]} pages · {b["fmt"]}</p>'
            f'<p>{note}</p><p class="cprice">${b["price"]} on Amazon ({PRICE_DATE})</p>'
            f'<a class="more" href="{book_url(key)}">See inside &amp; details</a>'
            f'{buy(b["asin"])}</article>')

def bilingual_card(note=None):
    e = BILINGUAL[0]
    note = note or ("The same 15 birds of the South with every fact in English plus Spanish, "
                    "French or Tagalog. Three editions.")
    return (f'<article class="card">'
            f'<a href="/{BILINGUAL_SLUG}.html" class="cimg">{img("covers/"+e["cover"], "Bilingual English-Spanish bird coloring book by Poss Jonah, cover")}</a>'
            f'<h3><a href="/{BILINGUAL_SLUG}.html">Birds from Around the World: Bilingual Editions</a></h3>'
            f'<p class="meta">Bilingual nature book · 40 pages · Paperback &amp; Kindle</p>'
            f'<p>{note}</p><p class="cprice">$10.99 paperback on Amazon ({PRICE_DATE})</p>'
            f'<a class="more" href="/{BILINGUAL_SLUG}.html">See inside &amp; editions</a>'
            f'{buy(e["asin"], "Buy Spanish edition")}</article>')

def grid(cards):
    return '<div class="grid">' + "".join(cards) + "</div>"

def faq_html(faq):
    return '<section class="faq"><h2>Questions families ask</h2>' + "".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq) + "</section>"

def faq_ld(faq):
    import re
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": strip(q),
                            "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faq]}

def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
                                for i, (n, u) in enumerate(trail)]}

def crumbs_html(trail):
    parts = [f'<a href="{u}">{html.escape(n)}</a>' for n, u in trail[:-1]] + [html.escape(trail[-1][0])]
    return '<nav class="crumbs" aria-label="Breadcrumb">' + " › ".join(parts) + "</nav>"

def book_ld(b, url, images, extra_editions=None):
    author = {"@type": "Person", "name": "Poss Jonah", "url": SITE + "/about.html"}
    def edition(fmt, asin, price=None, isbn=None, pages=None):
        e = {"@type": "Book", "bookFormat": "https://schema.org/" + ("Hardcover" if fmt == "Hardcover" else "Paperback" if fmt == "Paperback" else "EBook"),
             "url": amz(asin)}
        if isbn: e["isbn"] = isbn
        if pages and fmt != "Kindle": e["numberOfPages"] = pages
        if price:
            e["offers"] = {"@type": "Offer", "price": price, "priceCurrency": "USD",
                           "url": amz(asin), "seller": {"@type": "Organization", "name": "Amazon.com"}}
        return e
    eds = [edition(b["fmt"], b["asin"], b["price"], b.get("isbn"), b["pages"])]
    if b.get("kindle"): eds.append(edition("Kindle", b["kindle"]))
    eds += extra_editions or []
    d = {"@context": "https://schema.org", "@type": "Book", "name": b["title"], "author": author,
         "url": SITE + url, "image": [SITE + i for i in images], "description": b["blurb"],
         "inLanguage": "en", "datePublished": b["pub"], "genre": b["genre"],
         "publisher": {"@type": "Organization", "name": "Independently published"},
         "workExample": eds}
    if b.get("age") and "year" in b["age"]:
        lo, hi = b["age"].split(" ")[0].replace("–", "-").split("-")
        d["typicalAgeRange"] = f"{lo}-{hi}"
    return d

CSS = """*{box-sizing:border-box}body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;margin:0;color:#1d2433;background:#fffaf0;line-height:1.6;font-size:17px}
.wrap{max-width:980px;margin:0 auto;padding:0 16px 56px}
nav.top{display:flex;align-items:center;gap:6px 14px;padding:12px 0;border-bottom:2px solid #ff9a2e;font-size:.95rem;flex-wrap:wrap}
nav.top a{color:#8a4b00;font-weight:600;text-decoration:none}
nav.top .home{display:flex;align-items:center;gap:8px;color:#1d2433;font-weight:800;margin-right:auto}
nav.top .home img{width:36px;height:36px}
.crumbs{font-size:.85rem;color:#6a6f7d;margin:12px 0 0}.crumbs a{color:#8a4b00}
h1{font-size:clamp(1.7rem,5.5vw,2.5rem);line-height:1.15;margin:18px 0 10px}
h2{font-size:1.35rem;line-height:1.25;margin:36px 0 12px;padding-left:10px;border-left:5px solid #ff9a2e}
h3{font-size:1.08rem;line-height:1.3;margin:22px 0 6px}
p,li{max-width:46em}a{color:#8a4b00}
.lede{font-size:1.12rem;color:#3a4152}
.hero{display:grid;grid-template-columns:minmax(0,300px) 1fr;gap:24px;align-items:start;margin-top:8px}
.hero img{width:100%;height:auto;border-radius:8px;box-shadow:0 6px 22px rgba(0,0,0,.18);background:#f4ecdf}
.buybox{background:#fff;border:2px solid #f0dcc0;border-radius:16px;padding:16px;margin:14px 0}
.price{font-weight:800;font-size:1.15rem;margin:0 0 6px}.price span{display:block;font-weight:400;font-size:.8rem;color:#6a6f7d}
.facts{list-style:none;padding:0;margin:8px 0 0;font-size:.92rem;color:#3a4152}.facts li{padding:2px 0}
.buy{display:block;text-align:center;background:#ff9a2e;color:#1d2433;font-weight:800;text-decoration:none;padding:14px 16px;border-radius:999px;font-size:1.05rem;margin-top:10px}
.buy:hover,.buy:focus-visible{background:#ffb35c}.buy.alt{background:#fff;border:2px solid #ff9a2e;color:#8a4b00;padding:11px 14px;font-size:.95rem}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px;margin:12px 0}
figure{margin:0;background:#fff;border:1px solid #ecdcc4;border-radius:12px;padding:8px}
figure img{width:100%;height:auto;border-radius:6px;display:block}
figcaption{font-size:.86rem;color:#4a5060;padding:8px 4px 2px;line-height:1.4}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:18px;margin:12px 0}
.card{background:#fff;border:2px solid #f0dcc0;border-radius:16px;padding:14px;display:flex;flex-direction:column}
.card img{width:100%;height:auto;border-radius:6px}.card .cimg img{width:100%;height:auto;border-radius:6px;box-shadow:0 3px 12px rgba(0,0,0,.14);background:#f4ecdf}
.card h3{margin:12px 0 2px}.card h3 a{color:#1d2433;text-decoration:none}
.card p{margin:4px 0;font-size:.9rem;color:#4a5060}.card .meta{font-size:.8rem;color:#8a4b00;font-weight:600}
.card .cprice{font-weight:800;color:#1d2433;margin-top:auto;padding-top:8px}
.card .more{display:block;text-align:center;margin-top:8px;font-weight:700;font-size:.92rem}
.card .buy{padding:11px 12px;font-size:.98rem}
.note{background:#fff4e3;border-left:5px solid #ff9a2e;padding:12px 16px;border-radius:8px;margin:18px 0}
.pill{display:inline-block;background:#fff;border:1px solid #f0dcc0;border-radius:999px;padding:6px 12px;margin:4px 6px 4px 0;font-size:.9rem;text-decoration:none;color:#8a4b00;font-weight:600}
table{border-collapse:collapse;width:100%;font-size:.92rem;margin:10px 0;background:#fff}th,td{border:1px solid #ecdcc4;padding:8px;text-align:left;vertical-align:top}th{background:#fff4e3}
.faq details{background:#fff;border:1px solid #ecdcc4;border-radius:10px;padding:10px 14px;margin:8px 0}.faq summary{font-weight:700;cursor:pointer}
.disc{font-size:.85rem;color:#666}
footer{margin-top:40px;padding-top:14px;border-top:1px solid #e5d3b3;font-size:.86rem;color:#666;text-align:center}
.feature{display:grid;grid-template-columns:1fr 1.2fr;gap:20px;background:#fff;border:2px solid #f0dcc0;border-radius:16px;padding:16px;margin:12px 0}.feature .thumbs{display:grid;grid-template-columns:1fr 1fr;gap:10px}.feature .thumbs img{width:100%;height:auto;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,.12)}.feature h3{margin-top:0;font-size:1.25rem}.feature h3 a{color:#1d2433}
@media(max-width:640px){.feature{grid-template-columns:1fr}.hero{grid-template-columns:1fr}.hero img{max-width:280px;margin:0 auto;display:block}.grid,.gallery{grid-template-columns:1fr 1fr;gap:10px}.card{padding:10px}figcaption{font-size:.8rem}body{font-size:16px}}
"""

NAV = ('<nav class="top"><a class="home" href="/"><img src="/poss-jonah-logo.png" alt="" width="36" height="36">Poss Jonah</a>'
       '<a href="/books.html">Books</a><a href="/homeschool-books.html">Homeschool</a>'
       '<a href="/christian-books-for-kids-and-families.html">Christian books</a>'
       '<a href="/christian-christmas-gifts.html">Christmas gifts</a>'
       '<a href="/coloring-pages.html">Free coloring pages</a><a href="/episodes/">Videos</a><a href="/about.html">About</a></nav>')

FOOT = ('<footer><p>Poss Jonah books are printed and sold by Amazon. Every “Buy” button on this site opens the book’s page on Amazon.com; '
        'nothing is sold or shipped from possjonah.com. As an Amazon Associate I earn from qualifying purchases.</p>'
        '<p><a href="/books.html">All books</a> · <a href="/homeschool-books.html">Homeschool books</a> · '
        '<a href="/christian-books-for-kids-and-families.html">Christian books</a> · <a href="/christian-christmas-gifts.html">Christian Christmas gifts</a> · '
        '<a href="/coloring-pages.html">Free coloring pages</a> · <a href="/about.html">About</a> · <a href="/contact.html">Contact</a> · '
        '<a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a></p>'
        '<nav class="family-sites" aria-label="Family of sites"><p><strong>Family of sites:</strong> <a href="https://shop.possjonah.com">Possum Holler Mercantile</a> · '
        '<a href="https://help-pal-apps.com/">Help-Pal free apps</a> · <a href="https://www.youtube.com/@PossJonah">Poss Jonah on YouTube</a> · '
        '<a href="https://www.youtube.com/@PossJonahKids">Poss Jonah Kids on YouTube</a></p></nav></footer>')

def page(fname, title, desc, og_image, body, ld, og_type="website"):
    url = "/" + fname
    canon = SITE + url
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{canon}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Poss Jonah">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FF9A2E">
<meta name="google-adsense-account" content="ca-pub-9747855263717273">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9747855263717273" crossorigin="anonymous"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-E7PX36SGJE"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-E7PX36SGJE');</script>
{lds}
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
{NAV}
{body}
{FOOT}
</div>
</body>
</html>
"""
    with open(os.path.join(ROOT, fname), "w") as f:
        f.write(doc)
    return url

H = dict(img=img, fig=fig, gallery=gallery, buy=buy, price_line=price_line, card=card, bilingual_card=bilingual_card,
         grid=grid, faq_html=faq_html, faq_ld=faq_ld, crumbs_html=crumbs_html, crumbs_ld=crumbs_ld, book_ld=book_ld,
         book_url=book_url, BOOKS=BOOKS, BILINGUAL=BILINGUAL, BILINGUAL_SLUG=BILINGUAL_SLUG, amz=amz, PRICE_DATE=PRICE_DATE)

if __name__ == "__main__":
    urls = C.build(page, H)
    with open(os.path.join(os.path.dirname(__file__), "book-pages.json"), "w") as f:
        json.dump(urls, f, indent=1)
    print("\n".join(urls))
