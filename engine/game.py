from enum import Enum
from typing import List

from engine.game_round import GameRound


class GameState(Enum):
    ZERO_STATE = 1
    ROUND_ONE_DEALING_DONE = 2
    ROUND_TWO_DEALING_DONE = 2
    GAME_DONE = 3

"""
Game represents multiple rounds of play between the players until a decision on the winner and loser is made
"""


class Game:
    state: GameState
    gameRounds: List[GameRound]

    def __init__(self):
        state = GameState.ZERO_STATE
