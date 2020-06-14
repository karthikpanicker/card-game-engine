from unittest import TestCase

from pydealer import Card
from pydealer import SUITS, VALUES

from engine.game_round import GameRound
from engine.player import Player


class TestGameRound(TestCase):
    def test_summarize(self):
        player1 = Player('player1', 1)
        player2 = Player('player2', 1)
        player3 = Player('player3', 1)
        player4 = Player('player4', 1)
        game_round = GameRound(player1)
        game_round.add_player_card(player1, Card("9", "DIAMONDS"))
        game_round.add_player_card(player2, Card("1", "DIAMONDS"))
        game_round.add_player_card(player1, Card("8", "DIAMONDS"))
        game_round.add_player_card(player1, Card("7", "DIAMONDS"))
        game_round.summarize(None)
        #self.assertEqual(player1.get_points(), 3)


