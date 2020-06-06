import abc
from typing import Dict

from engine.game_state import GameState


class ActionExecutor(abc.ABC):
    @abc.abstractmethod
    def execute(self,game_state: GameState, action_data: Dict[str,str]):
        pass