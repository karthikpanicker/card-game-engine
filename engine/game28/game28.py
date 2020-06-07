from enum import Enum
from typing import List, Dict

from engine.game import Game
from engine.game28.states.g28_state_zero import G28StateZero
from engine.game_round import GameRound
from engine.game28.gm_28_deck import Game28Deck
from engine.player import Player, PlayerAction


class Game28State(Enum):
    STATE_ZERO = 1
    ROUND_ONE_DEALING_DONE = 2
    ROUND_ONE_BIDDING_DONE = 3
    ROUND_TWO_DEALING_DONE = 4
    ROUND_TWO_BIDDING_DONE = 5
    TRUMP_SHOWN = 6
    GAME_OVER = 7


"""
Game represents multiple rounds of play between the players until a decision on the winner and loser is made
"""


class Game28(Game):
    state: Game28State
    gameRounds: List[GameRound]
    deck: Game28Deck

    def __init__(self, player_pos_dict: Dict[int, Player], prev_game: Game):
        self.state: Game28State = Game28State.STATE_ZERO
        self.deck = Game28Deck()
        self.player_pos_dict = player_pos_dict
        self.prev_game: Game28 = prev_game
        self.initialize_game()

    def get_game_state(self):
        return self.state

    def set_game_state(self, game_state: Game28State):
        self.state = game_state

    def player_action(self, player_id: str, action: PlayerAction, action_data: Dict[str, object] = {}):
        if self.state is Game28State.STATE_ZERO:
            G28StateZero.handle_player_action(player_id, action, self, action_data)
