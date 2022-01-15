import random


class Card:
    """A card with a number 1-13 on the back.

    The responsibility of card is to keep track of which number
    is face up on the card.

    Attributes:
        value (int): The number on the card currently facing up.    
    """
    def __init__(self):
        """Contructs a new instance of Card.
        
        Args:
            self (Card): An instance of Card.        
        """
        self.value = 0

    def flip(self):
        """Generates a new random value for the card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
