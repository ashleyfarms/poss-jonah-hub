# Homeschool and Christian landing pages.
from content_landing import collection_ld

def homeschool(page, H):
    card, grid = H["card"], H["grid"]
    url = "/homeschool-books.html"; trail = [("Home", "/"), ("Books", "/books.html"), ("Homeschool books", url)]
    faq = [("Are these books a complete curriculum?", "No. They're affordable workbooks and nature books that work as a homeschool curriculum supplement, either on their own or next to any program you already use. None of them claim to follow a particular standard."),
           ("Are they Christian?", "The math, states and nature books teach their subjects without Bible lessons. The Night Before Christmas includes the nativity story from Scripture, and Renewed Every Morning is a Bible verse devotional. All of them are made by Poss Jonah, and they fit faith-based homeschools well."),
           ("Where do I buy them?", "Every buy button goes straight to the book's page on Amazon. Amazon prints, sells and ships the books."),
           ("Can I see inside first?", "Yes. Each book's page on this site shows real inside pages.")]
    body = (H["crumbs_html"](trail) +
      '<h1>Homeschool Books &amp; Workbooks from Poss Jonah</h1>'
      '<p class="lede">Simple, friendly homeschool workbooks and nature-study books for preschool through 3rd grade. There are counting and first-grade math workbooks, a 50 states and capitals book, bird and ocean nature studies, and bilingual editions. A Christian Christmas read-aloud and a devotional for mom are on this page too. Every book shows real inside pages, and every buy button goes straight to Amazon.</p>'
      '<p><a class="pill" href="#prek-k">Preschool &amp; K</a><a class="pill" href="#first">1st grade</a><a class="pill" href="#second-third">2nd–3rd grade</a><a class="pill" href="#nature">Nature study</a><a class="pill" href="#language">Foreign language</a><a class="pill" href="#faith">Faith-based learning</a><a class="pill" href="#plan">Sample week</a></p>'
      '<h2 id="prek-k">Preschool &amp; kindergarten: counting, coloring and read-alouds</h2>'
      '<p>At this age, short and cheerful is the goal: one idea per page and lots of coloring. <b>Math with Poss: Counting 1–20</b> is a kindergarten math workbook that walks through every number with tracing, counting and ten frames. The <b>Possum Holler</b> picture book and coloring book make a matching read-then-color pair for narration and fine-motor practice.</p>'
      + grid([card("counting"), card("holler"), card("hcolor")]) +
      '<h2 id="first">1st grade math: adding and subtracting within 20</h2>'
      '<p><b>Math with Poss: Adding &amp; Subtracting</b> is a first grade math workbook with 44 practice pages: ten frames, number lines, make 10, doubles, fact families and story problems, plus an answer key. Do one page a day, four days a week, and you\'ll finish in about 11 weeks. It also makes great summer review.</p>'
      + grid([card("math1"), card("counting")]) +
      '<h2 id="second-third">2nd–3rd grade geography: all 50 states and capitals</h2>'
      '<p><b>Poss Explores the States</b> is a homeschool geography workbook with a two-page spread for every state. Kids color the outline, write the capital, and read about the state bird, flower, nickname, statehood date and fun facts. Two states a week fills a school year.</p>'
      + grid([card("states")]) +
      '<h2 id="nature">Nature study: birds and ocean animals</h2>'
      '<p>Each of these nature study books gives every animal two facing pages: a full-color fact page and a matching coloring page. That suits Charlotte Mason-style nature notebooks, backyard bird watching, and beach-trip learning. One animal a week gives you a 15- or 18-week unit.</p>'
      + grid([card("birds"), card("davey")]) +
      '<h2 id="language">Foreign language: bilingual editions</h2>'
      '<p>The bird book also comes in <b>English–Spanish, English–French and English–Tagalog</b>. Every fact is printed in both languages, a low-pressure way to build vocabulary along with science.</p>'
      + grid([H["bilingual_card"]()]) +
      '<h2 id="faith">Faith-based learning for the whole family</h2>'
      '<p>Many homeschool families start the day in the Word. <b>The Night Before Christmas</b> pairs Moore\'s poem with the nativity story told from the Bible, with a Scripture reference on every nativity page. That makes it a ready-made Advent unit for poetry memorization and Bible memory. <b>Renewed Every Morning</b> is for mom: one verse, a short reflection and a prayer each day, about two minutes before the house wakes up.</p>'
      + grid([card("nbc"), card("renewed")]) +
      '<h2 id="plan">A sample homeschool week using these books</h2>'
      '<table><tr><th>Day</th><th>Morning</th><th>Math</th><th>Afternoon</th></tr>'
      '<tr><td>Mon</td><td>Mom: Renewed Every Morning. Kids: a Possum Holler read-aloud</td><td>One Math with Poss page</td><td>Bird of the week: read the fact page</td></tr>'
      '<tr><td>Tue</td><td>Narrate yesterday\'s story; color the matching page</td><td>Practice page</td><td>Color the bird; watch the feeder</td></tr>'
      '<tr><td>Wed</td><td>Bible memory verse</td><td>One Math with Poss page</td><td>State of the week (older kids)</td></tr>'
      '<tr><td>Thu</td><td>Read-aloud</td><td>Review page</td><td>Bird notes page: draw what you saw</td></tr>'
      '<tr><td>Fri</td><td>Recite the memory verse</td><td>Math game with real objects</td><td>Capitals quiz or nature walk</td></tr></table>'
      '<p>Want to try the style first? Print <a href="/coloring-pages.html">free Possum Holler coloring pages</a>.</p>'
      + H["faq_html"](faq))
    keys = ["counting", "math1", "states", "birds", "davey", "holler", "hcolor", "nbc", "renewed"]
    ld = [collection_ld(H, "Homeschool Books & Workbooks from Poss Jonah", url, keys), H["crumbs_ld"](trail), H["faq_ld"](faq)]
    return page(url[1:], "Homeschool Books & Workbooks: Kindergarten Math, 1st Grade, 50 States, Nature Study | Poss Jonah",
        "Homeschool workbooks and books for preschool–3rd grade: kindergarten counting, 1st grade math, 50 states and capitals, bird and ocean nature study, bilingual and faith-based books.",
        "/img/books/covers/counting.webp", body, ld)

