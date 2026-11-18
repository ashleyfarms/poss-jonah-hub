# Book catalog for the possjonah.com book pages.
# Titles, ASINs, page counts, ISBNs and prices were read from each live Amazon.com
# product page on Wed Nov 18, 2026. Kindle prices were not shown, so none are listed.
PRICE_DATE = "Nov 18, 2026"

def amz(asin):
    return f"https://www.amazon.com/dp/{asin}?tag=possjonah-20"

BOOKS = {
 "nbc": dict(
  slug="night-before-christmas-nativity-picture-book",
  title="The Night Before Christmas: with Poss Jonah and the Possum Holler Friends",
  short="The Night Before Christmas (hardcover)",
  asin="B0HRR7WZMG", isbn="9798142647412", fmt="Hardcover", pages=78, price="25.99",
  size="8.25 × 11 in", age="3–8 years", pub="2026-11-15", cover="nbc",
  genre="Christian Christmas picture book",
  blurb="Clement Clarke Moore's classic Christmas poem, followed by the story of the first Christmas told from the Bible in words kids can follow. One hardcover gift book, 78 pages.",
 ),
 "renewed": dict(
  slug="renewed-every-morning-daily-devotional-for-women",
  title="Renewed Every Morning: A 365-Day Verse Book for Women",
  short="Renewed Every Morning (hardcover)",
  asin="B0HRRXTFL8", isbn="9798142662576", fmt="Hardcover", pages=396, price="24.99",
  size="5.5 × 8.5 in", age="Adults", pub="2026-11-15", cover="renewed",
  genre="Daily Bible verse devotional for women",
  blurb="A dated hardcover devotional for women: one Bible verse, a short reflection, and a one-line prayer or phrase to carry for every day of the year.",
 ),
 "counting": dict(
  slug="kindergarten-counting-workbook-math-with-poss",
  title="Math with Poss: Counting 1-20 (Kindergarten): A Possum Holler Homeschool Workbook to Trace, Count and Color Numbers 1 to 20",
  short="Math with Poss: Counting 1-20 (Kindergarten)",
  asin="B0HQWH13HL", isbn="9798140789879", fmt="Paperback", pages=76, price="7.99",
  size="8.5 × 11 in", age="3–6 years", pub="2026-11-08", cover="counting",
  genre="Kindergarten math workbook",
  blurb="A kindergarten counting workbook: trace, write, count and color every number from 1 to 20, with ten frames, number words and review pages.",
 ),
 "math1": dict(
  slug="first-grade-math-workbook-adding-subtracting",
  title="Math with Poss: Adding & Subtracting (1st Grade): A Possum Holler Homeschool Workbook for Numbers to 20",
  short="Math with Poss: Adding & Subtracting (1st Grade)",
  asin="B0HNG1PK9F", isbn="9798163210053", fmt="Paperback", pages=54, price="7.25",
  size="8.5 × 11 in", age="6–7 years", pub="2026-10-18", cover="math1",
  genre="1st grade math workbook",
  blurb="A first-grade homeschool math workbook for adding and subtracting within 20: 44 practice pages, a certificate and a 3-page answer key.",
 ),
 "states": dict(
  slug="50-states-and-capitals-homeschool-workbook",
  title="Poss Explores the States: All 50 States & Capitals",
  short="Poss Explores the States: All 50 States & Capitals",
  asin="B0HQWG43C2", isbn="9798140797492", fmt="Paperback", pages=110, price="9.99",
  size="8.5 × 11 in", age="Grades 2–3", pub="2026-11-08", cover="states",
  genre="50 states geography workbook",
  blurb="A homeschool coloring and fact book for grades 2–3: a two-page spread for every state, with its outline to color, its capital to write, and a page of state facts.",
 ),
 "holler": dict(
  slug="possum-holler-picture-book",
  title="Possum Holler: Three Stories from the Holler",
  short="Possum Holler: Three Stories from the Holler",
  asin="B0HMJT12WV", isbn="9798160848808", fmt="Paperback", pages=40, price="9.99",
  size="8.5 × 8.5 in", age="4–8 years", pub="2026-10-07", cover="holler",
  genre="Children's picture book with moral lessons",
  blurb="Three full-color read-aloud tales from Possum Holler, each with a simple lesson: pride, the road back home, and helping a stranger.",
 ),
 "hcolor": dict(
  slug="possum-holler-coloring-book",
  title="Possum Holler Coloring Book: Color the Stories from the Holler",
  short="Possum Holler Coloring Book",
  asin="B0HMJYDD7R", isbn="", fmt="Paperback", pages=74, price="7.99",
  size="8.5 × 11 in", age="4–8 years", pub="2026-10-07", cover="holler-coloring",
  genre="Children's coloring book",
  blurb="Thirty single-sided coloring pages from the three Possum Holler stories, each with a line of the story printed underneath.",
 ),
 "birds": dict(
  slug="birds-of-the-american-south-coloring-book",
  title="Birds from Around the World: The American South: 15 Birds to Meet and Color",
  short="Birds from Around the World: The American South",
  asin="B0HN9CDN1C", isbn="9798163013005", fmt="Paperback", pages=40, price="9.99",
  size="8.5 × 8.5 in", age="4–10 years", pub="2026-10-16", cover="birds",
  kindle="B0HN96ZW3X",
  genre="Bird coloring and nature study book",
  blurb="Fifteen birds of the American South, each with a full-color fact page and a matching coloring page. Built for backyard bird watching and homeschool nature study.",
 ),
 "davey": dict(
  slug="florida-marine-life-coloring-book-captain-davey",
  title="Captain Davey's Marine Life of Florida's Coast: 18 Sea Critters to Meet and Color",
  short="Captain Davey's Marine Life of Florida's Coast",
  asin="B0HP7T4BBQ", isbn="9798165020605", fmt="Paperback", pages=44, price="10.99",
  size="8.5 × 8.5 in", age="4–10 years", pub="2026-10-25", cover="davey",
  kindle="B0H1RWTT59",
  genre="Ocean animal coloring and nature study book",
  blurb="Eighteen sea critters of Florida's coast, each with a full-color fact page and a matching coloring page.",
 ),
 "cryptid": dict(
  slug="cryptid-coloring-book-well-thats-weird",
  title="Well, That's Weird!: Cryptid Coloring Book: 50 Monsters, Mysteries & Legends with Poss Jonah",
  short="Well, That's Weird! Cryptid Coloring Book",
  asin="B0HPZ8R9HZ", isbn="9798166765765", fmt="Paperback", pages=106, price="10.99",
  size="8.5 × 11 in", age="Teens and adults", pub="2026-11-01", cover="cryptid",
  genre="Cryptid and folklore coloring book",
  blurb="Fifty detailed, single-sided illustrations of legendary creatures from around the world, each with a short note on the legend.",
 ),
}

