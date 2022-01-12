import random


class Card:
    """A card with a number 1-13 on the back.

    The responsibility of card is to keep track of which numbered card
    is face up and calculate whether the players guess was correct. It then 
    gives them points for correct guesses or takes them away for incorrect guesses.

    Attributes:
        value(int): The number on the card currently facing up.    
    """
    def __init__(self):
        """Contructs a new instance of Card.

        Args:
            self (Card): An instance of Card.        
        """
        self.value = 0
        self.guessRight = True

    def flip(self):
        """
        comment here
        
        """