import abc
from typing import Dict

from engine.game import Game
from engine.player import PlayerAction


class GameState(abc.ABC):
    @abc.abstractmethod
    def handle_player_action(self, player_id: str, action: PlayerAction,
                             game: Game, action_data: Dict[str, object]):
        pass