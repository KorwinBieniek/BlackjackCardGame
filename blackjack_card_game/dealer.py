"""
Module that represents a dealer class
"""

from hand import Hand

class Dealer:
    """
    Class representing a dealer
    :get_str_hand_hidden: hides the last card to display
    :get_str_hand: displays the card on hand
    :hit: adds a card to a specific hand
    """
    def __init__(self, hand):
        """
        :param hand: Hand, dealer's hand
        """
        self.hand = hand

    def get_str_hand_hidden(self):
        """
        separate __str__ implementation with the last value as 'Unknown'
        :return: str, returns all cards except the last one, which is displayed as 'Unknown'
        """
        return f'{", ".join(self.hand.cards[:-1])}, Unknown'

    def get_str_hand(self):
        """
        separate __str__ implementation with all values shown of cards on hand
        :return: str, uses __str__ method of Hand class
        """
        return str(self.hand)

    def hit(self, hand):
        """
        Adding a card to specific hand (player's/dealer's)
        :param hand: Hand, specific hand to add card to
        """
        hand.add_to_hand()


if __name__ == '__main__':
    deal = Dealer(Hand())
    deal.hand.add_to_hand()
    deal.hand.add_to_hand()
    deal.hand.add_to_hand()
    print(deal.get_str_hand())
