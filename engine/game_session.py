import uuid
from enum import Enum
from typing import List, Dict

from engine.game import Game
from engine.game_engine_exception import GameEngineException
from engine.game_factory import GameFactory, GameType
from engine.player import Player, PlayerAction
from engine.team import Team


class GameSessionState(Enum):
    SESSION_CREATED = 1
    GAME_STARTED = 2


class GameSession:
    """

    A game session would involve a set of players playing multiple games.
    ...

     Methods
    -------
    distribute_player_to_teams()
        links the player to a team. Teams teams considered in the current engine implementation
    """
    session_id: str
    players: List[Player]
    game_type: GameType
    number_of_players: int
    player_pos_dict: Dict[int, Player]
    active_game: Game

    def __init__(self, player_ids: List[str] =[], game_type=GameType.TWENTY_EIGHT, number_of_players=4):
        self.session_id = self.__generateSession()
        self.game_type = game_type
        self.number_of_players = number_of_players
        self.session_state: GameSessionState = GameSessionState.SESSION_CREATED
        self.player_pos_dict: Dict[int,Player] = {}
        self.active_game: Game = None
        self.__allocate_seats(player_ids)

    @staticmethod
    def __generateSession():
        return str(uuid.uuid1())

    def get_session_id(self):
        return self.session_id

    def __allocate_seats(self, player_ids):
        for pos in range (1,self.number_of_players + 1):
            if pos < len(player_ids) + 1:
                player = Player(player_ids[pos -1], pos)
                self.player_pos_dict[pos] = player
            else:
                break
        return self.player_pos_dict

    def get_seat_allocations(self):
        return self.player_pos_dict

    def add_player_to_session(self, player_id):
        for pos in range(1, self.number_of_players + 1):
            if pos not in self.player_pos_dict:
                player = Player(player_id, pos)
                self.player_pos_dict[pos] = player
                return self.player_pos_dict
        raise GameEngineException("No free position available for allocation")

    def change_player_pos(self, new_position , player_id):
        if self.session_state is not GameSessionState.SESSION_CREATED:
            raise GameEngineException("Cannot change player position after starting the game")
        if new_position > self.number_of_players:
            raise GameEngineException(str.format("Position invalid for maximum number of {} players"
                                                 , self.number_of_players))
        current_position, player = self.get_player_position_and_details(player_id)
        if current_position is None:
            raise GameEngineException("Player not part of this game session")
        player_in_new_pos = self.player_pos_dict[new_position] if new_position in self.player_pos_dict.keys() else None
        self.player_pos_dict[new_position] = player
        self.player_pos_dict[current_position] = player_in_new_pos
        return self.player_pos_dict

    def get_player_position_and_details(self, player_id):
        for key, value in self.player_pos_dict.items():
            if value is not None and player_id == value.player_id:
                return key, value
        return None, None

    def get_player_at_position(self, position):
        return self.player_pos_dict[position]

    def can_start_game(self):
        return self.number_of_players == len(self.player_pos_dict)

    def start_game(self):
        self.session_state = GameSessionState.GAME_STARTED
        self.distribute_player_to_teams()
        self.active_game = GameFactory.get_game_implementation(
            self.game_type, self.player_pos_dict, self.active_game)

    def player_action(self, player_id: str, action_type: PlayerAction, action_data):
        return self.active_game.player_action(player_id, action_type, action_data)

    def distribute_player_to_teams(self):
        first_team = Team()
        second_team = Team()
        for pos, player in self.player_pos_dict.items():
            if pos % 2 == 1:
                player.set_team(first_team)
                first_team.add_player_pos(pos)
            else:
                player.set_team(second_team)
                second_team.add_player_pos(pos)



