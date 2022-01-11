from game.card import Card

class Director:
    """
    comments
    
    """

    def __init__(self):
        """
        Constructs a new Director.

        Args:
            Self (Director): and instance of Director.
        
        """
        self.card = ""
        self.is_playing = True
        self.score = 0
        self.total_score = 0

    
    def start_game(self):
        """
        comments
        
        """