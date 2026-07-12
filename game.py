"""
Handles operations related to the game and connections
between player,board, chat and round.
"""

class Game:

    def __init__(self, id, players):
        self.id = id
        self.players = []
        self.words_used = []
        self.round = None
        self.board = None

    def player_guess(self, player, guess):
        ...

    def player_disconnected(self, player):
        ...

    def skip(self):
        ...

    def round_ended(self):
        ...

    def update_board(self):
        ...