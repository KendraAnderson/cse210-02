import random


class Card:
    """A card with a number 1-13 on the back.

    The responsibility of card is to keep track of which numbered card
    is face up and calculate whether the players guess was correct. It then 
    gives them points for correct guesses or takes them away for incorrect guesses.

    Attributes:
        value(int): The number on the card currently facing up.    
    """
    def __init__(self, guess):
        """Contructs a new instance of Card.

        Args:
            self (Card): An instance of Card.        
        """
        self.value = 0
        self.points = 0
        self.guess = guess

    def flip(self, guess):
        """Generates a new random value and calculates the points for the card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
        self.guess = True if guess >= self.value else False if guess <= self.value else 0
        self.points = 100 if self.guess == True else -75 if self.guess == False else 0