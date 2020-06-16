from unittest import TestCase

from engine.game_engine_exception import GameEngineException
from engine.game_session import GameSession


class TestGameSession(TestCase):
    def test_generate_session(self):
        session = GameSession(['player1','player2','player3','player4'])
        self.assertIsNotNone(session.get_session_id())

    def test_allocate_seats(self):
        session = GameSession(['player1','player2','player3','player4'])
        player_positions = session.get_seat_allocations()
        self.assertEqual(4,len(player_positions))
        s1 = set([1,2,3,4])
        self.assertTrue(s1.issubset(player_positions.keys()))

    def test_add_player_to_session_without_seat(self):
        session = GameSession(['player1','player2','player3','player4'])
        with self.assertRaises(GameEngineException) as context:
            session.add_player_to_session('player5')
        self.assertTrue('No free position available for allocation' in str(context.exception))

    def test_add_player_to_session_with_free_seat(self):
        session = GameSession(['player1','player2','player3'])
        self.assertEqual(3, len(session.get_seat_allocations()))
        new_allocation = session.add_player_to_session('player4')
        self.assertEqual(4,len(new_allocation))

    def test_change_player_pos_with_free_pos(self):
        session = GameSession(['player1', 'player2', 'player3'])
        session.change_player_pos(4, 'player1')
        self.assertEqual(4, session.get_player_position_and_details('player1')[0])
        self.assertIsNone(session.get_player_at_position(1))

    def test_change_player_pos_with_new_player(self):
        session = GameSession(['player1', 'player2', 'player3', 'player4'])
        with self.assertRaises(GameEngineException) as context:
            session.change_player_pos(4, 'player5')
        self.assertTrue('Player not part of this game session' in str(context.exception))

    def test_change_player_pos_new_player_invalid_player_position(self):
        session = GameSession(['player1', 'player2', 'player3', 'player4'])
        with self.assertRaises(GameEngineException) as context:
            session.change_player_pos(5, 'player5')
        self.assertTrue('Position invalid for maximum number of 4 players' in str(context.exception))

    def test_get_player_position_and_details(self):
        session = GameSession(['player1', 'player2', 'player3', 'player4'])
        self.assertEqual(1, session.get_player_position_and_details('player1')[0])

    def test_can_start_game_without_seats_filled(self):
        session = GameSession(['player1', 'player2', 'player3'])
        self.assertFalse(session.can_start_game())

    def test_can_start_game_with_seats_filled(self):
        session = GameSession(['player1', 'player2', 'player3','player4'])
        self.assertTrue(session.can_start_game())

    def test_start_game(self):
        session = GameSession(['player1', 'player2', 'player3', 'player4'])
        session.start_game()
        first_player_team = session.get_player_at_position(1).get_team()
        self.assertTrue(all(item in [1,3] for item in first_player_team.get_player_positions()))