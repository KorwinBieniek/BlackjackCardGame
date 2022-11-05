from deck import Deck
from hand import Hand
from sys import exit

#Testing
from player import Player
from dealer import Dealer


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):
        while self.player.balance > 0:
            self.player.balance = round(self.player.balance, 2)
            self.player.hand = Hand()
            self.dealer.hand = Hand()
            choice = input(f'You are starting with ${self.player.balance}. Would you like to play a hand? ')
            if choice != 'yes':
                print(f'You left the table with ${self.player.balance}')
                exit(0)

            self.bet = input('Place your bet: $')
            while not self.bet.replace('.', '', 1).isdigit() or float(self.bet) < 1 or float(self.bet) > self.player.balance:
                print(f'The minimum bet is: $1 and the maximum bet cannot exceed your balance ({self.player.balance})')
                self.bet = input('Place your bet: $')

            self.bet = float(self.bet)
            #print(self.bet)

            self.player.hand.add_to_hand()
            self.player.hand.add_to_hand()
            self.player.hand_value = self.player.hand.get_value()
            print(f'You are dealt: {self.player.get_str_hand()}')

            self.dealer.hand.add_to_hand()
            self.dealer.hand.add_to_hand()
            self.dealer.hand_value = self.dealer.hand.get_value()
            print(f'The dealer is dealt: {self.dealer.get_str_hand_hidden()}')


            while True:
                player_hit = input(f'Would you like to hit or stay? ')

                while player_hit not in ['hit', 'stay']:
                    print('That is not a valid option,')
                    player_hit = input(f'Would you like to hit or stay? ')

                if player_hit == 'hit':
                    dealer.hit(self.player.hand)
                    print(f'You are dealt: {self.player.hand.cards[-1]}')
                    print(f'You now have: {self.player.hand}')

                print('player: ', player.hand.get_value())
                print('dealer: ', dealer.hand.get_value())

                if player.hand.get_value() > 21:
                    break

                if player_hit == 'stay':
                    print(f'The dealer has: {self.dealer.get_str_hand()}')
                    while self.dealer.hand.get_value() <= 16:
                        self.dealer.hit(self.dealer.hand)
                        print(f'Dealer hits and is dealt: {self.dealer.hand.cards[-1]}')
                        print(f'The dealer has: {self.dealer.hand}')
                    else:
                        print('The dealer stays.')
                    break

            print('player: ', player.hand.get_value())
            print('dealer: ', dealer.hand.get_value())

            if player.hand.get_value() > 21:
                print(f'Your hand value is over 21 and you lose ${self.bet} :(')
                self.player.balance -= self.bet
            elif player.hand.get_value() == 21 and dealer.hand.get_value() != 21:
                print(f'Blackjack! You win {self.bet * 1.5}')
                self.player.balance += self.bet * 1.5
            elif dealer.hand.get_value() > 21:
                print(f'The dealer has over 21 points, you win ${self.bet} :)')
                self.player.balance += self.bet
            elif player.hand.get_value() > dealer.hand.get_value():
                print(f'The dealer busts, you win ${self.bet} :)')
                self.player.balance += self.bet
            elif player.hand.get_value() < dealer.hand.get_value():
                print(f'The dealer wins, you lose ${self.bet} :(')
                self.player.balance -= self.bet
            elif player.hand.get_value() == dealer.hand.get_value():
                print('You tie. Your bet has been returned.')


        print('You\'ve ran out of money. Please restart this program to try again. Goodbye.')

if __name__ == '__main__':
    player = Player(500, Hand())
    dealer = Dealer(Hand())
    game = Game(player, dealer)
    game.start_game()