# Bilingual bird editions (one page covers all three)
BILINGUAL = [
 dict(key="es", lang="English–Spanish", native="Aves de todo el mundo: El sur de Estados Unidos",
      title="Birds from Around the World: The American South: Bilingual English-Spanish / Aves de todo el mundo: El sur de Estados Unidos",
      asin="B0HN9BXJZJ", kindle="B0HN9B4GCD", price="10.99", isbn="", pub="2026-10-17", cover="birds-es"),
 dict(key="fr", lang="English–French", native="Oiseaux du monde entier : Le Sud des États-Unis",
      title="Birds from Around the World: The American South: Bilingual English-French / Oiseaux du monde entier : Le Sud des États-Unis",
      asin="B0HNG4R82X", kindle="B0HNF6QX58", price="10.99", isbn="9798163254934", pub="2026-10-18", cover="birds-fr"),
 dict(key="tl", lang="English–Tagalog", native="Mga Ibon Mula sa Buong Mundo: Ang Timog ng Estados Unidos",
      title="Birds from Around the World: The American South: Bilingual English-Tagalog / Mga Ibon Mula sa Buong Mundo: Ang Timog ng Estados Unidos",
      asin="B0HP7B9NNB", kindle="B0HNFPVPPN", price="10.99", isbn="", pub="2026-10-25", cover="birds-tl"),
]
BILINGUAL_SLUG = "bilingual-spanish-french-tagalog-bird-books"
