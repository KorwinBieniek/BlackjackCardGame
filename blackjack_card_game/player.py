class Player:
    def __init__(self, balance, hand):
        self.balance = balance
        self.hand = hand
        self.hand_value = 0

    def get_str_hand(self):
        # separate implementation with all values shown - can use the hand __str__ method
        return str(self.hand)
