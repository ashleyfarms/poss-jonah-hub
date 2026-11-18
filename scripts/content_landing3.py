# Christmas gift guide and the books hub (books.html).
from content_landing import collection_ld

def christmas(page, H):
    card, grid = H["card"], H["grid"]
    url = "/christian-christmas-gifts.html"; trail = [("Home", "/"), ("Books", "/books.html"), ("Christian Christmas gifts", url)]
    faq = [("Will it arrive before Christmas?", "Amazon handles shipping. On Nov 18, 2026, Amazon listed The Night Before Christmas as usually shipping within 8 days and Renewed Every Morning within 9 days. The paperbacks showed as in stock. Always check the delivery date at checkout."),
           ("Can I gift-wrap it?", "Amazon offers gift options at checkout, including a gift message and gift wrap on eligible items."),
           ("Which book is best for a young child?", "The Night Before Christmas hardcover. It pairs the classic poem with the nativity story and is listed for ages 3–8."),
           ("What about a gift for a woman?", "Renewed Every Morning, a 365-day Bible verse devotional in hardcover.")]
    body = (H["crumbs_html"](trail) +
      '<h1>Christian Christmas Gifts: Nativity Books, Devotionals and Stocking Stuffers</h1>'
      '<p class="lede">Gifts that keep Christ in Christmas. There\'s a hardcover nativity picture book for the kids, a daily Bible verse devotional for the women in your life, and stocking stuffers under $11 for homeschoolers and young artists. Every book links straight to Amazon, which ships it and offers gift options at checkout.</p>'
      '<div class="note"><b>Order early:</b> On Nov 18, 2026, Amazon listed The Night Before Christmas as “usually ships within 8 days” and Renewed Every Morning as “usually ships within 9 days.” The paperbacks below showed as in stock. Check the delivery date at checkout.</div>'
      '<h2>For children: a nativity Christmas book they\'ll ask for every year</h2>'
      '<p>The Night Before Christmas hardcover gives kids the poem they\'ll hear everywhere, then tells the true story of Jesus\' birth from the Bible. It\'s an 8.25 × 11 inch gift book with 78 full-color pages, a natural pick for Christmas Eve, a baptism or dedication gift, or a grandparent\'s gift.</p>'
      + H["gallery"]([("nbc/p19", "Santa Zeb with a white beard in his sleigh, from the Christmas picture book", "The poem: Santa Zeb in his sleigh."),
                      ("nbc/p60", "Nativity scene with Mary, Joseph and baby Jesus in the manger", "The nativity: the manger (Luke 2:7).")]) +
      grid([card("nbc")]) +
      '<h2>For mom, grandma, a teacher or a friend: a daily devotional</h2>'
      '<p>Renewed Every Morning is a compact hardcover with a Bible verse, reflection and prayer for every date. She can start the day it\'s unwrapped, and it makes a gentle New Year gift too.</p>'
      + grid([card("renewed")]) +
      '<h2>Stocking stuffers under $11</h2>'
      '<p>Paperbacks for homeschoolers, young readers and coloring fans, at Amazon prices on ' + H["PRICE_DATE"] + ':</p>'
      + grid([card("hcolor"), card("counting"), card("math1"), card("holler"), card("states"), card("birds"), card("davey")]) +
      '<h2>Gift ideas by person</h2>'
      '<table><tr><th>For</th><th>Pick</th></tr>'
      '<tr><td>Ages 3–8</td><td><a href="/night-before-christmas-nativity-picture-book.html">The Night Before Christmas</a> plus the <a href="/possum-holler-coloring-book.html">Possum Holler Coloring Book</a></td></tr>'
      '<tr><td>A homeschool family</td><td><a href="/kindergarten-counting-workbook-math-with-poss.html">Counting 1–20</a>, <a href="/first-grade-math-workbook-adding-subtracting.html">Adding &amp; Subtracting</a>, or <a href="/50-states-and-capitals-homeschool-workbook.html">All 50 States</a></td></tr>'
      '<tr><td>A young bird watcher or beach lover</td><td><a href="/birds-of-the-american-south-coloring-book.html">Birds of the American South</a> or <a href="/florida-marine-life-coloring-book-captain-davey.html">Florida marine life</a></td></tr>'
      '<tr><td>A bilingual family</td><td><a href="/bilingual-spanish-french-tagalog-bird-books.html">English–Spanish, French or Tagalog bird book</a></td></tr>'
      '<tr><td>Mom, grandma, a teacher, a pastor\'s wife</td><td><a href="/renewed-every-morning-daily-devotional-for-women.html">Renewed Every Morning</a></td></tr>'
      '<tr><td>A teen who loves mysteries</td><td><a href="/cryptid-coloring-book-well-thats-weird.html">Well, That\'s Weird! Cryptid Coloring Book</a></td></tr></table>'
      + H["faq_html"](faq))
    keys = ["nbc", "renewed", "hcolor", "counting", "math1", "holler", "states", "birds", "davey"]
    ld = [collection_ld(H, "Christian Christmas Gifts: Nativity Books, Devotionals and Stocking Stuffers", url, keys), H["crumbs_ld"](trail), H["faq_ld"](faq)]
    return page(url[1:], "Christian Christmas Gifts for Kids & Women: Nativity Book, Devotional, Stocking Stuffers",
        "Christian Christmas gift ideas: a nativity picture book hardcover for kids, a 365-day Bible verse devotional for women, and homeschool stocking stuffers under $11. Ships from Amazon.",
        "/book-B0HRR7WZMG.jpg", body, ld)

