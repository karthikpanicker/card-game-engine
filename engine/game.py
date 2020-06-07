import abc
from typing import Dict

from engine.player import PlayerAction, Player


class Game(abc.ABC):
    dealer_pos: int
    player_pos_dict: Dict[int, Player]
    prev_game: 'Game'

    @abc.abstractmethod
    def player_action(self, player_id: str, action: PlayerAction, action_data):
        pass

    def initialize_game(self):
        if self.prev_game is not None:
            self.dealer_pos = self.get_next_pos(self.prev_game.dealer_pos)
        else:
            self.dealer_pos = 1

    def get_next_pos(self, pos):
        next_pos = pos + 1
        if next_pos > len(self.player_pos_dict):
            next_pos = 1
        return next_pos
