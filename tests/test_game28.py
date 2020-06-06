from unittest import TestCase

from engine.game28.game28 import Game28


class TestGame28(TestCase):
    def test_game_initialization_no_prev_game(self):
        game = self.initialize_game(None)
        self.assertEqual(game.bidder_pos, 1)

    def test_game_initialization_with_prev_game(self):
        game1 = self.initialize_game(None)
        game2 = self.initialize_game(game1)
        self.assertEqual(game2.bidder_pos, 2)

    def test_game_initialization_full_round(self):
        game1 = self.initialize_game(None)
        game2 = self.initialize_game(game1)
        game3 = self.initialize_game(game2)
        game4 = self.initialize_game(game3)
        game5 = self.initialize_game(game4)
        self.assertEqual(game5.bidder_pos, 1)


    def test_player_action(self):
        pass

    @staticmethod
    def initialize_game(prev_game):
        player_pos_dict = {1: 'player1', 2: 'player2', 3: 'player3', 4: 'player4'}
        return Game28(player_pos_dict, prev_game)
