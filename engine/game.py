import abc
from typing import Dict

from engine.game_state import GameState
from engine.player import PlayerAction, Player


class Game(abc.ABC):
    bidder_pos: int
    player_pos_dict: Dict[int, Player]
    prev_game: 'Game'

    @abc.abstractmethod
    def player_action(self, player_id: str, action: PlayerAction, action_data) -> GameState:
        pass

    def initialize_game(self):
        if self.prev_game is not None:
            self.bidder_pos = self.get_next_pos(self.prev_game.bidder_pos)
        else:
            self.bidder_pos = 1

    def get_next_pos(self, pos):
        next_pos = pos + 1
        if next_pos > len(self.player_pos_dict):
            next_pos = 1
        return next_pos
