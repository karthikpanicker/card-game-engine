from unittest import TestCase

from engine.game28.gm_28_deck import Game28Deck


class TestGame28Deck(TestCase):
    def test_reset_deck(self):
        deck = Game28Deck()
        deck.reset_deck()

    def test_get_stack_for_deck(self):
        self.assertEqual(len(Game28Deck().get_stack_for_deck().cards), 32)
