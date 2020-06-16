from typing import Dict

from pydealer import Card

from engine import constants
from engine.game import Game
from engine.game28.game28_state import Game28State
from engine.game_engine_exception import GameEngineException
from engine.game_round import GameRound
from engine.game_state import GameState
from engine.player import PlayerAction, Player


class GamePlay(GameState):
    def handle_player_action(self, player_id: str, action: PlayerAction, game: Game, action_data: Dict[str, object]):
        if action not in [PlayerAction.CARD_PLAY_ACTION, PlayerAction.SHOW_TRUMP_ACTION]:
            raise GameEngineException("Invalid player action for the game state")
        player = game.player_pos_dict[game.get_next_player_pos()]
        if player_id is not player.player_id:
            raise GameEngineException("Specified player is not the next player")
        if action is PlayerAction.CARD_PLAY_ACTION:
            return self.handle_card_play(game, action_data)
        elif action is PlayerAction.SHOW_TRUMP_ACTION:
            return self.handle_show_trump(game, player)

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

        game_round = GamePlay.get_or_initialize_game_round(game, player)
        GamePlay.check_for_cheating(game, card_played, player, game_round)
        game_round.add_player_card(player,card_played)

        if game_round.get_card_count() == len(game.player_pos_dict):
            trump_card = game.get_trump_card() if game.get_trump_shown() else None
            round_winner = game_round.summarize(trump_card)
            game.set_next_player_pos(game.find_player_position(round_winner))
            game.set_active_round(None)
        else:
            game.set_next_player_pos(game.get_next_pos(game.get_next_player_pos(), 1))

        player.remove_card(card_played)
        return game.state

    @staticmethod
    def handle_show_trump(game: Game, player: Player):
        game_round = GamePlay.get_or_initialize_game_round(game, player)
        GamePlay.check_for_cheating_trump_show(game, player, game_round)
        game.set_trump_shown(True)
        return Game28State.TRUMP_SHOWN

    @staticmethod
    def check_for_cheating(game, card_played: Card, player: Player, game_round: GameRound):
        if not game.settings.get_setting_value(constants.VALIDATE_GAME_PLAY):
            return
        if game_round.get_card_count() == 0:
            return
        first_card = game_round.get_first_card()
        if card_played.suit == first_card.suit:
            return
        for card in player.cards:
            if card.suit == first_card.suit:
                raise GameEngineException("Player has another card of the same suit as the current round")

    @staticmethod
    def check_for_cheating_trump_show(game, player, game_round: GameRound):
        if not game.settings.get_setting_value(constants.VALIDATE_GAME_PLAY):
            return
        if game_round.get_card_count() == 0:
            raise GameEngineException("Can't ask to show trump without playing a single card in the round")
        first_card = game_round.get_first_card()
        for card in player.cards:
            if card.suit == first_card.suit:
                raise GameEngineException("Can't ask to show trump when the player has the same suite")


    @staticmethod
    def get_or_initialize_game_round(game: GameRound, player: Player):
        game_round = game.get_active_round()
        if game.get_active_round() is None:
            game_round = GameRound(player)
            game.set_active_round(game_round)
        return game_round