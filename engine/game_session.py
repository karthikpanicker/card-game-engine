"""
A game session would involve a set of players playing multiple games.
"""
import uuid
from enum import Enum
from typing import List, Dict

from engine.game_engine_exception import GameEngineException
from engine.player import Player


class GameType(Enum):
    TWENTY_EIGHT = 28
    FIFTY_SIX = 56

class GameSessionState(Enum):
    SESSION_CREATED = 1
    GAME_STARTED = 2


class GameSession:
    session_id: str
    players: List[Player]
    game_type: GameType
    number_of_players: int
    player_pos_dict: Dict[int,Player] = {}

    def __init__(self, player_ids: List[str] =[], game_type=GameType.TWENTY_EIGHT, number_of_players=4):
        self.session_id = self.generateSession()
        self.game_type = game_type
        self.number_of_players = number_of_players
        self.session_state: GameSessionState = GameSessionState.SESSION_CREATED
        self.allocate_seats(player_ids)

    @staticmethod
    def generateSession():
        return str(uuid.uuid1())

    def allocate_seats(self, player_ids):
        for pos in range (1,self.number_of_players):
            if pos < player_ids.len + 1:
                player = Player(player_ids[pos -1], pos)
                self.player_pos_dict[pos] = player
            else:
                break
        return self.player_pos_dict;

    def add_player_to_session(self, player_id):
        for pos in range(1, self.number_of_players):
            if pos not in self.player_pos_dict:
                player = Player(player_id, pos)
                self.player_pos_dict[pos] = player
                return self.player_pos_dict
        raise GameEngineException("No free position available for allocation")

    def change_player_pos(self, new_position ,player_id):
        if self.session_state is not GameSessionState.SESSION_CREATED:
            raise GameEngineException("Cannot change player position after starting the game")

    def get_player_position(self, player_id):
            

    def can_start_game(self):
        return self.number_of_players == len(self.player_pos_dict)


