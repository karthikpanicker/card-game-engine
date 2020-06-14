from typing import Dict

from pydealer import Card

from engine.player import Player

"""
Game round represents a game play involving one card from each player. The cards played in the round will be used 
to determine who wins the round.
"""


class GameRound:
    player_card_map: Dict[Player, Card]

    def __init__(self, first_player: Player):
        self.first_player = first_player
        self.player_card_map = {}

    def add_player_card(self, player: Player, card: Card):
        self.player_card_map[player] = card

    def get_card_count(self):
        return len(self.player_card_map)

    def get_first_card(self):
        return list(self.player_card_map.values())[0]

    def summarize(self, trump_card):
        if trump_card is None:
            print("hello world")


