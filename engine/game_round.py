from typing import Dict

from pydealer import Card

from engine.player import Player

"""
Game round represents a game play involving one card from each player. The cards played in the round will be used 
to determine who wins the round.
"""


class GameRound:
    player_card_map: Dict[Player, Card] = {}

    def __init__(self, first_player: Player):
        self.first_player = first_player

    def add_player_card(self, player: Player, card: Card):
        self.player_card_map[player] = card
