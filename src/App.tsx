import { moreOnTheTrail, verticals, type Vertical } from './data/verticals';

const HELP_PAL_COLLECTION_URL = 'https://help-pal-apps.com/apps/';

function formatList(items: string[]): string {
  if (items.length <= 1) return items[0] ?? '';
  if (items.length === 2) return `${items[0]} and ${items[1]}`;
  return `${items.slice(0, -1).join(', ')}, and ${items[items.length - 1]}`;
}

function VerticalCard({ vertical }: { vertical: Vertical }) {
  const isLive = vertical.status === 'live';
  const className = [
    'vertical-card',
    isLive ? 'vertical-card--live' : 'vertical-card--soon',
    `vertical-card--${vertical.id}`,
  ].join(' ');

  const inner = (
    <>
      <span className="vertical-card__emoji" aria-hidden="true">
        {vertical.emoji}
      </span>
      <div className="vertical-card__body">
        <div className="vertical-card__top">
          <h2>{vertical.name}</h2>
          <span className={isLive ? 'badge badge--live' : 'badge badge--soon'}>
            {isLive ? 'Live' : 'Coming soon'}
          </span>
        </div>
        <p className="vertical-card__scope">{vertical.scope}</p>
        <p className="vertical-card__blurb">{vertical.blurb}</p>
        {isLive ? (
          <span className="vertical-card__go">Come on in →</span>
        ) : (
          <span className="vertical-card__wait">Hang tight, y’all.</span>
        )}
      </div>
    </>
  );

  if (isLive && vertical.href) {
    return (
      <a
        className={className}
        href={vertical.href}
        target="_blank"
        rel="noopener noreferrer"
      >
        {inner}
      </a>
    );
  }

  return (
    <article className={className} aria-disabled="true">
      {inner}
    </article>
  );
}

const BOOKS = [
  {
    title: 'The Night Before Christmas: with Poss Jonah and the Possum Holler Friends',
    kind: 'Hardcover gift book',
    price: '$25.99',
    cover: '/book-B0HRR7WZMG.jpg',
    w: 900,
    h: 1200,
    href: 'https://www.amazon.com/dp/B0HRR7WZMG?tag=possjonah-20',
  },
  {
    title: 'Renewed Every Morning: A 365-Day Verse Book for Women',
    kind: 'Hardcover verse book',
    price: '$24.99',
    cover: '/book-B0HRRXTFL8.jpg',
    w: 782,
    h: 1200,
    href: 'https://www.amazon.com/dp/B0HRRXTFL8?tag=possjonah-20',
  },
  {
    title: 'Possum Holler: Three Stories from the Holler',
    kind: 'Picture book',
    price: '$9.99',
    cover: '/book-possum-holler.jpg',
    w: 440,
    h: 440,
    href: 'https://www.amazon.com/dp/B0HMJT12WV?tag=possjonah-20',
  },
  {
    title: 'Possum Holler Coloring Book',
    kind: 'Coloring book',
    price: '$7.99',
    cover: '/book-possum-holler-coloring.jpg',
    w: 440,
    h: 569,
    href: 'https://www.amazon.com/dp/B0HMJYDD7R?tag=possjonah-20',
  },
];


const SERIES = [
  {
    id: 'weird-history',
    name: 'Well, That’s Weird: History',
    text: 'True, odd moments from the past, told short and checked against published sources: a bear who served in the Polish army, a soldier who kept fighting until 1974, the strangest Olympic marathon ever run, and the 19th-century fear that tomatoes were poison.',
  },
  {
    id: 'weird-animals',
    name: 'Well, That’s Weird: Animals',
    text: 'Real animals that sound made up, from the axolotl that never grows up to the star-nosed mole, the glow-in-the-dark flying squirrel and the tiny, deadly blue-ringed octopus. Every claim is checked against published science or museum sources.',
  },
  {
    id: 'weird-cryptids',
    name: 'Well, That’s Weird: Cryptids',
    text: 'Creatures people report but science has never confirmed. Each story covers where the legend came from, what witnesses said they saw and what a sensible explanation might be, then leaves the verdict to you.',
  },
  {
    id: 'weird-crime',
    name: 'Well, That’s Weird: Crime',
    text: 'Odd, non-graphic true-crime stories and courtroom curiosities, like the unsolved D.B. Cooper hijacking and the “bear” that wrecked a Rolls-Royce.',
  },
  {
    id: 'weird-science',
    name: 'Well, That’s Weird: Science',
    text: 'Strange but real experiments and discoveries, including the pitch drop experiment, which has dripped only a handful of times since 1927.',
  },
  {
    id: 'i-grandi',
    name: 'I Grandi: Great Early Recordings',
    text: 'Public-domain recordings made before 1923 by the first stars of recorded sound, each with a short introduction to the artist and the piece.',
  },
];

