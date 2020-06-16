from enum import Enum
from typing import List

from pydealer import Card

from engine.team import Team


class PlayerAction(Enum):
    DEALING_ACTION = 0
    BIDDING_ACTION = 1
    CARD_PLAY_ACTION = 2
    SHOW_TRUMP_ACTION = 3


class Player:
    def __init__(self, player_id: str, position: int):
        self.player_id: str = player_id
        self.cards: List[Card] = []
        self.position = position
        self.points = 0
        self.team: Team = None

    def add_cards(self, cards: List[Card]):
        self.cards.extend(cards)

    def add_card(self, card: Card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards

    def remove_card(self,card):
        self.cards.remove(card)

    def add_points(self, point):
        self.points += point

    def get_points(self):
        return self.points

    def set_team(self, value):
        self._team = value

    def get_team(self) -> Team:
        return self._team

    def __str__(self):
        return str.format("{{Player id: {}}}", self.player_id)

    def __repr__(self):
        return str.format("{{Player id: {}}}", self.player_id)

    team = property(get_team, set_team)

