from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):
        while self.player.balance > 0:
            choice = input(f'You are starting with ${self.player.balance}. Would you like to play a hand? ')
            if choice != 'yes':
                break
            self.bet = int(input('Place your bet: '))