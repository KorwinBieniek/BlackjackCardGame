"""
Module with a Card class tha represents a card in a deck
"""
class Card:
    """
    A class that represents a card in a deck
    """
    SUIT_SYMBOLS = {
        1: "\u2666",  # diamonds
        2: "\u2665",  # hearts
        3: "\u2663",  # clubs
        4: "\u2660"  # spades
    }

    VALUE_NAMES = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "T",
        11: "J",
        12: "Q",
        13: "K"
    }

    def __init__(self, suit, value):
        """
        :param suit: str, suit of a card
        :param value: str, value of a card
        """
        self.suit = suit
        self.value = value

    def __str__(self):
        """
        :return: str, joined value and suit of a card
        """
        return f'{self.value}{self.suit}'