def feature(H, key, thumbs, text):
    b = H["BOOKS"][key]; u = H["book_url"](key)
    ims = "".join(H["img"](r, a) for r, a in thumbs)
    return (f'<div class="feature"><div><h3><a href="{u}">{b["title"]}</a></h3><p class="meta">{b["genre"]} · {b["fmt"]} · {b["pages"]} pages</p>'
            f'{text}{H["price_line"](b)}{H["buy"](b["asin"], "Buy the " + b["fmt"].lower() + " on Amazon")}'
            f'<a class="buy alt" href="{u}">See inside &amp; read more</a></div><div class="thumbs">{ims}</div></div>')

def hub(page, H):
    card, grid = H["card"], H["grid"]
    url = "/books.html"; trail = [("Home", "/"), ("Books", url)]
    faq = [("Where do I buy Poss Jonah books?", "On Amazon. Every buy button opens the book's Amazon.com page, and Amazon prints, sells, ships and handles returns."),
           ("Who is Poss Jonah?", "Poss Jonah is a possum storyteller from Possum Holler, the character behind these books and the Poss Jonah videos. See the <a href=\"/about.html\">About page</a>."),
           ("Are the prices on this site current?", "Prices shown were read from Amazon on " + H["PRICE_DATE"] + ". Amazon shows the current price at checkout."),
           ("Can I see inside the books?", "Yes. Each book's page here shows real inside pages.")]
    body = (H["crumbs_html"](trail) +
      '<h1>Poss Jonah Books: Christian, Homeschool &amp; Christmas Books for Kids and Families</h1>'
      '<p class="lede">Christian Christmas picture books, a daily Bible verse devotional for women, homeschool math and geography workbooks, nature-study coloring books, and bilingual editions, all from Poss Jonah. See real inside pages for each book, then buy straight from Amazon.</p>'
      '<p><a class="pill" href="/homeschool-books.html">📚 Homeschool books</a><a class="pill" href="/christian-books-for-kids-and-families.html">✝️ Christian books</a><a class="pill" href="/christian-christmas-gifts.html">🎄 Christmas gifts</a><a class="pill" href="/coloring-pages.html">🖍️ Free coloring pages</a></p>'
      '<div class="note"><b>Christmas ordering:</b> On Nov 18, 2026, Amazon listed the two hardcovers as usually shipping within 8–9 days. Order soon if a copy is meant to be under the tree.</div>'
      '<h2 id="christmas"><span id="nbc"></span>Christian Christmas hardcover</h2>'
      '<p>Moore\'s classic poem, followed by the story of the first Christmas told from the Bible, in one 78-page hardcover.</p>'
      + feature(H, "nbc", [("covers/nbc", "The Night Before Christmas with Poss Jonah hardcover cover"), ("nbc/p10", "Opening stanza of the Night Before Christmas poem"), ("nbc/p38", "Poss Jonah begins the nativity story for the Holler kids"), ("nbc/p60", "Nativity manger scene with Mary, Joseph and baby Jesus, Luke 2:7")],
          '<p>Part one is Moore\'s poem, word for word, acted out by Santa Zeb and the Possum Holler friends. Part two is 34 painted pages telling the story of Jesus\' birth from the Gospels, with a Scripture reference on each page. It makes a family Christmas Eve read-aloud and an easy Advent devotional.</p>') +
      '<h2 id="renewed"><span id="renewed-book"></span>A daily devotional for women</h2>'
      + feature(H, "renewed", [("covers/renewed", "Renewed Every Morning devotional for women hardcover cover"), ("renewed/p008", "January 1 devotional page, Lamentations 3:22-23"), ("renewed/p050", "February 11 devotional page, Romans 5:8"), ("renewed/p382", "December 25 devotional page")],
          '<p>Every date of the year gets one Bible verse from the World English Bible, a short reflection, and a one-line prayer or phrase to carry. It takes about two minutes, and she can start on any date. It\'s a thoughtful Christmas or New Year gift for moms, grandmothers, teachers and friends.</p>') +
      '<h2 id="workbooks">Homeschool workbooks</h2>'
      '<p>Kindergarten counting, first-grade adding and subtracting, and all 50 states and capitals. <a href="/homeschool-books.html">See the homeschool guide →</a></p>'
      + grid([card("counting"), card("math1"), card("states")]) +
      '<h2 id="holler">Possum Holler stories</h2>'
      '<p>Three read-aloud tales with simple lessons, plus a coloring book of the same stories.</p>'
      + grid([card("holler"), card("hcolor")]) +
      '<h2 id="nature"><span id="birds"></span><span id="captain-davey"></span>Nature study and bilingual books</h2>'
      '<p>Fact pages plus coloring pages for birds of the South and sea creatures of Florida, with bilingual bird editions.</p>'
      + grid([card("birds"), H["bilingual_card"](), card("davey")]) +
      '<h2 id="coloring-more">For teens and grown-ups who like a mystery</h2>'
      + grid([card("cryptid")]) +
      '<h2>About these books</h2>'
      '<p>Every Poss Jonah book is written for families. Little ones get big pictures and simple words, homeschoolers get one-idea-per-page practice, and the Christian books are for parents who want Scripture at the center. The books are printed on demand and sold by Amazon. This site never takes payment; each button opens the book on Amazon.com.</p>'
      + H["faq_html"](faq) +
      '<p style="text-align:center;margin-top:24px"><a class="pill" href="/coloring-pages.html">🖍️ Try free printable coloring pages first →</a></p>')
    keys = ["nbc", "renewed", "counting", "math1", "states", "holler", "hcolor", "birds", "davey", "cryptid"]
    ld = [collection_ld(H, "Poss Jonah Books", url, keys, ("/" + H["BILINGUAL_SLUG"] + ".html", "Birds from Around the World: bilingual editions")),
          H["crumbs_ld"](trail), H["faq_ld"](faq)]
    return page(url[1:], "Poss Jonah Books: Christian Christmas Picture Book, Women's Devotional & Homeschool Workbooks",
        "Books by Poss Jonah: a Christian Christmas nativity picture book, a 365-day Bible verse devotional for women, homeschool math and 50 states workbooks, nature-study coloring books, bilingual editions.",
        "/book-B0HRR7WZMG.jpg", body, ld)
