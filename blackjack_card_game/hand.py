from deck import Deck
from card import Card
import random

class Hand:
    def __init__(self):
        self.deck = Deck()
        self.deck.create_deck()
        self.deck.shuffle()
        self.cards = []


    def get_value(self):
        sum = 0
        for card in self.cards:
            if card[0] in ['K', 'Q', 'J']:
                sum += 10
            else:
                sum += self.get_key_from_value(Card.VALUE_NAMES, card[0])[0]
        return sum
        
    def add_to_hand(self):
        self.cards.append(random.choice(self.deck.card_list))

    def __str__(self):
        return ', '.join(self.cards)

    def get_key_from_value(self, d, val):
        return [k for k, v in d.items() if v == val]

if __name__ == '__main__':
    hand = Hand()
    hand.add_to_hand()
    hand.add_to_hand()
    print(hand.get_value())
    print(hand)