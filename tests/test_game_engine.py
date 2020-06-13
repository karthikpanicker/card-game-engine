from unittest import TestCase

from engine.game_engine import GameEngine


class TestGameEngine(TestCase):
    def test_begin_session(self):
        game_engine = GameEngine()
        game_engine.begin_session(['player1'])
