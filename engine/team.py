from typing import List


class Team:

    def __init__(self):
        self.player_positions: List[int] = []
        self.session_score: int = 0
        self.active_game_score: int = 0

    def add_player_pos(self, pos: int):
        self.player_positions.append(pos)

    def get_player_positions(self):
        return self.player_positions

    def notify_game_score_change(self, player_pos, score: int):
        self.active_game_score += score

    def notify_game_score_reset(self):
        self.active_game_score = 0

    def notify_session_game_score(self, score):
        self.session_score += score
