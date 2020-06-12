from unittest import TestCase

from engine import constants
from engine.game28.game28_state import Game28State
from engine.game_engine_exception import GameEngineException
from engine.game_factory import GameType, GameFactory
from engine.player import Player, PlayerAction


class TestRoundTwoDealing(TestCase):
    def test_handle_player_action(self):
        game = TestRoundTwoDealing.create_game_for_testing()
        game.player_action('player1', PlayerAction.DEALING_ACTION, None)
        self.assertEqual(len(game.player_pos_dict[1].cards), 4)

    def test_handle_player_action(self):
        game = TestRoundTwoDealing.create_game_for_testing()
        with self.assertRaises(GameEngineException) as context:
            game.player_action('player1', PlayerAction.BIDDING_ACTION, None)
        self.assertTrue("Invalid player action for the game state", str(context.exception))

    @staticmethod
    def create_game_for_testing():
        player_dict = {1: Player('player1', 1), 2: Player('player2', 2), 3: Player('player3', 3),
                       4: Player('player4', 4), }
        game = GameFactory.get_game_implementation(GameType.TWENTY_EIGHT, player_dict, None)
        game.state = Game28State.ROUND_ONE_BIDDING_DONE
        return game