import pytest
from card import Card, Rank, Suit

def test_invalid_value_of_suit():
    with pytest.raises(ValueError):
        suit = Suit('すぺーど')

def test_invalid_type_of_rank():
    with pytest.raises(TypeError):
        rank = Rank(1)

def test_invalid_type_of_rank():
    with pytest.raises(ValueError):
        rank = Rank('11')

def test_card_ok():
    suit = Suit('♠')
    rank = Rank('2')
    card = Card(suit, rank)

    assert '♠2' == str(card)



# def test_get_notation():
#     card = Card('♠', '2')

#     assert '♠2' == str(card)

# def test_get_notation_2():
#     card = Card(Suit.spade, Rank.two)

# def test_get_notation_3():
#     card = Card(Suit('♠'), Rank('2'))

# def test_invalid_value_of_suit():
#     with pytest.raises(ValueError):
#         Card('ほげ', '2')

# def test_invalid_type_of_rank():
#     with pytest.raises(TypeError):
#         Card('♠', 2)

# def test_invalid_value_of_rank():
#     with pytest.raises(ValueError):
#         Card('♠', '14')