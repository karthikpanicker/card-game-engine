from typing import Dict

from engine.game import Game
from engine.game_engine_exception import GameEngineException
from engine.game_state import GameState
from engine.player import PlayerAction


class GamePlayBase(GameState):
    def handle_player_action(self, player_id: str, action: PlayerAction, game: Game, action_data: Dict[str, object]):
        if action not in [PlayerAction.CARD_PLAY_ACTION, PlayerAction.SHOW_TRUMP_ACTION]:
            raise GameEngineException("Invalid player action for the game state")
        player = game.player_pos_dict[game.get_next_player_pos()]
        if player_id is not player.player_id:
            raise GameEngineException("Specified player is not the next player")