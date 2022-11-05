from deck import Deck
from card import Card

class Hand:
    def __init__(self):
        self.deck = Deck()
        self.deck.create_deck()
        self.deck.shuffle()
        self.cards = []


    def get_value(self):
        cards_values = '23456789TJQKA'
        self.cards = sorted(self.cards, key=lambda word: [cards_values.index(c) for c in word[0]])
        #print(self.cards)
        sum = 0
        for card in self.cards:

            if card[0] in ['K', 'Q', 'J']:
                sum += 10
            elif card[0] == 'A':
                #print('Tutaj jest AS')
                if sum <= 10:
                    sum += 11
                else:
                    sum += 1
            else:
                sum += self.get_key_from_value(Card.VALUE_NAMES, card[0])[0]
            #print(card[0], sum)
        return sum
        
    def add_to_hand(self):
        card_to_hand = self.deck.card_list[0]
        self.cards.append(card_to_hand)
        del self.deck.card_list[0]

    def __str__(self):
        return ', '.join(self.cards)

    def get_key_from_value(self, d, val):
        return [k for k, v in d.items() if v == val]

if __name__ == '__main__':
    hand = Hand()
    hand.add_to_hand()
    hand.add_to_hand()
    hand.add_to_hand()
    hand.add_to_hand()
    hand.add_to_hand()
    print(hand.get_value())
    print(hand)