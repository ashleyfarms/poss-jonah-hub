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
    status: 'live',
    href: 'https://pizza.possjonah.com',
    scope: 'National US cities',
    blurb: 'Slices, pies, and late-night boxes — city by city across the whole country.',
  },
  {
    id: 'burger',
    name: 'Best Burger',
    emoji: '🍔',
    status: 'live',
    href: 'https://burger.possjonah.com',
    scope: 'National US cities',
    blurb: 'Diners, stands, trucks, and smash patties — cheer the burgers that make you smile.',
  },
  {
    id: 'steak',
    name: 'Best Steak',
    emoji: '🥩',
    status: 'live',
    href: 'https://steak.possjonah.com',
    scope: 'National US cities',
    blurb: 'Honest crust, thick cuts, and rooms that feel like home — steak city by city.',
  },
  {
    id: 'hot-dog',
    name: 'Best Hot Dog',
    emoji: '🌭',
    status: 'live',
    href: 'https://hotdog.possjonah.com',
    scope: 'National US cities',
    blurb: 'Carts, stands, and classic counters — hunt the best dog in town.',
  },
  {
    id: 'bbq',
    name: 'Best BBQ',
    emoji: '🍖',
    status: 'live',
    href: 'https://bbq.possjonah.com',
    scope: 'National US cities',
    blurb: 'Smoke, sauce, and the kind of bark that makes you lean on a lamppost and sigh.',
  },
  {
    id: 'fried-chicken',
    name: 'Best Fried Chicken',
    emoji: '🍗',
    status: 'live',
    href: 'https://chicken.possjonah.com',
    scope: 'National US cities',
    blurb: 'Crispy, juicy, Sunday-after-church good — golden pieces city by city.',
  },
  {
    id: 'seafood',
    name: 'Best Seafood',
    emoji: '🦐',
    status: 'live',
    href: 'https://seafood.possjonah.com',
    scope: 'National US cities',
    blurb: 'Shrimp, oysters, and a fryer that smells like the coast.',
  },
  {
    id: 'chinese',
    name: 'Best Chinese',
    emoji: '🥡',
    status: 'live',
    href: 'https://chinese.possjonah.com',
    scope: 'National US cities',
    blurb: 'Restaurants and takeout counters — banquet halls to late-night windows.',
  },
  {
    id: 'mexican',
    name: 'Best Mexican',
    emoji: '🌶️',
    status: 'live',
    href: 'https://mexican.possjonah.com',
    scope: 'National US cities',
    blurb: 'Family tables, festive rooms, and honest Mexican restaurants city by city.',
  },
  {
    id: 'fast-food',
    name: 'Best Fast Food',
    emoji: '🍟',
    status: 'live',
    href: 'https://fastfood.possjonah.com',
    scope: 'National US cities',
    blurb: 'Chains, locals, and drive-thrus that get it right — cheer the quick wins.',
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

export const moreOnTheTrail = ['fries', 'subs', 'wings', 'donuts'];
