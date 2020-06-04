from enum import Enum


class GameStateConstants(Enum):
    STATE_ZERO = 1
    ROUND_ONE_BIDDING_DONE = 2
    ROUND_TWO_BIDDING_DONE = 3
    TRUMP_SHOWN = 4
    GAME_OVER = 5


class GameState():
    def __init__(self):
        self.game_state: GameStateConstants = GameStateConstants.STATE_ZERO