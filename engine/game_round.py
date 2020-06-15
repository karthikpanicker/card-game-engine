from typing import Dict, Optional

from pydealer import Card
from engine.player import Player

# Game round represents a game play involving one card from each player. The cards played in the round will be used
# to determine who wins the round.


class GameRound:

    player_card_map: Dict[Player, Card]
    high_card: Optional[Card]
    trump_card: Card
    player: Player
    round_winner: Player
    trump_lifted: bool

    #    player_card_map --> Maps the card played by each player for the round
    #   high_card       --> A temporary variable used to store the higher value card while iterating the round
    #    round_winner    --> Denotes the player who won the particular round
    #    trump_lifted    --> Is a boolean used to specify when exactly the Trump was lifted in the round.
    #                        This will be used to determine if a trump card was used/passed in a Round.
    #                        Will be implemented
    #                        once the details of the trump lifting logic are confirmed

    def __init__(self, first_player: Player):
        self.player_card_map = {}
        self.first_player = first_player
        self.high_card = None
        self.points = 0
        self.trump_lifted = False
        self.card_ranks_28 = {
                "Jack": 13,
                "9": 12,
                "Ace": 11,
                "10": 10,
                "King": 9,
                "Queen": 8,
                "8": 7,
                "7": 6,
                "6": 5,
                "5": 4,
                "4": 3,
                "3": 2,
                "2": 1

        }

    # Adds the Player and Card Played details to a list

    def add_player_card(self, player: Player, card: Card):
        self.player_card_map[player] = card

    def get_card_count(self):
        return len(self.player_card_map)

    def get_first_card(self):
        return list(self.player_card_map.values())[0]

    # Summarize is called once all 4 players play their cards. This will determine the points for the round  and who the
    # round winner is.

    def summarize(self, trump_card):
        # If the trump card has not been lifted, the highest value of the leading suit wins the round.
        if trump_card is None:
            for player in self.player_card_map:
                if self.high_card is None:
                    self.high_card = self.player_card_map[player]
                else:
                    self.high_card = self.compare_cards_no_trump(self.player_card_map[player])
                    self.points += self.fetch_card_point(self.player_card_map[player])
        else:
            # If the trump card has been lifted, the highest value of the leading suit wins the round provided
            # a trump has not been used in that round
            for player in self.player_card_map:
                if self.high_card is None:
                    self.high_card = self.player_card_map[player]
                else:
                    self.high_card = self.compare_cards_trump(self.player_card_map[player])
                    self.points += self.fetch_card_point(self.player_card_map[player])
        # Below code to decide the round winner based on who has played the high card
        for player in self.player_card_map:
            if self.player_card_map[player].abbrev == self.high_card.abbrev:
                round_winner = player
                return round_winner

    # Accumulates points for the round and these points will be used to decide if the bidder has won the bid

    @staticmethod
    def fetch_card_point(card):
        if card.value == 'Jack':
            return 3
        elif card.value == '9':
            return 2
        elif card.value == '10' or card.value == 'Ace':
            return 1
        else:
            return 0

    # Logic to compare 2 cards and find the higher value one if the trump card has not been lifted

    def compare_cards_no_trump(self, card: Card):
        if self.high_card.suit == card.suit:
            # card_ranks_28 has the list of cards ranked on their values and that is used to decide the high card.
            if self.card_ranks_28[self.high_card.value] > self.card_ranks_28[card.value]:
                return self.high_card
            else:
                return card
        else:
            return self.high_card

    # Logic to compare 2 cards and find the higher value one if the trump card has been lifted

    def compare_cards_trump(self, card: Card):
        if self.high_card.suit == card.suit:
            if self.card_ranks_28[self.high_card.value] > self.card_ranks_28[card.value]:
                return self.high_card
            else:
                return card
        elif card.suit == self.trump_card.suit:
            return card
        else:
            return self.high_card


