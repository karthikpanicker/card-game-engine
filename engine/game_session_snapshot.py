from engine.game_session import *
from engine.game_round import GameRound
from engine.team import Team
from engine.game import Game
from engine.player import Player
from engine.game_factory import GameType
from pydealer import Card
from typing import List, Dict

# GameSessionSnapshot fetches a snapshot of the current state of the Game Session/Game/Round and this will be used
#       to represent the game at the front end.


class GameSessionManager:
    game_session1: GameSession

    @staticmethod
    def game_session_manager(session1: GameSession):
        game_session1 = session1
        game_session_snap = GameSessionSnapshot()

        y = game_session_snap.generate_snapshot(game_session1)
        return y


class GameSessionSnapshot:
    def __init__(self):
        self.session_id: str
        self.game_type:  GameType
        self.number_of_players: int
        self.player_pos_dict: Dict[int, Player] = {}
        self.active_round_player_cards: Dict[Player, List[Card]] = {}
        self.first_team: Team()
        self.second_team: Team()
        self.first_team_session_score: int
        self.second_team_session_score: int
        self.active_game: Game
        self.first_team_active_game_score: int
        self.second_team_active_game_score: int
        self.active_game_round: GameRound
        self.dealer_pos: int
        self.first_bidder_pos: int
        self.bid_history_dict: Dict[int, int] = {}
        self.current_bid_value: int
        self.current_trump_card_player: Player
        # self.player_cards: Dict[Player, Card] = {}
        self.player_card_map: Dict[Player, Card] = {}
        self.first_player: Player
        self.trump_shown: bool
        self.trump_card:  Card
        self.trump_lifted: bool
        self.trump_lift_player: Player

    def generate_snapshot(self, game_session: GameSession):
        self.session_id = game_session.session_id
        self.game_type = game_session.game_type
        self.active_game = game_session.active_game

        self.number_of_players = game_session.number_of_players
        self.player_pos_dict = game_session.player_pos_dict
        self.first_team = game_session.get_player_at_position(1).get_team()
        self.second_team = game_session.get_player_at_position(2).get_team()

        self.first_team_session_score = self.first_team.session_score
        self.second_team_session_score = self.second_team.session_score
        self.first_team_active_game_score = self.first_team.active_game_score
        self.second_team_active_game_score = self.second_team.active_game_score

        print("active_game       : ", self.active_game)
        print("session_id        : ", self.session_id)
        print("game_type         : ", self.game_type)
        print("number_of_players : ", self.number_of_players)
        print("player_pos_dict   : ", self.player_pos_dict)
        print("First Team Player Positions : ", self.first_team.get_player_positions())
        print("Second Team Player Positions : ", self.second_team.get_player_positions())
        print("First Team Session Score  : ", self.first_team_session_score)
        print("Second Team Session Score : ", self.second_team_session_score)
        print("First Team ActGame Score  : ", self.first_team_active_game_score)
        print("Second Team ActGame Score : ", self.second_team_active_game_score)

        if self.active_game is not None:
            self.dealer_pos = self.active_game.dealer_pos
            self.first_bidder_pos = self.active_game.first_bidder_pos
            self.bid_history_dict = self.active_game.bid_history_dict
            self.current_bid_value = self.active_game.get_current_bid_value()
            self.current_trump_card_player = self.active_game.get_trump_card_player()
            self.trump_shown = self.active_game.get_trump_shown()

            print("active_game       : ", self.active_game)
            print("dealer_pos        : ", self.dealer_pos)
            print("first_bidder_pos  : ", self.first_bidder_pos)
            print("bid_history_dict  : ", self.bid_history_dict)
            print("current_bid_value : ", self.current_bid_value)
            print("trump_card_player : ", self.current_trump_card_player)
            print("trump_shown       : ", self.trump_shown)

            self.active_game_round = self.active_game.get_active_round()

            # active_round_player_cards is the list of cards still available with each player
            for pos1, player in self.player_pos_dict.items():
                self.active_round_player_cards[player] = self.active_game.player_pos_dict[pos1].cards
                print("active_round_player_cards: Player , Cards : ", player, self.active_round_player_cards[player])

            if self.active_game_round is not None:
                # player_card_map contains the details of the card played by each player during a round.
                self.player_card_map = self.active_game_round.player_card_map
                self.first_player = self.active_game_round.first_player
                self.trump_card = self.active_game_round.trump_card
                self.trump_lifted = self.active_game_round.trump_lifted
                self.trump_lift_player = self.active_game_round.trump_lift_player

                print("active_game_round : ", self.active_game_round)
                print("player_card_map   : ", self.player_card_map)
                print("first_player      : ", self.first_player)
                print("trump_card        : ", self.trump_card)
                print("trump_lifted      : ", self.trump_lifted)
                print("trump_lift_player : ", self.trump_lift_player)

        return self




