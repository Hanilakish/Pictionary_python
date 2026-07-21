"""
Handles a single game room: wires together Player, Board, chat and Round.
"""

class Board:
    WIDTH = HEIGHT = 720

    def __init__(self):
        self.actions = [] #an ordered list of dict

    def draw(self, x: int, y:int, color:tuple, size: int = 4)-> dict:
        """Record a single point/segment being drawn."""
        #tuple(color) is utilized as a safety net just in case the input is of type list.
        action = {"type": "draw", "x":x, "y":y, "color": tuple(color), "size":size}
        self.actions.append(action)
        return action

    def fill(self, x:int, y:int, color:tuple)->dict:
        """Record a flood-fill action."""
        action ={"type":"fill", "x":x, "y":y, "color":tuple(color)}
        self.actions.append(action)
        return action
    
    def clear(self)->None:
        """Clear the pallet."""
        self.actions = []

    def get_actions(self)-> list:
        """Send this to players which join mid match such that
        their canvas can be replayed to the current state."""
        return self.actions