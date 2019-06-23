import enum

class Suit:
    def __init__(self, value):
        suit_list = ['♠', '♥', '♣', '♦︎']
        if value not in suit_list:
            raise ValueError(f'{value} is invalid suit')

        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"

class Rank:
    def __init__(self, value):
        rank_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        if not isinstance(value, str):
            raise TypeError(f'TypeError: unsupported type for rank: "str" , not {type(value)}')

        if value not in rank_list:
            raise ValueError(f'{value} is invalid rank')

        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"

class Card:

    def __init__(self, suit: str, rank: str):
        self._suit = suit
        self._rank = rank

    def __str__(self) -> str:
        return f"{self._suit}{self._rank}"

if __name__ == "__main__":
    card = Card(suit, rank)