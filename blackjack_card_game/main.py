"""
Main module to start and play the game
"""

from player import Player
from dealer import Dealer
from game import Game
from hand import Hand

STARTING_BALANCE = 500
player = Player(STARTING_BALANCE, Hand())
dealer = Dealer(Hand())
game = Game(player, dealer)

print("Welcome to Blackjack!")
print()
game.start_game()
