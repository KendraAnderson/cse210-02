from game.card import Card
from game.director import Director
import random
import pytest



#    Director.card = Card()
#    Director.previous_card = 0
#    Director.current_card = 0
#    Director.is_playing = True
#    Director.total_score = 300
#    Director.guess = ""
 
    
def test_flip():
    "This test will make sure that the random number is withing the parameters set"
    cards_count = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    Card.value = random.randint(1, 13)
    assert cards_count.__contains__(Card.value)

def test_start_game():
    "This test is to see if the fucntions are run correctly"
     
    while Director == True:
        assert Director.do_flip() == True
        assert Director.get_guess() == True
        assert Director.do_update() == True
        assert Director.do_output() == True
        assert Director.is_playing == Director.play_again()

def test_do_flip():
    "This is test if to verify that the card displayed is correct"
    Director.card = Card()
    Director.previous_card = 0
    Director.current_card = 0

 
    if Director.previous_card == 0:
        assert Director.previous_card == Director.current_card

def test_get_guess():
    "This test is to make sure that first the guess input is displayed when different than wanted input and that input (moked at the moment) is correctly resived"

    Director.guess = ""
        
    assert Director.guess != "l"  
    assert Director.guess != "h"

    while (Director.guess != "l" and Director.guess != "h"):
        
        Director. guess = "l"
        assert Director.guess == "l"
        Director.guess = "h"
        assert Director.guess == "h"


       



pytest.main(["-v", "--tb=line", "-rN", __file__])