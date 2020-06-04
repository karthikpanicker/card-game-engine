from typing import Dict

from engine.game_session import GameSession


class GameEngine:
    # TODO: This is an inmemory session store. Have to be moved to a better mechanism
    sessionStore: Dict[str, GameSession] = {}

    def begin_session(self, player_ids):
        session = GameSession(player_ids)
        self.sessionStore[session.session_id, session]
        return session.session_id
