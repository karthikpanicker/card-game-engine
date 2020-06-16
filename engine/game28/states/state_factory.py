from engine.game28.game28_state import Game28State
from engine.game28.states.game_play import GamePlay
from engine.game28.states.round_one_bidding import RoundOneBidding
from engine.game28.states.round_one_dealing import RoundOneDealing
from engine.game28.states.round_two_bidding import RoundTwoBidding
from engine.game28.states.round_two_dealing import RoundTwoDealing
from engine.game_state import GameState


class Game28StateFactory:
    @staticmethod
    def get_state_handler(state: Game28State) -> GameState:
        if state is Game28State.STATE_ZERO:
            return RoundOneDealing()
        elif state is Game28State.ROUND_ONE_DEALING_DONE:
            return RoundOneBidding()
        elif state is Game28State.ROUND_ONE_BIDDING_DONE:
            return RoundTwoDealing()
        elif state is Game28State.ROUND_TWO_DEALING_DONE:
            return RoundTwoBidding()
        elif state in [Game28State.ROUND_TWO_BIDDING_DONE, Game28State.TRUMP_SHOWN]:
            return GamePlay()