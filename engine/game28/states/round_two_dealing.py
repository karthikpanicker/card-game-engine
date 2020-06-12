from typing import Dict

from engine.game import Game
from engine.game28.game28_state import Game28State
from engine.game28.states.dealing_base import DealingBase
from engine.player import PlayerAction


class RoundTwoDealing():
    @staticmethod
    def handle_player_action(player_id: str, action: PlayerAction, game: Game, action_data: Dict[str, object]):
        DealingBase.handle_player_action(player_id, action, game, action_data)
        return Game28State.ROUND_TWO_DEALING_DONE
