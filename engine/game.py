import abc
from typing import Dict, List

from pydealer import Card

from engine.game_round import GameRound
from engine.player import PlayerAction, Player


class Game(abc.ABC):
    dealer_pos: int
    player_pos_dict: Dict[int, Player]
    # TODO: This might recursively refer older games and would sit in memory. Have to take a call on this.
    prev_game: 'Game'
    first_bidder_pos: int
    current_bid_value: int
    final_bid_value: int
    next_minimum_bid_value: int
    next_bidder_pos: int
    bid_history_dict: Dict[int, int]
    next_player_pos: int
    active_round: GameRound
    game_rounds: List[GameRound]

    @abc.abstractmethod
    def player_action(self, player_id: str, action: PlayerAction, action_data):
        pass

    def initialize_game(self):
        self.first_bidder_pos = 0
        self.next_minimum_bid_value = 0
        self.bid_history_dict = {}
        self.set_dealer_pos()
        self.set_bidder_pos()
        self.current_bid_value = 0
        self.active_round = None
        self.trump_shown = False
        self.game_rounds = []
        self.current_trump_card_player = None

    def set_dealer_pos(self):
        if self.prev_game is not None:
            self.dealer_pos = self.get_next_pos(self.prev_game.dealer_pos)
        else:
            self.dealer_pos = 1

    def set_bidder_pos(self):
        self.first_bidder_pos = self.get_next_pos(self.dealer_pos)
        self.next_bidder_pos = self.first_bidder_pos
        self.next_player_pos = self.first_bidder_pos

    def get_next_pos(self, pos, increment_by: int = 1):
        next_pos = pos
        stride = 1 if increment_by > 0 else -1
        for value in range(0, increment_by, stride):
            next_pos += stride
            if next_pos > len(self.player_pos_dict):
                next_pos = 1
            if next_pos < 1:
                next_pos = len(self.player_pos_dict)
        return next_pos

    def find_player_position(self, player: Player):
        for pos, p in self.player_pos_dict.items():
            if player.player_id == p.player_id:
                return pos

    def get_current_bid_value(self):
        return self.current_bid_value

    def get_final_bid_value(self):
        return self.final_bid_value

    def get_next_minimum_bid_value(self):
        return self.next_minimum_bid_value

    def get_current_bidder_pos(self):
        return self.__current_bidder_pos

    def set_next_minimum_bid_value(self, value):
        self.next_minimum_bid_value = value

    def set_current_bid_value(self, value):
        self.current_bid_value = value

    def set_bidder_history(self, position, bid_value):
        self.bid_history_dict[position] = bid_value

    def get_bidder_history(self):
        return self.bid_history_dict

    def set_next_bidder_pos(self, position):
        self.next_bidder_pos = position

    def get_next_bidder_pos(self):
        return self.next_bidder_pos

    def get_first_bidder_pos(self):
        return self.first_bidder_pos

    def get_trump_card(self):
        return self._current_trump_card

    def set_trump_card(self, card: Card):
        self._current_trump_card = card

    def get_next_player_pos(self):
        return self._next_player_pos

    def set_next_player_pos(self, value):
        self._next_player_pos = value

    def get_active_round(self):
        return self._active_round

    def set_active_round(self, value):
        self._active_round = value
        if value is not None: self.game_rounds.append(value)

    def set_trump_shown(self, value):
        self._trump_shown = value

    def get_trump_shown(self):
        return self._trump_shown

    def set_trump_card_player(self, value: Player):
        self._current_trump_card_player = value

    def get_trump_card_player(self) -> Player:
        return self._current_trump_card_player

    next_player_pos = property(get_next_player_pos, set_next_player_pos)
    active_round = property(get_active_round, set_active_round)
    trump_shown = property(get_trump_shown, set_trump_shown)
    current_trump_card = property(get_trump_card, set_trump_card)
    current_trump_card_player = property(get_trump_card_player, set_trump_card_player)
