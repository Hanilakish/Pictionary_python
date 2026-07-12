"""
Handles operations related to the game and connections
between player,board, chat and round.
"""

from player import Player
from board import Board
from round import Round

class Game:

    def __init__(self, id: int, players: Player,thread):
        """init the game! once player threshold is met"""
        self.id = id
        self.players = players
        self.words_used = []
        self.round = Round(self.get_word())
        self.board = None
        self.player_draw_index = 0
        self.connected_thread = thread
        self.start_new_round()
        self.create_board()

    def start_new_round(self)-> None:
        """Starts a new round with a new word."""
        self.round = Round(self.get_word(), self.players[self.player_draw_index])
        self.player_draw_index += 1

        if self.player_draw_index >= len(self.players):
            self.round_ended()
            self.end_game()

    def create_board(self):
        self.board = Board()

    def player_guess(self, player: Player, guess: str)-> bool:
        """Makes the player guess the word"""
        ...

    def player_disconnected(self, player)-> Exception:
        """Call to to clean up objects when disconnected"""
        ...

    def skip(self)-> None:
        """Increments the skips round. If Skip '>' threshold starts a new round."""
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended() 
        else:
            raise Exception("No round started yet") 

    def round_ended(self) -> None:
        """If round ends call this"""
        self.start_new_round()
        self.create_board()

    def update_board(self, x:int, y:int, color:list[int])->None:
        """calls update method on board"""
        if self.board:
            raise Exception("No board created.")
        self.board.update(x,y,color)

    def end_game(self):
        ...

    def get_word(self)->str:
        """Gives a word which is not yet used."""
        # get a list of words from somewhere
        ...
