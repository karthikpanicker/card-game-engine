from typing import List, Dict

from engine.game import Game
from engine.game28.g28_dealer_action_executor import G28DealerActionExecutor
from engine.game_round import GameRound
from engine.game_state import GameState
from engine.game28.gm_28_deck import Game28Deck
from engine.player import Player, PlayerAction

"""
Game represents multiple rounds of play between the players until a decision on the winner and loser is made
"""


class Game28(Game):
    state: GameState
    gameRounds: List[GameRound]
    deck: Game28Deck

    def __init__(self, player_pos_dict, prev_game: Game):
        self.state = GameState()
        self.deck = Game28Deck()
        self.player_pos_dict = player_pos_dict
        self.prev_game: Game28 = prev_game
        self.initialize_game()

    def player_action(self, player_id: str, action: PlayerAction, action_data):
        if action is PlayerAction.DEALING_ACTION:
            G28DealerActionExecutor()


