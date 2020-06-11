from typing import List

from pydealer import Deck, SUITS, VALUES, Stack, Card


class Game28Deck:
    deck: Deck

    def __init__(self):
        self.deck = Deck()
        self.deck.empty()
        self.deck.add(Game28Deck.get_stack_for_deck())
        self.deck.shuffle()

    def reset_deck(self):
        self.deck = Deck(cards=self.get_stack_for_deck())

    def get_all_cards(self):
        return self.deck.cards

    def deal_cards(self, count):
        # TODO: might have to group this by suite
        return self.deck.deal(count)

    @staticmethod
    def get_stack_for_deck():
        stack: Stack = Stack();
        cards: List[Card] = []
        for suit in SUITS:
            for value in VALUES:
                if value not in ["2", "3", "4", "5", "6"]:
                    cards.append(Card(value, suit))
        stack.add(cards)
        return stack