const FEATURED = [
  { href: '/episodes/the-bear-who-went-to-war-wojtek.html', title: 'Wojtek, the bear who went to war' },
  { href: '/episodes/d-b-cooper-he-jumped-out-of-a-plane-with-200-000.html', title: 'D.B. Cooper and the $200,000 jump' },
  { href: '/episodes/the-1938-martian-panic-might-be-a-myth.html', title: 'The 1938 Martian panic might be a myth' },
  { href: '/episodes/the-great-tomato-scare.html', title: 'The great tomato scare' },
  { href: '/episodes/the-axolotl-that-never-grows-up.html', title: 'The axolotl that never grows up' },
  { href: '/episodes/inky-the-octopus-escapes-to-the-ocean.html', title: 'Inky the octopus escapes to the ocean' },
  { href: '/hiroo-onoda-lubang.html', title: 'Hiroo Onoda: the soldier whose war lasted until 1974' },
  { href: '/mona-lisa-theft-1911.html', title: 'The day the Mona Lisa walked out of the Louvre' },
];

function StoriesSection() {
  return (
    <section className="stories" aria-labelledby="stories-heading">
      <h2 id="stories-heading" className="section-title">
        Stories from Poss Jonah
      </h2>
      <p className="section-note">
        Poss Jonah is a cartoon possum who leans on a lamppost and tells true
        stories that sound too strange to be real. Each short video comes with a
        written article on this site, with the full story told in plain language
        and the sources listed at the bottom so you can check every fact
        yourself. The stories are family-friendly and non-graphic. When
        historians or scientists disagree, the article says so.
      </p>
      <div className="series-list">
        {SERIES.map((s) => (
          <article className="series-card" key={s.id}>
            <h3>
              <a href={`/episodes/#${s.id}`}>{s.name}</a>
            </h3>
            <p>{s.text}</p>
          </article>
        ))}
      </div>
      <h3 className="stories__subhead">Start reading</h3>
      <ul className="stories__featured">
        {FEATURED.map((f) => (
          <li key={f.href}>
            <a href={f.href}>{f.title}</a>
          </li>
        ))}
      </ul>
      <p className="section-note">
        Browse <a href="/episodes/">every video and article</a>, read the{' '}
        <a href="/articles.html">World of the Strange articles</a>, or learn{' '}
        <a href="/about.html">more about Poss Jonah</a>.
      </p>
      <h3 className="stories__subhead">The best-of rankings</h3>
      <p className="section-note">
        Poss Jonah also runs a family of free, fan-driven rankings. Best Tea
        started it with Southern iced tea, city by city across the South. The
        trail now covers pizza, burgers, steak, hot dogs, BBQ, fried chicken,
        seafood, Chinese, Mexican, fast food, burritos, tacos and egg rolls
        across the United States. Visitors nominate the places they love and
        cheer for their favorites. The rankings only celebrate the good spots;
        there are no “worst of” lists.
      </p>
    </section>
  );
}

function BooksSection() {
  return (
    <section className="books" aria-labelledby="books-heading">
      <h2 id="books-heading" className="section-title">
        Poss Jonah books
      </h2>
      <p className="section-note">Christmas hardcovers, picture books, and coloring books from Poss Jonah. The hardcovers usually ship in about 8–9 days as of Nov 16, so order soon if a copy is meant to be under the tree.</p>
      <div className="book-grid">
        {BOOKS.map((b) => (
          <article className="book-card" key={b.href}>
            <img
              className="book-card__cover"
              src={b.cover}
              alt={`Cover of ${b.title}`}
              width={b.w}
              height={b.h}
              loading="lazy"
            />
            <h3 className="book-card__title">{b.title}</h3>
            <p className="book-card__meta">
              {b.kind} · {b.price}
            </p>
            <a
              className="book-card__buy"
              href={b.href}
              target="_blank"
              rel="sponsored noopener"
            >
              Buy on Amazon
            </a>
          </article>
        ))}
      </div>
      <a className="books__free" href="/books.html">
        See all Poss Jonah books →
      </a>
      <a className="books__free" href="/coloring-pages.html">
        <span aria-hidden="true">🖍️</span> Free coloring pages to print
      </a>
      <p className="books__disclosure">
        As an Amazon Associate I earn from qualifying purchases.
      </p>
    </section>
  );
}

