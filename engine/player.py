from typing import List

from pydealer import Card


class Player:
    def __init__(self, player_id: str, position: int):
        self.player_id: str = player_id
        self.cards: List[Card] = []
        self.position = position

    def add_cards(self, cards: List[Card]):
        self.cards.extend(cards)

    def add_card(self, card : Card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards
