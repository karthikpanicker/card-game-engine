from enum import Enum
from typing import List

from engine.game_round import GameRound
from engine.game_state import GameState

"""
Game represents multiple rounds of play between the players until a decision on the winner and loser is made
"""


class Game:
    state: GameState
    gameRounds: List[GameRound]

    def __init__(self):
        state = GameState()
