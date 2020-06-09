from typing import Dict

from engine.game import Game
from engine.game_engine_exception import GameEngineException
from engine.game_state import GameState
from engine.player import PlayerAction
import engine.constants as constants


class RoundOneDealingDone(GameState):

    @staticmethod
    def handle_player_action(player_id: str, action: PlayerAction, game: Game, action_data: Dict[str, object]):
        if action is not PlayerAction.BIDDING_ACTION:
            raise GameEngineException("Invalid player action for the game state")
        bid_value = action_data[constants.BID_VALUE]
        if bid_value is constants.PASS:
            RoundOneDealingDone.validate_pass(game)
            position = game.player_pos_dict[game.get_next_bidder_pos()].player_id
            game.set_bidder_history(position, constants.PASS)
        else:
            value = int(bid_value)
            RoundOneDealingDone.process_bid_value(player_id, value, game)

    @staticmethod
    def validate_pass(game: Game):
        if game.get_current_bid_value() is 0:
            raise GameEngineException("First player to bid cannot pass the bid.")

    @staticmethod
    def process_bid_value(player_id, value, game):
        if value < game.get_next_minimum_bid_value():
            raise GameEngineException("Can't bid below the current minimum value")
        if player_id is not game.player_pos_dict[game.get_next_bidder_pos()].player_id:
            raise GameEngineException("Specified player is not the next bidder.")
        game.set_current_bid_value(value)
        bidder_pos = game.get_next_bidder_pos()
        game.set_bidder_history(bidder_pos,value)
        RoundOneDealingDone.find_and_set_next_bidder_pos(game, value, bidder_pos)

    @staticmethod
    def find_and_set_next_bidder_pos_and_bid_value(game, bid_value, current_position):
        nxt_bidder_pos = 0
        nxt_bid_value = bid_value
        if len(game.get_bidder_history()) == 1:
            nxt_bidder_pos = game.get_next_pos(current_position)
            nxt_bid_value += 1
        elif len(game.get_bidder_history()) == 2:
            if len(list(filter(lambda x: x is constants.PASS, game.get_bidder_history().values()))) == 1:
                nxt_bidder_pos = game.get_next_pos(current_position, 2)
            else:
                nxt_bidder_pos = game.get_next_pos(current_position, 1)
            nxt_bid_value += 1
        elif len(game.get_bidder_history()) == 3:
            if len(list(filter(lambda x: x is constants.PASS, game.get_bidder_history().values()))) == 2:
                nxt_bidder_pos = game.get_next_pos(current_position, -1)
                nxt_bid_value = 20
            else:
                nxt_bidder_pos = game.get_next_pos(current_position, 1)
                nxt_bid_value += 1

        game.set_next_bidder_pos(nxt_bidder_pos, bid_value)

