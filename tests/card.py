class Card:

    def __init__(self, suit: str, rank: str):
        self._suit = suit
        self._rank = rank

    def __str__(self) -> str:
        return f"{self._suit}{self._rank}"
