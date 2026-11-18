# Bilingual page, landing pages and the books hub.
SITE = "https://possjonah.com"

def collection_ld(H, name, url, keys, extra=None):
    B = H["BOOKS"]
    items = [{"@type": "ListItem", "position": i + 1, "url": SITE + H["book_url"](k), "name": B[k]["title"]} for i, k in enumerate(keys)]
    if extra:
        items.append({"@type": "ListItem", "position": len(items) + 1, "url": SITE + extra[0], "name": extra[1]})
    return {"@context": "https://schema.org", "@type": "CollectionPage", "name": name, "url": SITE + url,
            "mainEntity": {"@type": "ItemList", "itemListElement": items}}

def build_landing(page, H):
    out = []
    out.append(bilingual(page, H))
    from content_landing2 import homeschool, christian, christmas, hub
    out.append(homeschool(page, H))
    out.append(christian(page, H))
    out.append(christmas(page, H))
    out.append(hub(page, H))
    return out

def bilingual(page, H):
    E = H["BILINGUAL"]; buy = H["buy"]; card = H["card"]
    url = "/" + H["BILINGUAL_SLUG"] + ".html"
    trail = [("Home", "/"), ("Books", "/books.html"), ("Bilingual bird books", url)]
    cards = []
    for e in E:
        cards.append(f'<article class="card">{H["img"]("covers/"+e["cover"], "Bilingual " + e["lang"] + " bird coloring book by Poss Jonah, cover")}'
                f'<h3>{e["lang"]} edition</h3><p class="meta">{e["native"]}</p>'
                f'<p>Paperback, 40 pages, 8.5 × 8.5 in. Kindle edition too.</p><p class="cprice">${e["price"]} paperback on Amazon ({H["PRICE_DATE"]})</p>'
                f'{buy(e["asin"], "Buy paperback on Amazon")}{buy(e["kindle"], "Kindle edition", alt=True)}</article>')
    faq = [("Which languages are available?", "There are three bilingual editions, English with Spanish, French or Tagalog (Filipino). The English-only edition is listed separately."),
           ("How is the second language shown?", "On each color page, every fact is printed in English with the translation right below. The coloring page shows the bird's name in both languages."),
           ("Is it good for kids who don't speak the second language yet?", "Yes. The English is always there, so children can learn new words with a parent and use the pictures as clues."),
           ("What ages?", "Amazon lists 4–10.")]
    body = (H["crumbs_html"](trail) +
      '<h1>Bilingual Bird Books for Kids: English–Spanish, English–French and English–Tagalog</h1>'
      '<p class="lede">The same fifteen birds of the American South as <a href="/birds-of-the-american-south-coloring-book.html">the English edition</a>, with every fact printed in English and a second language. Kids color the bird, learn its name in both languages, and pick up new words along the way.</p>'
      + H["grid"](cards) +
      '<h2>Look inside the bilingual edition</h2>' + H["gallery"]([
        ("birds-bilingual/p003", "Bilingual English Spanish welcome page Howdy from Poss / Saludos de Poss", "<b>Howdy from Poss! / ¡Saludos de Poss!</b> (English–Spanish edition)"),
        ("birds-bilingual/p004", "Northern Cardinal / Cardenal norteño bilingual fact page in English and Spanish", "<b>Northern Cardinal / Cardenal norteño.</b> Facts in English with Spanish below."),
        ("birds-bilingual/p005", "Bilingual coloring page of a Northern Cardinal with English and Spanish names", "<b>Coloring page</b> with the name in both languages."),
        ("birds-bilingual/p018", "Mourning Dove bilingual fact page in English and Spanish", "<b>Mourning Dove / Paloma huilota.</b>"),
        ("birds-bilingual/p019", "Mourning Dove bilingual coloring page", "<b>Mourning Dove to color.</b>"),
        ("birds-bilingual/p035", "Bilingual index of bird names in English and Spanish", "<b>Index / Índice</b> of bird names.")]) +
      '<p class="disc">Sample pages are from the English–Spanish edition. The French and Tagalog editions use the same layout.</p>'
      '<h2>How bilingual and language-learning families use it</h2>'
      '<p><b>Spanish at home:</b> read the English line, then the Spanish, then point to the bird. Over a few weeks kids learn the names of colors, foods and habitats in both languages. Dual-language and Spanish-immersion families can flip it: read the Spanish first.</p>'
      '<p><b>French learners:</b> it\'s a natural fit for French-immersion families and for anyone learning Louisiana or Canadian French. Every fact and every bird name appears in both languages, and the index lists the French names.</p>'
      '<p><b>Filipino-American families:</b> the Tagalog edition lets kids and grandparents read together, each in their own language.</p>'
      '<p><b>Homeschool foreign language:</b> try one bird a week. Say the bird name in both languages, copy one fact into a notebook in the second language, and color the page. That\'s a gentle, low-pressure way to build vocabulary with nature study.</p>'
      + H["faq_html"](faq) + '<h2>More books for homeschool families</h2>' + H["grid"]([card("birds"), card("davey"), card("states")]))
    ldb = {"@context": "https://schema.org", "@type": "Book", "name": "Birds from Around the World: The American South (bilingual editions)",
           "author": {"@type": "Person", "name": "Poss Jonah"}, "url": SITE + url, "inLanguage": ["en", "es", "fr", "tl"],
           "image": [SITE + "/img/books/covers/" + e["cover"] + ".webp" for e in E],
           "workExample": [dict({"@type": "Book", "name": e["title"], "bookFormat": "https://schema.org/Paperback", "numberOfPages": 40, "url": H["amz"](e["asin"]),
                                 "offers": {"@type": "Offer", "price": e["price"], "priceCurrency": "USD", "url": H["amz"](e["asin"])}},
                                **({"isbn": e["isbn"]} if e["isbn"] else {})) for e in E]}
    return page(url[1:], "Bilingual Children's Books: English–Spanish, French & Tagalog Bird Coloring Books",
        "Bilingual bird coloring books for kids in English–Spanish, English–French and English–Tagalog. 15 birds with facts in both languages. Great for homeschool language learning.",
        "/img/books/covers/birds-es.webp", body, [ldb, H["crumbs_ld"](trail), H["faq_ld"](faq)], og_type="book")
