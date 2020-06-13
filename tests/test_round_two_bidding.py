from unittest import TestCase

from engine import constants
from engine.game_engine_exception import GameEngineException
from engine.game_factory import GameFactory, GameType
from engine.player import Player, PlayerAction
from tests.test_round_one_bidding import TestRoundOneBidding


class TestRoundTwoBidding(TestCase):
    def test_2nd_round_bidding_first_player_bid_min_honors(self):
        game = TestRoundTwoBidding.create_game_for_testing()
        game.player_action('player2', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: game.settings.get_setting_value(constants.SECOND_ROUND_HONORS_MIN),
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        self.assertEqual(game.get_next_minimum_bid_value(),
                         game.settings.get_setting_value(constants.SECOND_ROUND_HONORS_MIN) + 1)

    def test_2nd_round_bidding_wrong_first_player(self):
        game = TestRoundTwoBidding.create_game_for_testing()
        with self.assertRaises(GameEngineException) as context:
            game.player_action('player1', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: game.settings.get_setting_value(constants.SECOND_ROUND_HONORS_MIN)})

        self.assertTrue("Specified player is not the next bidder" in str(context.exception))

    def test_2nd_round_bidding_second_player_doesnt_raise_bid(self):
        game = TestRoundTwoBidding.create_game_for_testing()
        game.player_action('player2', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: game.settings.get_setting_value(constants.SECOND_ROUND_HONORS_MIN)})
        with self.assertRaises(GameEngineException) as context:
            game.player_action('player3', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: game.settings.get_setting_value(constants.SECOND_ROUND_HONORS_MIN)})

        self.assertTrue("Specified player is not the next bidder" in str(context.exception))

    def test_2nd_round_bidding_second_player_doesnt_raise_bid(self):
        game = TestRoundTwoBidding.create_game_for_testing()
        game.player_action('player2', PlayerAction.BIDDING_ACTION,
                        {constants.BID_VALUE: game.settings.get_setting_value(constants.SECOND_ROUND_HONORS_MIN),
                         constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player3', PlayerAction.BIDDING_ACTION,
                        {constants.BID_VALUE: game.settings.get_setting_value(constants.SECOND_ROUND_HONORS_MIN) + 1,
                         constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player4', PlayerAction.BIDDING_ACTION, {constants.BID_VALUE: constants.PASS})
        game.player_action('player1', PlayerAction.BIDDING_ACTION,
                        {constants.BID_VALUE: game.settings.get_setting_value(constants.SECOND_ROUND_HONORS_MIN) + 2,
                         constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        self.assertEqual(game.get_current_bid_value(), game.settings.get_setting_value(constants.SECOND_ROUND_HONORS_MIN) + 2)

    @staticmethod
    def create_game_for_testing():
        player_dict = {1: Player('player1', 1), 2: Player('player2', 2), 3: Player('player3', 3),
                       4: Player('player4', 4), }
        game = GameFactory.get_game_implementation(GameType.TWENTY_EIGHT, player_dict, None)
        game.player_action('player1', PlayerAction.DEALING_ACTION, None)
        game.player_action('player2', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: game.settings.get_setting_value(constants.MIN_BID_VALUE),
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player3', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: game.settings.get_setting_value(constants.MIN_BID_VALUE) + 1,
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player4', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: game.settings.get_setting_value(constants.MIN_BID_VALUE) + 2,
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player1', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: game.settings.get_setting_value(constants.MIN_BID_VALUE) + 3,
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player1', PlayerAction.DEALING_ACTION, None)
        return game
