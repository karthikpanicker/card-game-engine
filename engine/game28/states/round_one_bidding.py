from typing import Dict

from engine.game import Game
from engine.game28.game28 import Game28State
from engine.game_engine_exception import GameEngineException
from engine.game_state import GameState
from engine.player import PlayerAction
import engine.constants as constants


class RoundOneBidding(GameState):

    def handle_player_action(self, player_id: str, action: PlayerAction, game: Game, action_data: Dict[str, object]):
        if action is not PlayerAction.BIDDING_ACTION:
            raise GameEngineException("Invalid player action for the game state")
        bid_value = action_data[constants.BID_VALUE]
        if player_id is not game.player_pos_dict[game.get_next_bidder_pos()].player_id:
            raise GameEngineException("Specified player is not the next bidder")
        if bid_value is constants.PASS:
            self.validate_pass(game)
        return self.process_bid_value(bid_value, game)

    @staticmethod
    def validate_pass(game: Game):
        if game.get_current_bid_value() is 0:
            raise GameEngineException("First player to bid cannot pass the bid")

    def process_bid_value(self, value, game):
        if value != constants.PASS:
            if int(value) < game.get_next_minimum_bid_value():
                raise GameEngineException("Can't bid below or equal to the current bid value")
            game.set_current_bid_value(int(value))
        bidder_pos = game.get_next_bidder_pos()
        game.set_bidder_history(bidder_pos,value)
        return self.find_and_set_next_bidder_pos_and_bid_value(game, value, bidder_pos)

    @staticmethod
    def find_and_set_next_bidder_pos_and_bid_value(game, bid_value, current_position):
        nxt_bidder_pos = 0
        nxt_bid_value = game.get_current_bid_value() if bid_value is constants.PASS else int(bid_value)
        state = Game28State.ROUND_ONE_DEALING_DONE
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
                nxt_bid_value = game.settings.get_setting_value(constants.FIRST_ROUND_HONORS_MIN)
            else:
                nxt_bidder_pos = game.get_next_pos(current_position, 1)
                nxt_bid_value += 1
        elif len(game.get_bidder_history()) == 4:
            state = Game28State.ROUND_ONE_BIDDING_DONE
            nxt_bid_value = game.settings.get_setting_value(constants.SECOND_ROUND_HONORS_MIN)
            nxt_bidder_pos = game.get_first_bidder_pos()

        game.set_next_bidder_pos(nxt_bidder_pos)
        game.set_next_minimum_bid_value(nxt_bid_value)
        if bid_value != constants.PASS:
            game.set_current_bid_value(int(bid_value))
        return state
