"""
A module that contains a Game class, which is used to represent and start the Blackjack game
"""
import time
import sys
from deck import Deck
from hand import Hand

# Testing
from player import Player
from dealer import Dealer


class Game:
    """
    Class that represents a game of Blackjack
    """
    MINIMUM_BET = 1

    def __init__(self, game_player, game_dealer):
        self.player = game_player
        self.dealer = game_dealer
        self.bet = None
        self.deck = Deck()

    def play_hand(self):
        """
        Take a player's choice to start the game, if not then exits the program
        """
        choice = input(f'You are starting with ${self.player.balance}. '
                       f'Would you like to play a hand? ')
        if choice != 'yes':
            print(f'You left the table with ${self.player.balance}')
            sys.exit(0)

    def place_bet(self):
        """
        Allows player to place a bet and verifies if it has been properly input
        :return: float, player's bet
        """
        self.bet = input('Place your bet: $')
        while not self.bet.replace('.', '', 1).isdigit() or float(self.bet) < self.MINIMUM_BET \
                or float(self.bet) > self.player.balance:
            print(
                f'The minimum bet is: ${self.MINIMUM_BET} '
                f'and the maximum bet cannot exceed your balance (${self.player.balance})')
            self.bet = input('Place your bet: $')

        return float(self.bet)

    def first_deal(self):
        """
        First deal of cards to both player and dealer
        """
        self.player.hand.add_to_hand()
        self.player.hand.add_to_hand()
        self.player.hand_value = self.player.hand.get_value()
        print(f'You are dealt: {self.player.get_str_hand()}')

        self.dealer.hand.add_to_hand()
        self.dealer.hand.add_to_hand()
        self.dealer.hand_value = self.dealer.hand.get_value()
        print(f'The dealer is dealt: {self.dealer.get_str_hand_hidden()}')

    def player_hit(self):
        """
        Allows player to draw another card or stay with his available cards
        """
        while True:
            choice = input('Would you like to hit or stay? ')

            while choice not in ['hit', 'stay']:
                print('That is not a valid option,')
                choice = input('Would you like to hit or stay? ')

            if choice == 'hit':
                self.dealer.hit(self.player.hand)
                print(f'You are dealt: {self.player.hand.cards[-1]}')
                print(f'You now have: {self.player.hand}')

            if self.player.hand.get_value() > 21:
                break

            if choice == 'stay':
                print(f'The dealer has: {self.dealer.get_str_hand()}')
                time.sleep(1)
                while self.dealer.hand.get_value() <= 16:
                    self.dealer.hit(self.dealer.hand)
                    print(f'Dealer hits and is dealt: {self.dealer.hand.cards[-1]}')
                    print(f'The dealer has: {self.dealer.hand}')
                    time.sleep(1)
                else:
                    print('The dealer stays.')
                    break
                break

    def determine_winner(self):
        """
        Function to check which condition has been fullfilled and determines the round's result
        """
        if self.player.hand.get_value() > 21:
            print(f'Your hand value is over 21 and you lose ${self.bet} :(')
            self.player.balance -= self.bet
        elif self.player.hand.get_value() == 21 and self.dealer.hand.get_value() != 21:
            print(f'Blackjack! You win {self.bet * 1.5}')
            self.player.balance += self.bet * 1.5
        elif self.dealer.hand.get_value() > 21:
            print(f'The dealer has over 21 points, you win ${self.bet} :)')
            self.player.balance += self.bet
        elif self.player.hand.get_value() > self.dealer.hand.get_value():
            print(f'The dealer busts, you win ${self.bet} :)')
            self.player.balance += self.bet
        elif self.player.hand.get_value() < self.dealer.hand.get_value():
            print(f'The dealer wins, you lose ${self.bet} :(')
            self.player.balance -= self.bet
        elif self.player.hand.get_value() == self.dealer.hand.get_value():
            print('You tie. Your bet has been returned.')
        else:
            print('This situation hasn\'t been included')

    def start_game(self):
        """Allows to run the game"""
        while self.player.balance > 0:
            # Rounding the balance to the second decimal place
            self.player.balance = round(self.player.balance, 2)
            # Resetting hand on each round
            self.player.hand = Hand()
            self.dealer.hand = Hand()

            self.play_hand()

            self.bet = self.place_bet()

            self.first_deal()

            self.player_hit()
            self.determine_winner()
        print('You\'ve ran out of money. Please restart this program to try again. Goodbye.')


if __name__ == '__main__':
    player = Player(500, Hand())
    dealer = Dealer(Hand())
    game = Game(player, dealer)
    game.start_game()
