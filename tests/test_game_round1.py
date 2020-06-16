from unittest import TestCase

from pydealer import Card

from engine.game_round import GameRound
from engine.player import Player


class TestGameRound(TestCase):
    # All cards same suit.. No trump.. First player wins
    def test_1_first_player_wins_no_trump(self):
        player1 = Player("player1", 1)
        player2 = Player("player2", 2)
        player3 = Player("player3", 3)
        player4 = Player("player4", 4)
        game_round = GameRound(player1)

        game_round.add_player_card(player1, Card("9", "DIAMONDS"))
        game_round.add_player_card(player2, Card("Ace", "DIAMONDS"))
        game_round.add_player_card(player3, Card("8", "DIAMONDS"))
        game_round.add_player_card(player4, Card("10", "DIAMONDS"))

        game_round.summarize()
        self.assertEqual(player1.get_points(), 4)

        # All cards same suit.. No trump.. second player wins
    def test_2_second_player_wins_no_trump(self):
        player1 = Player("player1", 1)
        player2 = Player("player2", 2)
        player3 = Player("player3", 3)
        player4 = Player("player4", 4)
        game_round = GameRound(player1)

        game_round.add_player_card(player1, Card("9", "DIAMONDS"))
        game_round.add_player_card(player2, Card("Jack", "DIAMONDS"))
        game_round.add_player_card(player3, Card("8", "DIAMONDS"))
        game_round.add_player_card(player4, Card("10", "DIAMONDS"))

        game_round.summarize()
        self.assertEqual(player2.get_points(), 6)

    # All cards same value and diff suit.. No trump.. First player wins
    def test_3_first_player_wins_no_trump(self):
        player1 = Player("player1", 1)
        player2 = Player("player2", 2)
        player3 = Player("player3", 3)
        player4 = Player("player4", 4)
        game_round = GameRound(player1)

        game_round.add_player_card(player1, Card("9", "DIAMONDS"))
        game_round.add_player_card(player2, Card("9", "Hearts"))
        game_round.add_player_card(player3, Card("9", "Spade"))
        game_round.add_player_card(player4, Card("9", "Clubs"))

        game_round.summarize()
        self.assertEqual(player1.get_points(), 8)

    # All cards zero value and diff suit.. No trump.. First player wins
    def test_4_first_player_wins_no_trump(self):
        player1 = Player("player1", 1)
        player2 = Player("player2", 2)
        player3 = Player("player3", 3)
        player4 = Player("player4", 4)
        game_round = GameRound(player1)

        game_round.add_player_card(player1, Card("7", "DIAMONDS"))
        game_round.add_player_card(player2, Card("8", "Hearts"))
        game_round.add_player_card(player3, Card("7", "Spade"))
        game_round.add_player_card(player4, Card("7", "Clubs"))

        game_round.summarize()
        self.assertEqual(player1.get_points(), 0)

        # Trump lifted and played by third player.. Third player wins
    def test_5_first_player_wins_no_trump(self):
        player1 = Player("player1", 1)
        player2 = Player("player2", 2)
        player3 = Player("player3", 3)
        player4 = Player("player4", 4)
        game_round = GameRound(player1)

        game_round.add_player_card(player1, Card("Jack", "DIAMONDS"))
        game_round.add_player_card(player2, Card("8", "DIAMONDS"))
        game_round.add_player_card(player3, Card("10", "DIAMONDS"))
        game_round.add_player_card(player4, Card("7", "SPADE"))
        game_round.set_trump_card_details(player4, Card("7", "SPADE"))

        game_round.summarize()
        self.assertEqual(player4.get_points(), 4)

        # Trump lifted and played by fourth player.. He wins
    def test_6_first_player_wins_no_trump(self):
        player1 = Player("player1", 1)
        player2 = Player("player2", 2)
        player3 = Player("player3", 3)
        player4 = Player("player4", 4)
        game_round = GameRound(player1)

        game_round.add_player_card(player1, Card("Jack", "DIAMONDS"))
        game_round.add_player_card(player2, Card("8", "DIAMONDS"))
        game_round.add_player_card(player3, Card("10", "DIAMONDS"))
        game_round.add_player_card(player4, Card("7", "SPADE"))
        game_round.set_trump_card_details(player4, Card("7", "SPADE"))

        game_round.summarize()
        self.assertEqual(player4.get_points(), 4)

        # Trump lifted and passed by fourth player.. First player wins
    def test_7_first_player_wins_no_trump(self):
        player1 = Player("player1", 1)
        player2 = Player("player2", 2)
        player3 = Player("player3", 3)
        player4 = Player("player4", 4)
        game_round = GameRound(player1)

        game_round.add_player_card(player1, Card("Jack", "DIAMONDS"))
        game_round.add_player_card(player2, Card("8", "DIAMONDS"))
        game_round.add_player_card(player3, Card("10", "DIAMONDS"))
        game_round.add_player_card(player4, Card("7", "Hearts"))
        game_round.set_trump_card_details(player4, Card("7", "SPADE"))

        game_round.summarize()
        self.assertEqual(player1.get_points(), 4)


        # Trump lifted and played by fourth player.. second player had passed a card of trump suit. Fourth wins
    def test_8_first_player_wins_no_trump(self):
        player1 = Player("player1", 1)
        player2 = Player("player2", 2)
        player3 = Player("player3", 3)
        player4 = Player("player4", 4)
        game_round = GameRound(player1)

        game_round.add_player_card(player1, Card("Jack", "DIAMONDS"))
        game_round.add_player_card(player2, Card("10", "SPADE"))
        game_round.add_player_card(player3, Card("10", "DIAMONDS"))
        game_round.add_player_card(player4, Card("7", "SPADE"))
        game_round.set_trump_card_details(player4, Card("7", "SPADE"))

        game_round.summarize()
        self.assertEqual(player4.get_points(), 5)

        # Trump lifted in some previous round.. In that case the trump_lifted_player will be blank
        # No trump in this round. Player 3 wins
    def test_9_first_player_wins_no_trump(self):
        player1 = Player("player1", 1)
        player2 = Player("player2", 2)
        player3 = Player("player3", 3)
        player4 = Player("player4", 4)
        game_round = GameRound(player1)

        game_round.add_player_card(player1, Card("King", "DIAMONDS"))
        game_round.add_player_card(player2, Card("10", "Hearts"))
        game_round.add_player_card(player3, Card("10", "DIAMONDS"))
        game_round.add_player_card(player4, Card("7", "Hearts"))
        # game_round.set_trump_card_details(, Card("7", "SPADE"))
        game_round.trump_lift_player = Player(0,0)
        game_round.trump_card = Card("7", "SPADE")

        game_round.summarize()
        self.assertEqual(player3.get_points(), 2)

    # Trump lifted in some previous round.. In that case the trump_lifted_player will be blank
    # All trump in this round. Player 3 wins
    def test_10_first_player_wins_all_trump(self):
        player1 = Player("player1", 1)
        player2 = Player("player2", 2)
        player3 = Player("player3", 3)
        player4 = Player("player4", 4)
        game_round = GameRound(player1)

        game_round.add_player_card(player1, Card("King", "SPADE"))
        game_round.add_player_card(player2, Card("10", "SPADE"))
        game_round.add_player_card(player3, Card("9", "SPADE"))
        game_round.add_player_card(player4, Card("7", "SPADE"))
        # game_round.set_trump_card_details(, Card("7", "SPADE"))
        game_round.trump_lift_player = Player(0,0)
        game_round.trump_card = Card("7", "SPADE")

        game_round.summarize()
        self.assertEqual(player3.get_points(), 3)
