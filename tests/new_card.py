import enum

class Suit(enum.Enum):
    spade = '♠'
    

class Rank(enum.Enum):
    two = '2'


class NewCard:
    def __init__(self, suit: Suit, rank: Rank):
        if not isinstance(suit, Suit):
            raise TypeError
        
        if not isinstance(rank, Rank):
            raise TypeError
        
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit.value}{self.rank.value}'
