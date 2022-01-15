from game.card import Card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card: A Card instance.
        previous_card (int): the card flipped last round.
        current_card (int): the card flipped this round.
        is_playing (boolean): Whether or not the game is being played.
        guess (string): The score for one round of play.
        total_score (int): The score for the entire game.
    
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            Self (Director): and instance of Director.
        
        """
        self.card = Card()
        self.previous_card = 0
        self.current_card = 0
        self.is_playing = True
        self.total_score = 300
        self.guess = ""

    def start_game(self):
        """
        This method starts the game running. 
        It is called by the __main__ file. 
        It calls methods from the director class.

        Args:
            self (Director): an instance of Director.
        """
        
        while self.is_playing:
            self.do_flip()
            self.get_guess()
            self.do_update()
            self.do_output()
            self.is_playing = self.play_again()

    def do_flip(self):
        """Get the card to be guessed on.

        Args:
            self (Director): An instance of Director.
        
        """
        if self.previous_card == 0:
            self.card.flip()
            self.current_card = self.card.value
        
        self.previous_card = self.current_card

        print(f"The card is: {self.previous_card}")
    

    def get_guess(self):
        """Ask the user if they guess high or low.
        
        Args:
            self (Director): An instance of Director.
        """
        self.guess = ""
        
        while (self.guess != "l" and self.guess != "h"):
            self.guess = input("Higher or Lower? [h/l]")
        

    def do_update(self):
        """Update the card.

        Args: 
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        self.card.flip()
        self.current_card = self.card.value

        print(f"Next card was: {self.current_card}")

        
    def do_output(self):
        """Display the players score based on whether they guessed correctly.

        Args: 
            Self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        if ((self.guess == "h" and self.current_card > self.previous_card) or
        (self.guess == "l" and self.current_card < self.previous_card)):
            self.total_score += 100

        elif ((self.guess == "l" and self.current_card > self.previous_card) or
        (self.guess == "h" and self.current_card < self.previous_card)):
            self.total_score -= 75

        print(f"Your score is: {self.total_score}")
        
        if self.total_score <= 0:
            self.is_playing = False
            print("\nGame over. You ran out of points.")
    
 
    def play_again(self):
        """Ask the user if they want to play again.
        
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        answer = input("Want to play again? [y/n] ")
        
        if answer == "n":
            print("\nGame over. You chose to stop playing.")
            return False
        else:
            return True
