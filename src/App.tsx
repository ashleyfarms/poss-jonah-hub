import { moreOnTheTrail, verticals, type Vertical } from './data/verticals';

const HELP_PAL_COLLECTION_URL = 'https://help-pal-apps.com/our-app-collection';

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
        </p>
        <p className="site-footer__fine">
          Tea is Southern. The rest of the trail is national — all live now.
        </p>
      </footer>
    </div>
  );
}
