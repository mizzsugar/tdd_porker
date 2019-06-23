from new_card import NewCard, Suit, Rank
import pytest

def test_new_card():
    card = NewCard(Suit.spade, Rank.two)

    assert '♠2' == str(card)

def test_not_allowed_suit():
    with pytest.raises(TypeError):
        NewCard('♠', Rank.two)

def test_not_allowed_rank():
    with pytest.raises(TypeError):
        NewCard(Suit.spade, 2)
