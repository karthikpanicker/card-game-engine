from typing import Dict, List

from engine.game_session import GameSession
from engine.player import PlayerAction


class GameEngine:
    # TODO: This is an in memory session store. Have to be moved to a better mechanism
    sessionStore: Dict[str, GameSession]

    def __init__(self):
        self.sessionStore = {}

    def begin_session(self, player_ids: List[str]):
        session = GameSession(player_ids)
        self.sessionStore[session.session_id] = session
        return session.session_id

    def begin_new_game(self, session_id: str):
        self.sessionStore[session_id].start_game()

    def execute_player_action(self, session_id: str, player_id: str,
                              action_type: PlayerAction, action_data: Dict[str,str]):
        return self.sessionStore[session_id].player_action(player_id, action_type, action_data)


