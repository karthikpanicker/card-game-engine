from typing import Dict

from engine import constants
from engine.game import Game
from engine.game_engine_exception import GameEngineException
from engine.game_state import GameState
from engine.player import PlayerAction


class BiddingBase(GameState):
    def handle_player_action(self, player_id: str, action: PlayerAction, game: Game, action_data: Dict[str, object]):
        if action is not PlayerAction.BIDDING_ACTION:
            raise GameEngineException("Invalid player action for the game state")
        player = game.player_pos_dict[game.get_next_bidder_pos()]
        if player_id is not player.player_id:
            raise GameEngineException("Specified player is not the next bidder")
        value = action_data[constants.BID_VALUE]
        if value != constants.PASS:
            if int(value) < game.get_next_minimum_bid_value():
                raise GameEngineException("Can't bid below or equal to the current bid value")
            if constants.TRUMP_CARD_ABBREVIATION not in action_data:
                raise GameEngineException("Choose a trump card for bidding")
            trump_card = action_data[constants.TRUMP_CARD_ABBREVIATION]
            for card in player.cards:
                if card.abbrev == trump_card:
                    self.set_trump_details(card, player, game)
            if game.get_trump_card() is None:
                raise GameEngineException("Trump card specified is not in players hand")
            game.set_current_bid_value(int(value))


    @staticmethod
    def set_trump_details(card, player, game: Game):
        # If there is an already set trump by a previous bidder, added it back to his hand.
        if game.get_trump_card_player() is not None:
            game.get_trump_card_player().add_card(game.get_trump_card())
        game.set_trump_card(card)
        game.set_trump_card_player(player)
        player.remove_card(card)