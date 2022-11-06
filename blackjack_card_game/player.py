"""
A module with a Player class that represents a player
"""
class Player:
    """
    Class that represents a player
    """
    def __init__(self, balance, hand):
        self.balance = balance
        self.hand = hand

    def get_str_hand(self):
        """
        :return: str, __str__ from Hand class to show all the cards in a hand
        """
        return str(self.hand)
