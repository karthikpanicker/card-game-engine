from engine.game_session import *
from engine.game_round import GameRound
from engine.team import Team
from engine.game import Game
from engine.player import Player
from engine.game_factory import GameType

from pydealer import Card

# GameSessionSnapshot fetches a snapshot of the current state of the Game Session/Game/Gameround and this will be used
#       to represent the game at the front end.

class GameSessionSnapshot:
    session_id: str
    game_type:  GameType
    number_of_players: int
    player_pos_dict: Dict[int, Player] = {}
    # active_round_player_cards: Dict[Player, List[Card]] = {}
    first_team: Team()
    second_team: Team()
    # session_state: GameSessionState
    first_team_session_score: int
    second_team_session_score: int
    active_game: Game
    first_team_active_game_score: int
    second_team_active_game_score: int
    active_game_round: GameRound
    dealer_pos: int
    first_bidder_pos: int
    bid_history_dict: Dict[int, int] = {}
    current_bid_value: int
    current_trump_card_player: Player
    player_cards: Dict[Player, Card] = {}
    player_card_map: Dict[Player, Card] = {}
    first_player: Player
    trump_shown: bool
    trump_card:  Card
    trump_lifted: bool
    trump_lift_player: Player

    @staticmethod
    def generate_snapshot(GameSession):
        session_id = GameSession.session_id
        game_type = GameSession.game_type
        number_of_players = GameSession.number_of_players
        player_pos_dict = GameSession.player_pos_dict

        first_team = GameSession.get_player_at_position(1).get_team()
        second_team = GameSession.get_player_at_position(2).get_team()

        first_team_session_score = first_team.session_score
        second_team_session_score = second_team.session_score

        # second_team = GameSession.player_pos_dict[2].get_team()
        # session_state = GameSession.session_state
        active_game = GameSession.active_game
        first_team_active_game_score = first_team.active_game_score
        second_team_active_game_score = second_team.active_game_score

        print("active_game       : ", active_game)
        print("session_id        : ", session_id)
        print("game_type         : ", game_type)
        print("number_of_players : ", number_of_players)
        print("player_pos_dict   : ", player_pos_dict)

        if active_game is not None:
            dealer_pos = active_game.dealer_pos
            first_bidder_pos = active_game.first_bidder_pos
            bid_history_dict = active_game.bid_history_dict
            current_bid_value = GameSession.active_game.get_current_bid_value()
            current_trump_card_player = GameSession.active_game.get_trump_card_player()
            trump_shown = active_game.get_trump_shown()

            print("dealer_pos        : ", dealer_pos)
            print("first_bidder_pos  : ", first_bidder_pos)
            print("bid_history_dict  : ", bid_history_dict)
            print("current_bid_value : ", current_bid_value)
            print("trump_card_player : ", current_trump_card_player)
            print("trump_shown       : ", trump_shown)

            active_game_round = active_game.get_active_round()
            if active_game_round is not None:
                # active_round_player_cards is the list of cards still available with each player
                for pos1, player in player_pos_dict.items():
                    print("Pos and Cards : ", pos1, player)
                    # active_round_player_cards[player] = player.cards

                # player_card_map contains the details of the card played by each player during a round.
                player_card_map = active_game_round.player_card_map
                first_player = active_game_round.first_player
                trump_card = active_game_round.trump_card
                trump_lifted = active_game_round.trump_lifted
                trump_lift_player = active_game_round.trump_lift_player

                print("player_card_map   : ", player_card_map)
                print("first_player      : ", first_player)
                print("trump_card        : ", trump_card)
                print("trump_lifted      : ", trump_lifted)
                print("trump_lift_player : ", trump_lift_player)


        return GameSessionSnapshot




