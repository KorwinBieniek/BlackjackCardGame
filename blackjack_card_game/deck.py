import random
from card import Card


class Deck:
    def __init__(self):
        self.num_of_cards = 52
        self.card_list = []

    def create_deck(self):
        x = 0
        for i in range(self.num_of_cards):
            if i % 13 == 0:
                x += 1
            self.card_list.append(str(Card(Card.SUIT_SYMBOLS[x], Card.VALUE_NAMES[i % 13 + 1])))

    def shuffle(self):
        random.shuffle(self.card_list)

    def deal(self, num_cards):
        pass

    def __str__(self):
        return f'{self.card_list}'


if __name__ == '__main__':
    deck = Deck()
    deck.create_deck()
    print(deck)
    deck.shuffle()
    print(deck)
