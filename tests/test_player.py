from unittest import TestCase

from pydealer import Card, VALUES, SUITS

from engine.player import Player


class TestPlayerMethods(TestCase):
    def test_add_and_retrieve_card(self):
        player = Player("2","3","1")
        card = Card(VALUES[0], SUITS[0])
        player.add_card(card)
        self.assertEqual(player.get_cards()[0].value, VALUES[0])
        self.assertEqual(player.get_cards()[0].suit, SUITS[0])

    def test_add_and_retrieve_cards(self):
        player = Player("2", "3", "1")
        card1 = Card(VALUES[0], SUITS[0])
        card2 = Card(VALUES[0], SUITS[0])
        player.add_cards([card1, card2])
        self.assertEqual(len(player.get_cards()), 2)