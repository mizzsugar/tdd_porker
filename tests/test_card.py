import pytest
from card import Card


def test_get_notation():
    card = Card('♠', '2')

    assert '♠2' == str(card)

def test_invalid_value_of_suit():
    with pytest.raises(ValueError):
        Card('ほげ', '2')

def test_invalid_type_of_rank():
    with pytest.raises(TypeError):
        Card('♠', 2)

def test_invalid_value_of_rank():
    with pytest.raises(ValueError):
        Card('♠', '14')
