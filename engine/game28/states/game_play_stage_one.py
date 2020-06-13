from typing import Dict

from engine import constants
from engine.game import Game
from engine.game28.states.game_play_base import GamePlayBase
from engine.game_engine_exception import GameEngineException
from engine.game_round import GameRound
from engine.player import PlayerAction


class GamePlayStageOne(GamePlayBase):
    def handle_player_action(self, player_id: str, action: PlayerAction, game: Game, action_data: Dict[str, object]):
        super().handle_player_action(player_id, action, game, action_data)
        if action is PlayerAction.CARD_PLAY_ACTION:
            self.handle_card_play()

    @staticmethod
    def handle_card_play(game, action_data):
        if constants.CARD_ABBREVIATION not in action_data:
            raise GameEngineException("Card details not found")
        card_played = None
        player = game.player_pos_dict[game.get_next_player_pos()]
        for card in player.cards:
            if card.abbrev == action_data[constants.CARD_ABBREVIATION]:
                card_played = card
        if card_played is None:
            raise GameEngineException("Card doesnt belong to this player")

        game_round = game.get_active_round()
        if game.get_active_round() is None:
            game_round = GameRound(player)
            game.set_active_round(round)
        game_round.add_player_card(player,card_played)

        if game_round.get_card_count() == len(game.player_pos_dict):
            game_round.summarize(game.get_trump_card())
            game.set_active_round(None)