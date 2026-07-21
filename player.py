"""
Represents a player on the server side, holds identity and per game score.
"""

import uuid

class Player:
    def __init__(self, sid: str, name: str):
        self.id = str(uuid.uuid4())
        self.sid = sid
        self.name = name
        self.score = 0
        self.connected = True

    def add_score(self, points: int)-> None:
        self.score += points

    def reset_score(self)->None:
        self.score = 0

    def disconnect(self)->None:
        self.connected = False

    def to_dict(self) -> dict:
        """Serializable list of all participants to the client"""
        return {
            "id": self.id,
            "name": self.name,
            "score": self.score,
            "connected": self.connected,
        }
    
    def __eq__(self, other)-> bool:
        return isinstance(other, Player) and self.id == other.id

    def __hash__(self):
        return hash(self.id) 
    
    def __repr__(self):
        return f"Player({self.name!r}, score={self.score})"
