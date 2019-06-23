class Card:

    def __init__(self, suit: str, rank: str):
        suit_list = ['♠', '♥', '♣', '♦︎']
        if suit not in suit_list:
            raise ValueError(f'{suit} is invalid suit')
        if not isinstance(rank, str):
            raise TypeError(f'TypeError: unsupported type for rank: "str" , not {type(rank)}')

        self._suit = suit
        self._rank = rank

    def __str__(self) -> str:
        return f"{self._suit}{self._rank}"
