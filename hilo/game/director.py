from game.card import Card

class Director:
    """
    comments
    
    """

    def __init__(self):
        """
        comments
        Constructs a new Director.
        Args:
            Self (Director): and instance of Director.
        
        """
        self.card = 0
        self.is_playing = True
        self.score = 0
        self.total_score = 0
        self.guess = ""

    def start_game(self):
        """
        comments
        
        """
    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
            """
        flip_card = input("Flip a card [y/n] ")
        self.is_playing = (flip_card == "y")