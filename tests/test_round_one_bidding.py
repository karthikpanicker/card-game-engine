import random
from unittest import TestCase

from engine import constants
from engine.game28.game28_state import Game28State
from engine.game28.game_28_settings import Game28Settings
from engine.game_engine_exception import GameEngineException
from engine.game_factory import GameFactory, GameType
from engine.player import Player, PlayerAction


class TestRoundOneBidding(TestCase):

    def setUp(self) -> None:
        self.settings = Game28Settings()

    def test_invalid_player_action(self):
        game = TestRoundOneBidding.create_game_for_testing()
        with self.assertRaises(GameEngineException) as context:
            game.player_action('player2', PlayerAction.CARD_PLAY_ACTION, {constants.BID_VALUE: constants.PASS})
        self.assertTrue('Invalid player action for the game state' in str(context.exception))

    def test_pass_by_first_player(self):
        game = TestRoundOneBidding.create_game_for_testing()
        with self.assertRaises(GameEngineException) as context:
            game.player_action('player2', PlayerAction.BIDDING_ACTION, {constants.BID_VALUE: constants.PASS})
        self.assertTrue('First player to bid cannot pass the bid' in str(context.exception))

    def test_wrong_player_starting_the_bidding(self):
        game = TestRoundOneBidding.create_game_for_testing()
        with self.assertRaises(GameEngineException) as context:
            game.player_action('player3', PlayerAction.BIDDING_ACTION, {constants.BID_VALUE: constants.PASS})
        self.assertTrue('Specified player is not the next bidder' in str(context.exception))

    def test_bid_by_first_player_below_min_bid_value(self):
        game = TestRoundOneBidding.create_game_for_testing()
        with self.assertRaises(GameEngineException) as context:
            game.player_action('player2', PlayerAction.BIDDING_ACTION,
                               {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE) - 1})
        self.assertTrue('Can\'t bid below or equal to the current bid value' in str(context.exception))

    def test_bid_by_first_player_min_bid_value(self):
        game = TestRoundOneBidding.create_game_for_testing()
        game.player_action('player2', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE),
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        self.assertEqual(game.current_bid_value, self.settings.get_setting_value(constants.MIN_BID_VALUE))

    def test_bid_by_second_player_below_previous_bid(self):
        game = TestRoundOneBidding.create_game_for_testing()
        game.player_action('player2', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE),
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        with self.assertRaises(GameEngineException) as context:
            game.player_action('player3', PlayerAction.BIDDING_ACTION,
                               {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE),
                                constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(
                                    game)})
        self.assertTrue('Can\'t bid below or equal to the current bid value' in str(context.exception))

    def test_bid_by_second_player_raising_bid_by_one(self):
        game = TestRoundOneBidding.create_game_for_testing()
        game.player_action('player2', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE),
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player3', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE) + 1,
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        self.assertEqual(game.current_bid_value, self.settings.get_setting_value(constants.MIN_BID_VALUE) + 1)
        self.assertEqual(game.next_bidder_pos, 4)

    def test_bid_by_second_player_passing_bid(self):
        game = TestRoundOneBidding.create_game_for_testing()
        game.player_action('player2', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE),
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player3', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: constants.PASS})
        self.assertEqual(game.current_bid_value, self.settings.get_setting_value(constants.MIN_BID_VALUE))
        self.assertEqual(game.get_next_bidder_pos(), 1)

    def test_bidding_opposition_pass_their_turn(self):
        game = TestRoundOneBidding.create_game_for_testing()
        game.player_action('player2', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE),
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player3', PlayerAction.BIDDING_ACTION, {constants.BID_VALUE: constants.PASS})
        game.player_action('player1', PlayerAction.BIDDING_ACTION, {constants.BID_VALUE: constants.PASS})
        self.assertEqual(game.next_minimum_bid_value, 20)
        self.assertEqual(game.get_next_bidder_pos(), 4)

    def test_bidding_everyone_passes_except_first(self):
        game = TestRoundOneBidding.create_game_for_testing()
        game.player_action('player2', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE),
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player3', PlayerAction.BIDDING_ACTION, {constants.BID_VALUE: constants.PASS})
        game.player_action('player1', PlayerAction.BIDDING_ACTION, {constants.BID_VALUE: constants.PASS})
        game.player_action('player4', PlayerAction.BIDDING_ACTION, {constants.BID_VALUE: constants.PASS})
        self.assertEqual(game.get_current_bid_value(), 14)
        self.assertEqual(game.state, Game28State.ROUND_ONE_BIDDING_DONE)

    def test_bidding_everyone_bids(self):
        game = TestRoundOneBidding.create_game_for_testing()
        game.player_action('player2', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE),
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player3', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE) + 1,
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player4', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE) + 2,
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        game.player_action('player1', PlayerAction.BIDDING_ACTION,
                           {constants.BID_VALUE: self.settings.get_setting_value(constants.MIN_BID_VALUE) + 3,
                            constants.TRUMP_CARD_ABBREVIATION: TestRoundOneBidding.get_random_card_abbreviation(game)})
        self.assertEqual(game.get_current_bid_value(), 17)
        self.assertEqual(game.state, Game28State.ROUND_ONE_BIDDING_DONE)

    @staticmethod
    def create_game_for_testing():
        player_dict = {1: Player('player1', 1), 2: Player('player2', 2), 3: Player('player3', 3),
                       4: Player('player4', 4), }
        game = GameFactory.get_game_implementation(GameType.TWENTY_EIGHT, player_dict, None)
        game.player_action('player1', PlayerAction.DEALING_ACTION, None)
        return game

    @staticmethod
    def get_random_card_abbreviation(game):
        player = game.player_pos_dict[game.get_next_bidder_pos()]
        card = random.choice(player.cards)
        return card.abbrev
