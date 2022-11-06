"""
Module that contains a class that represents a deck of cards
"""

import random
from card import Card


class Deck:
    """
    Class that represents a deck of cards
    """

    def __init__(self):
        self.num_of_cards = 52
        self.card_list = []

    def create_deck(self):
        """
        Creates a deck of cards for each value separated for each suit (4 suits, 13 cards each)
        """
        suit = 0
        for i in range(self.num_of_cards):
            if i % 13 == 0:
                suit += 1
            self.card_list.append(str(Card(Card.SUIT_SYMBOLS[suit], Card.VALUE_NAMES[i % 13 + 1])))

    def shuffle(self):
        """
        Shuffles a deck of cards
        """
        random.shuffle(self.card_list)

    def __str__(self):
        return f'{self.card_list}'


if __name__ == '__main__':
    deck = Deck()
    deck.create_deck()
    print(deck)
    deck.shuffle()
    print(deck)
