import abc
from typing import Dict

from engine.player import PlayerAction, Player


class Game(abc.ABC):
    dealer_pos: int
    player_pos_dict: Dict[int, Player]
    # TODO: This might recursively refer older games and would sit in memory. Have to take a call on this.
    prev_game: 'Game'
    __first_bidder_pos: int
    __current_bid_value: int
    __final_bid_value: int
    __next_minimum_bid_value: int
    __next_bidder_pos: int
    __bid_history_dict: Dict[int, int]

    @abc.abstractmethod
    def player_action(self, player_id: str, action: PlayerAction, action_data):
        pass

    def initialize_game(self):
        self.__bid_history_dict = {}
        self.set_dealer_pos()
        self.set_bidder_pos()
        self.__current_bid_value = 0

    def set_dealer_pos(self):
        if self.prev_game is not None:
            self.dealer_pos = self.get_next_pos(self.prev_game.dealer_pos)
        else:
            self.dealer_pos = 1

    def set_bidder_pos(self):
        self.__first_bidder_pos == self.get_next_pos(self.dealer_pos)
        self.__next_bidder_pos = self.__first_bidder_pos

    def get_next_pos(self, pos, increment_by: int = 1):
        next_pos = pos + increment_by
        if next_pos > len(self.player_pos_dict):
            next_pos = increment_by
        return next_pos

    def get_current_bid_value(self):
        return self.__current_bid_value

    def get_final_bid_value(self):
        return self.__final_bid_value

    def get_next_minimum_bid_value(self):
        return self.__next_minimum_bid_value

    def get_current_bidder_pos(self):
        return self.__current_bidder_pos

    def set_next_minimum_bid_value(self, value):
        self.__next_minimum_bid_value = value

    def set_current_bid_value(self, value):
        self.__current_bid_value, value

    def set_bidder_history(self, position, bid_value):
        self.__bid_history_dict[position] = bid_value

    def get_bidder_history(self, position, bid_value):
        return self.__bid_history_dict

    def set_next_bidder_pos(self, position):
        self.__next_bidder_pos = position

    def get_next_bidder_pos(self):
        return self.__next_bidder_pos
