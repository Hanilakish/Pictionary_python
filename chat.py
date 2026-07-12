"""
Represents and stores information about the chat
"""
from round import Round

class Chat:
    def __init__(self, r):
        self.content = []
        self.round = r

    def update_chat(self, msg):
        self.content.append(msg)

    def get_chat(self):
        return self.content
    
    # dunder method for length of content
    def __len__(self):
        return len(self.content)
    
    # dunder method for string representation
    def __str__(self):
        return "".join(self.content)
    
    #dunder method for rep mainly for developers
    def __repr__(self):
        return str(self)