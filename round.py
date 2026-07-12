"""
Represents a round of the game, storing things like word, time, skips, drawing player and more
"""

from player import Player
import time as t
from _thread import *
from game import Game
from chat import Chat

class Round:
    def __init__(self, word: str, player_drawing: Player, players: list)-> None:
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.player_scores = {player:0 for player in players}
        self.time = t.time()
        start_new_thread(self.time_thread, ())

    def time_thread(self)-> None:
        """ Runs in thread to keep track of time."""
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time is up.")
             

    def guess(self, player: Player, wrd: str) -> bool:
        """Returns true if player guesses it right."""
        correct = wrd == self.word
        if correct:
            #implement scoring system here
            self.player_guessed[player]
        return correct

    
    def player_left(self, player: Player)-> None:
        """Removes the player that left from scores and list."""

        if player in self.player_scores:
            del self.player_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)

        if player == self.player_drawing:
            self.end_round("Drawing player leaves")

    def end_round(self, player: Player, masg: str)-> None:
        """This func is used to end the round."""
        pass
    