def christian(page, H):
    card, grid = H["card"], H["grid"]
    url = "/christian-books-for-kids-and-families.html"; trail = [("Home", "/"), ("Books", "/books.html"), ("Christian books", url)]
    faq = [("Which Poss Jonah books are Christian books?", "The Night Before Christmas includes a 34-page nativity story told from the Bible, and Renewed Every Morning is a daily Bible verse devotional for women. The Possum Holler stories are gentle moral tales that fit Christian homes, with Bible pairings suggested on their page."),
           ("Which Bible translation do they quote?", "The World English Bible, a public-domain modern English translation."),
           ("Are these good for Sunday school?", "The nativity pages work well for a small group. Each page has a big painting and a Scripture reference to open alongside."),
           ("Where are they sold?", "On Amazon. Every buy button opens the book's Amazon page.")]
    body = (H["crumbs_html"](trail) +
      '<h1>Christian Books for Kids and Families</h1>'
      '<p class="lede">Faith-based books from Poss Jonah. There\'s a Christian Christmas picture book that tells the nativity story from the Bible, a 365-day Bible verse devotional for women, and gentle moral stories from Possum Holler. They\'re made for family devotions, homeschool Bible time, and Sunday school.</p>'
      '<h2>A Christian Christmas book for children: the nativity story</h2>'
      '<p><b>The Night Before Christmas, with Poss Jonah and the Possum Holler Friends</b> starts with Moore\'s classic poem. Then it turns to the reason for the season. Poss gathers the Holler kids by the fire and tells the story of Jesus\' birth across 34 painted pages, from the promises in Isaiah and Micah through Gabriel, Mary and Joseph, the manger, the shepherds, Simeon and Anna, and the wise men. Each page has a Scripture reference and a kid-sized <em>Why it matters</em>.</p>'
      + H["gallery"]([("nbc/p38", "Poss Jonah tells the Holler kids the nativity story around a campfire", "Poss begins the story of the first Christmas."),
                      ("nbc/p60", "Mary holds baby Jesus in the manger scene with Luke 2:7", "The manger, Luke 2:7."),
                      ("nbc/p68", "The wise men visit young Jesus in a children's nativity book", "The wise men, Matthew 2.")]) +
      grid([card("nbc")]) +
      '<h2>A daily devotional for women</h2>'
      '<p><b>Renewed Every Morning</b> gives every date of the year one Bible verse, a short reflection, and a one-line prayer or a phrase to carry. It takes about two minutes. Each month has a theme, from “New mercies” in January to “Light, waiting, and joy” in December. It\'s a thoughtful Christian gift for moms, grandmothers, teachers and friends.</p>'
      + H["gallery"]([("renewed/p008", "January 1 page of a Bible verse devotional for women, Lamentations 3:22-23", "January 1, Lamentations 3:22–23."),
                      ("renewed/p382", "Christmas Day devotional page for women", "December 25.")]) +
      grid([card("renewed")]) +
      '<h2>Moral stories for Christian families</h2>'
      '<p>The <b>Possum Holler</b> tales aren\'t Bible stories, but each one carries a simple lesson. There\'s pride and contentment, a welcome home, and helping a stranger. They pair naturally with Proverbs 16:18, the lost son in Luke 15, and the Good Samaritan in Luke 10. The coloring book lets kids color the scenes while you talk.</p>'
      + grid([card("holler"), card("hcolor")]) +
      '<h2>Ideas for family devotions and Sunday school</h2>'
      '<ul><li><b>Advent:</b> read one nativity section an evening (see the reading plan on <a href="/night-before-christmas-nativity-picture-book.html">the book\'s page</a>).</li>'
      '<li><b>Bible memory:</b> choose one <em>Why it matters</em> line or quoted verse a week.</li>'
      '<li><b>Children\'s church:</b> hold up a nativity painting and read the Bible passage from its reference.</li>'
      '<li><b>Mom\'s quiet time:</b> keep Renewed Every Morning by the coffee pot.</li>'
      '<li><b>Gifts:</b> see the <a href="/christian-christmas-gifts.html">Christian Christmas gift guide</a>.</li></ul>'
      + H["faq_html"](faq))
    ld = [collection_ld(H, "Christian Books for Kids and Families", url, ["nbc", "renewed", "holler", "hcolor"]), H["crumbs_ld"](trail), H["faq_ld"](faq)]
    return page(url[1:], "Christian Books for Kids & Families: Nativity Picture Book, Women's Devotional | Poss Jonah",
        "Christian books for kids and families: a nativity Christmas picture book told from the Bible, a 365-day Bible verse devotional for women, and gentle moral stories for read-aloud.",
        "/book-B0HRR7WZMG.jpg", body, ld)
from content_landing3 import christmas, hub
