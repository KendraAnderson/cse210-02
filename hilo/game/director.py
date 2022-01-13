from game.card import Card

class Director:
    """
    comments
    
    """

    def __init__(self):
        """
        comments
        
        """

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