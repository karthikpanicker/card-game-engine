from enum import Enum
from typing import Dict
from engine.game import Game
from engine.game28.game28 import Game28
from engine.game_engine_exception import GameEngineException
from engine.player import Player


class GameType(Enum):
    TWENTY_EIGHT = 28
    FIFTY_SIX = 56


class GameFactory:
    @staticmethod
    def get_game_implementation(game_type: GameType, player_dict: Dict[str, Player],
                                prev_game: Game) -> Game:
        if game_type == GameType.TWENTY_EIGHT:
            return Game28(player_dict, prev_game)
        else:
            raise GameEngineException(str.format("Game of type {} not implemented", game_type))
