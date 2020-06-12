from typing import Dict

from engine.game import Game
from engine.game_engine_exception import GameEngineException
from engine.game_state import GameState
from engine.player import PlayerAction


class DealingBase(GameState):
    @staticmethod
    def handle_player_action(player_id: str, action: PlayerAction,
                             game: Game, action_data: Dict[str, object]):
        if action is not PlayerAction.DEALING_ACTION:
            raise GameEngineException("Invalid player action for the game state")

        if player_id is not game.player_pos_dict[game.dealer_pos].player_id:
            raise GameEngineException("Player performing the action is not the current dealer")

        for pos, player in game.player_pos_dict.items():
            player.add_cards(game.deck.deal_cards(4))
