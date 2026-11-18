# Page copy for the possjonah.com book pages. Facts come from the books themselves
# and their Amazon.com listings (read Nov 18, 2026). No reviews, ratings, awards,
# sales figures or curriculum-standard claims.

def book_page(page, H, key, title, desc, h1, lede, intro_extra, gallery_title, gallery_items, sections, faq, related, extra_buttons=""):
    b = H["BOOKS"][key]
    url = H["book_url"](key)
    trail = [("Home", "/"), ("Books", "/books.html"), (b["short"], url)]
    cover_alt = f'{b["short"]} by Poss Jonah, {b["fmt"].lower()} front cover'
    facts = [f'{b["fmt"]}, {b["pages"]} pages', b["size"], f'Ages / level: {b["age"]}', "By Poss Jonah"]
    if b.get("isbn"): facts.append(f'ISBN-13: {b["isbn"]}')
    hero = (f'<div class="hero"><div>{H["img"]("covers/"+b["cover"], cover_alt, eager=True)}</div><div>'
            f'<p class="lede">{lede}</p>{intro_extra}'
            f'<div class="buybox">{H["price_line"](b)}{H["buy"](b["asin"], "Buy the " + b["fmt"].lower() + " on Amazon")}{extra_buttons}'
            f'<ul class="facts">' + "".join(f"<li>{x}</li>" for x in facts) + '</ul></div></div></div>')
    rel = '<h2>More Poss Jonah books families pair with this one</h2>' + H["grid"]([H["card"](k) if k != "bilingual" else H["bilingual_card"]() for k in related])
    gal = (f'<h2>{gallery_title}</h2>' + H["gallery"](gallery_items)) if gallery_items else f'<h2>{gallery_title}</h2>'
    body = (H["crumbs_html"](trail) + f'<h1>{h1}</h1>' + hero + gal + sections +
            f'<div class="buybox">{H["price_line"](b)}{H["buy"](b["asin"], "Get " + b["short"] + " on Amazon")}{extra_buttons}</div>' +
            H["faq_html"](faq) + rel)
    imgs = ["/img/books/covers/" + b["cover"] + ".webp"] + ["/img/books/" + g[0] + ".webp" for g in gallery_items[:4]]
    og = {"nbc": "/book-B0HRR7WZMG.jpg", "renewed": "/book-B0HRRXTFL8.jpg"}.get(key, "/img/books/covers/" + b["cover"] + ".webp")
    ld = [H["book_ld"](b, url, imgs), H["crumbs_ld"](trail), H["faq_ld"](faq)]
    return page(url[1:], title, desc, og, body, ld, og_type="book")

from content_nbc import build_nbc, build_renewed
from content_books import build_books
from content_landing import build_landing

def build(page, H):
    out = []
    out += build_nbc(page, H, book_page)
    out += build_renewed(page, H, book_page)
    out += build_books(page, H, book_page)
    out += build_landing(page, H)
    return out
