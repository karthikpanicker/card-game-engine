from enum import Enum
from typing import List, Dict

from engine import constants
from engine.game import Game
from engine.game28.game28_state import Game28State
from engine.game28.game_28_settings import Game28Settings
from engine.game28.states.round_two_bidding import RoundTwoBidding
from engine.game28.states.round_two_dealing import RoundTwoDealing
from engine.game28.states.round_one_bidding import RoundOneBidding
from engine.game28.states.round_one_dealing import RoundOneDealing
from engine.game28.states.state_factory import Game28StateFactory
from engine.game_round import GameRound
from engine.game28.gm_28_deck import Game28Deck
from engine.player import Player, PlayerAction

"""
Game represents multiple rounds of play between the players until a decision on the winner and loser is made
"""


class Game28(Game):
    state: Game28State
    deck: Game28Deck
    settings: Game28Settings

    def __init__(self, player_pos_dict: Dict[int, Player], prev_game: Game):
        self.state: Game28State = Game28State.STATE_ZERO
        self.deck = Game28Deck()
        self.player_pos_dict = player_pos_dict
        self.prev_game: Game28 = prev_game
        self.initialize_game()
        self.settings = Game28Settings()
        self.next_minimum_bid_value = self.settings.get_setting_value(constants.MIN_BID_VALUE)

    def get_game_state(self):
        return self.state

    def set_game_state(self, game_state: Game28State):
        self.state = game_state

    def player_action(self, player_id: str, action: PlayerAction, action_data: Dict[str, object] = {}):
        state_handler = Game28StateFactory.get_state_handler(self.state)
        self.state = state_handler.handle_player_action(player_id, action, self, action_data)