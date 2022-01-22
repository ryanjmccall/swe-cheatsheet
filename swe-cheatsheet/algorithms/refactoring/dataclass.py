
from typing import Any, List
from dataclasses import make_dataclass, dataclass, field


@dataclass
class Position:
    name: str
    lon: float
    lat: float = 0.0

    # has __init__, __repr__, __eq__


# pos = Position('Oslo', 10, 59)
# print(f'{pos.name} is at {pos.lat} N')


Position2 = make_dataclass('Position2', ['name', 'lat', 'lon'])


@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42

    def some_method(self, other):
        return self.value + other


# foo = WithoutExplicitTypes('bar')
# print(foo.some_method(42))


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


@dataclass(order=True)
class PlayingCard:
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck,
                                     metadata={'type': 'french'})

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


#print(Deck(sorted(make_french_deck())))


@dataclass(frozen=True)
class Position3:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass
class Position4:
    name: str
    lon: float
    lat: float = 0.0


@dataclass
class Capital(Position4):
    country: str = ''  # b/c of super class default val


@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']  # only define these attrs to save resources
    name: str
    lon: float
    lat: float
