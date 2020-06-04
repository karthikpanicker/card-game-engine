"""
A game session would involve a set of players playing multiple games.
"""


class GameSession:
    session_id: str

    def __init__(self, players=[]):
        self.session_id = self.generateSession()
        self.players = players
