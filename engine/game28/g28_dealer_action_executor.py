from typing import Dict

from engine.action_executor import ActionExecutor
from engine.game28.gm_28_deck import Game28Deck
from engine.game_engine_exception import GameEngineException
from engine.game_state import GameState, GameStateConstants
import engine.action_constants as constants
from engine.player import Player


class G28DealerActionExecutor(ActionExecutor):
    @staticmethod
    def execute(game_state: GameState, action_data: Dict[str, object]):
        if game_state.get_game_state() == GameStateConstants.STATE_ZERO:
            deck = action_data[constants.DECK]
            player_pos_dict = action_data[constants.PLAYER_POSITION_DICT]
            for pos, player in player_pos_dict.items():
                player.add_cards(deck.deal_cards(4))
        else:
            raise GameEngineException("Invalid game state for dealing cards")
