from card import Card


def test_get_notation():
    card = Card('♠', 2)

    assert '♠2' == str(card)
