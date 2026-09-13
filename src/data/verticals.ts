export type VerticalStatus = 'live' | 'soon';

export type Vertical = {
  id: string;
  name: string;
  emoji: string;
  status: VerticalStatus;
  href?: string;
  scope: string;
  blurb: string;
};

export const verticals: Vertical[] = [
  {
    id: 'tea',
    name: 'Best Tea',
    emoji: '🧊',
    status: 'live',
    href: 'https://tea.possjonah.com',
    scope: 'Southern cities',
    blurb: 'Sweet, unsweet, and everything in between — city by city across the South.',
  },
  {
    id: 'pizza',
    name: 'Best Pizza',
    emoji: '🍕',
    status: 'soon',
    scope: 'National when it launches',
    blurb: 'Slices, pies, and late-night boxes. Whole country, soon as I pack a bigger suitcase.',
  },
  {
    id: 'bbq',
    name: 'Best BBQ',
    emoji: '🍖',
    status: 'soon',
    scope: 'National when it launches',
    blurb: 'Smoke, sauce, and the kind of bark that makes you lean on a lamppost and sigh.',
  },
  {
    id: 'fried-chicken',
    name: 'Best Fried Chicken',
    emoji: '🍗',
    status: 'soon',
    scope: 'Coming soon',
    blurb: 'Crispy, juicy, Sunday-after-church good. Huntin’ the golden pieces next.',
  },
  {
    id: 'seafood',
    name: 'Best Seafood',
    emoji: '🦐',
    status: 'soon',
    scope: 'Coming soon',
    blurb: 'Shrimp, oysters, and a fryer that smells like the coast. Coming along shortly.',
  },
  {
    id: 'burrito',
    name: 'Best Burrito',
    emoji: '🌯',
    status: 'soon',
    scope: 'Coming soon',
    blurb: 'Wrapped tight, filled right. I’ll be on the burrito beat before you know it.',
  },
  {
    id: 'taco',
    name: 'Best Taco',
    emoji: '🌮',
    status: 'soon',
    scope: 'Coming soon',
    blurb: 'Street stands, trucks, and the little spots with the handmade tortillas.',
  },
  {
    id: 'egg-roll',
    name: 'Best Egg Roll',
    emoji: '🥢',
    status: 'soon',
    scope: 'Coming soon',
    blurb: 'Crisp wrappers, hot filling, extra duck sauce if that’s how you take it.',
  },
];

export const moreOnTheTrail = ['hot dogs', 'burgers', 'fries', 'subs'];
