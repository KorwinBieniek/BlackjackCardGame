"""
Module with a class that represents a player's/dealer's hand
"""

from deck import Deck
from card import Card


class Hand:
    """
    A class that represents a player's/dealer's hand
    """

    def __init__(self):
        self.deck = Deck()
        self.deck.create_deck()
        self.deck.shuffle()
        self.cards = []

    def sort_by_card_value(self):
        """
        Custom sorting function to store Aces as the last card in a hand
        :return: Hand, sorted hand
        """
        #
        cards_values = '23456789TJQKA'
        return sorted(self.cards, key=lambda word: [cards_values.index(c) for c in word[0]])

    def get_value(self):
        """
        Calculates the value of cards in a hand
        :return: int, calculated value of cards
        """
        # Working on sorted hand to calculate Aces scores as the last
        self.cards = self.sort_by_card_value()
        points = 0
        for card in self.cards:
            # If card is King, Queen or Jack
            if card[0] in ['K', 'Q', 'J']:
                points += 10
            # If card is Ace add 11 or 1 depending on the score of your whole deck
            elif card[0] == 'A':
                if points <= 10:
                    points += 11
                else:
                    points += 1
            else:
                # If card is numerical, add numeric value (T has key 10)
                points += self.get_key_from_value(Card.VALUE_NAMES, card[0])[0]
        return points

    def add_to_hand(self):
        """
        Adds a first card from the sorted deck to hand and removes it from the deck
        """
        # Get first card from the list
        card_to_hand = self.deck.card_list[0]
        self.cards.append(card_to_hand)
        del self.deck.card_list[0]

    def __str__(self):
        return ', '.join(self.cards)

    def get_key_from_value(self, cards_dict, card_value):
        """

        :param cards_dict: dict with cards values
        :param card_value: a specific value to search within a cards_dic
        :return: return a value of the card
        """
        # Searches the dict with card values to check the specific card value
        return [key for key, value in cards_dict.items() if value == card_value]


if __name__ == '__main__':
    hand = Hand()
    hand.add_to_hand()
    hand.add_to_hand()
    hand.add_to_hand()
    hand.add_to_hand()
    hand.add_to_hand()
    print(hand.get_value())
    print(hand)
