from typing import Dict

from engine import constants
from engine.game import Game
from engine.game28.game28_state import Game28State
from engine.game_engine_exception import GameEngineException
from engine.game_state import GameState
from engine.player import PlayerAction


class RoundTwoBidding(GameState):
    @staticmethod
    def handle_player_action(player_id: str, action: PlayerAction, game: Game, action_data: Dict[str, object]):
        if action is not PlayerAction.BIDDING_ACTION:
            raise GameEngineException("Invalid player action for the game state")
        bid_value = action_data[constants.BID_VALUE]
        if player_id is not game.player_pos_dict[game.get_next_bidder_pos()].player_id:
            raise GameEngineException("Specified player is not the next bidder")
        if bid_value != constants.PASS:
            if int(bid_value) < game.get_next_minimum_bid_value():
                raise GameEngineException("Can't bid below or equal to the current bid value")
            game.set_current_bid_value(int(bid_value))
        bidder_pos = game.get_next_bidder_pos()
        game.set_bidder_history(bidder_pos,bid_value)
        return RoundTwoBidding.find_and_set_next_bidder_pos_and_bid_value(game, bid_value, bidder_pos)

    @staticmethod
    def find_and_set_next_bidder_pos_and_bid_value(game, bid_value, current_position):
        nxt_bid_value = game.get_current_bid_value() if bid_value is constants.PASS else int(bid_value)
        state = Game28State.ROUND_TWO_DEALING_DONE
        nxt_bidder_pos = game.get_next_pos(current_position)
        if bid_value is not constants.PASS: nxt_bid_value += 1
        game.set_next_bidder_pos(nxt_bidder_pos)
        game.set_next_minimum_bid_value(nxt_bid_value)
        if len(game.get_bidder_history()) is 8: state = Game28State.ROUND_TWO_BIDDING_DONE
        if bid_value != constants.PASS:
            game.set_current_bid_value(int(bid_value))
        return state
