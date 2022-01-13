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

    def get_guess(self):
        """Ask the user if they guess h or l

        Args:
            self (Director): An instance of Director.
            """
        h_or_l = input("Higher or Lower? [h/l]")


    def play_again(self):
        """Ask the user if they want to play again

        Args:
            self (Director): An instance of Director.
            """


        card = input("Want to play again? [y/n] ")
        self.is_playing = (card == "y")