export default function App() {
  return (
    <div className="app-shell">
      <div className="confetti confetti--tl" aria-hidden="true" />
      <div className="confetti confetti--tr" aria-hidden="true" />

      <header className="site-header">
        <div className="site-header__bunting" aria-hidden="true" />
        <div className="site-header__inner">
          <div className="brand">
            <span className="brand__mark">
              <img
                src="/poss-jonah-logo.png"
                alt=""
                className="brand__logo"
                width={53}
                height={53}
              />
            </span>
            <span className="brand__text">
              <span className="brand__name">Poss Jonah</span>
              <span className="brand__by">Best-of rankings, with a lamppost</span>
            </span>
          </div>
          <nav className="site-header__links">
            <a className="site-header__books" href="/books.html">📚 Books</a>{' '}<a className="site-header__books" href="/episodes/">🎬 Videos</a>
            <a className="site-header__books" href="https://shop.possjonah.com">🛍️ Shop</a>
            <a className="site-header__apps" href="https://help-pal-apps.com">Free Help-Pal apps</a>
          </nav>
        </div>
      </header>

      <main className="main">
        <section className="hero hero--big">
          <div className="hero__stickers" aria-hidden="true">
            <span className="sticker sticker--lemon">🍋</span>
            <span className="sticker sticker--ice">✨</span>
            <span className="sticker sticker--sparkle">🍑</span>
          </div>
          <div className="hero__mascot">
            <img
              src="/poss-jonah-logo.png"
              alt="Poss Jonah leaning on his lamppost"
              className="hero__mascot-img"
              width={168}
              height={168}
            />
          </div>
          <p className="eyebrow">Hey y’all — I’m Poss Jonah</p>
          <h1>Find the best of everything</h1>
          <p className="lede">
            I wander town to town huntin’ the good stuff. Tea’s live for the South,
            and the rest of the trail — pizza, BBQ, chicken, seafood, burgers, and
            more — is live nationwide. Pick a ranking and cheer your favorites.
          </p>
          <p className="lede">
            <a href="/articles.html">Read the World of the Strange articles →</a>
          </p>
        </section>

        <section className="verticals" aria-labelledby="verticals-heading">
          <h2 id="verticals-heading" className="section-title">
            What’s on the trail
          </h2>
          <p className="section-note">
            Best Tea covers the South. Everything else below is live nationwide —
            tap a card and go cheer.
          </p>
          <div className="vertical-grid">
            {verticals.map((vertical) => (
              <VerticalCard key={vertical.id} vertical={vertical} />
            ))}
          </div>
        </section>

        <StoriesSection />

        <BooksSection />

        <aside className="more-trail" aria-label="More rankings on the way">
          <p>
            And I ain’t done — {formatList(moreOnTheTrail)} are waitin’ their
            turn too.
          </p>
        </aside>
      </main>

      <footer className="site-footer">
        <p className="site-footer__tag">
          Poss Jonah · a Help-Pal “best of” family
        </p>
        <p className="help-pal-link">
          <a
            href={HELP_PAL_COLLECTION_URL}
            target="_blank"
            rel="noopener noreferrer"
          >
            More apps from Help-Pal
          </a>
          {' · '}
          <a href="/books.html">Books</a>
          {' · '}
          <a href="https://help-pal-apps.com">Free Help-Pal apps</a>
          {' · '}
          <a href="/articles.html">Articles</a>
          {' · '}
          <a href="/about.html">About</a>
          {' · '}
          <a href="/episodes/">Videos</a>{' · '}<a href="/contact.html">Contact</a>{' · '}<a href="/privacy.html">Privacy</a>{' · '}<a href="/terms.html">Terms</a>
        </p>
        <nav className="family-sites" aria-label="Family of sites">
          <p>
            <strong>Family of sites:</strong>{' '}
            <a href="https://shop.possjonah.com">Possum Holler Mercantile</a>{' '}
            (vintage finds &amp; ornaments){' · '}
            <a href="https://help-pal-apps.com/">Help-Pal free apps</a>{' · '}
            <a href="https://www.youtube.com/@PossJonah">Poss Jonah on YouTube</a>{' · '}
            <a href="https://www.youtube.com/@PossJonahKids">Poss Jonah Kids on YouTube</a>{' · '}
            <a href="/books.html">Poss Jonah books on Amazon</a>
          </p>
        </nav>
        <p className="site-footer__fine">
          Tea is Southern. The rest of the trail is national — all live now.
        </p>
      </footer>
    </div>
  );
}
