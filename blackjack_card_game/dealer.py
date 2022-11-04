from hand import Hand

class Dealer:
    def __init__(self, hand):
        self.hand = hand
        self.hand_value = 0

    def get_str_hand_hidden(self):
        # separate implementation with the last value as 'Unknown'
        return f'{", ".join(self.hand.cards[:-1])}, Unknown'

    def get_str_hand(self):
        # separate implementation with all values shown - can use the hand __str__ method
        return str(self.hand)

    def hit(self, hand):
        hand.add_to_hand()

if __name__ == '__main__':
    deal = Dealer(Hand())
    deal.hand.add_to_hand()
    deal.hand.add_to_hand()
    deal.hand.add_to_hand()
    print(deal.get_str_hand())