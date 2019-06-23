class Card:

    def __init__(self, suit: str, rank: str):
        suit_list = ['♠', '♥', '♣', '♦︎']
        rank_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        if suit not in suit_list:
            raise ValueError(f'{suit} is invalid suit')

        if not isinstance(rank, str):
            raise TypeError(f'TypeError: unsupported type for rank: "str" , not {type(rank)}')

        if rank not in rank_list:
            raise ValueError(f'{rank} is invalid rank')

        self._suit = suit
        self._rank = rank

    def __str__(self) -> str:
        return f"{self._suit}{self._rank}"

if __name__ == "__main__":
    card = Card(suit="♠", rank=2)
