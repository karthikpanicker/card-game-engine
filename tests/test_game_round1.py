from unittest import TestCase

from pydealer import Card

from engine.game_round import GameRound
from engine.player import Player


class TestGameRound(TestCase):
    def test_summarize(self):
        self.fail()

    def test_round(self):
        print("ssssss")
        player1 = Player("player1", 1)
        player2 = Player("player2", 2)
        player3 = Player("player3", 3)
        player4 = Player("player4", 4)

        game_round = GameRound(player1)
        game_round.add_player_card(player1, Card("9", "DIAMONDS"))
        game_round.add_player_card(player2, Card("Ace", "DIAMONDS"))
        game_round.add_player_card(player3, Card("8", "DIAMONDS"))
        game_round.add_player_card(player4, Card("7", "DIAMONDS"))

        game_round.summarize(None)
        self.assertEqual(player1.get_points(), 3)
