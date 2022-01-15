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

def do_update():
    "This test makes sure that the value of the card is correctly updated"
    if Director != True:
        return

    Director.card.flip()
    assert Director.current_card == Director.card.value



        
def test_do_output():
    "This test makes sure that the scores are given correctly"

    if Director != True:
        return
    Director.card = Card()
    Director.previous_card = 5
    Director.current_card = 8
    Director.is_playing = True
    Director.total_score = 300
    Director.guess = "h"
    if ((Director.guess == "h" and Director.current_card > Director.previous_card) or
    (Director.guess == "l" and Director.current_card < Director.previous_card)):
        assert Director.total_score == 400
    
    Director.card = Card()
    Director.previous_card = 7
    Director.current_card = 4
    Director.is_playing = True
    Director.total_score = 300
    Director.guess = "l"
    if ((Director.guess == "h" and Director.current_card > Director.previous_card) or
    (Director.guess == "l" and Director.current_card < Director.previous_card)):
        assert Director.total_score == 400
    
    Director.card = Card()
    Director.previous_card = 6
    Director.current_card = 9
    Director.is_playing = True
    Director.total_score = 300
    Director.guess = "l"
    if ((Director.guess == "l" and Director.current_card > Director.previous_card) or
    (Director.guess == "h" and Director.current_card < Director.previous_card)):
        assert Director.total_score == 228

    Director.card = Card()
    Director.previous_card = 9
    Director.current_card = 4
    Director.is_playing = True
    Director.total_score = 300
    Director.guess = "h"
    if ((Director.guess == "l" and Director.current_card > Director.previous_card) or
    (Director.guess == "h" and Director.current_card < Director.previous_card)):
        assert Director.total_score == 228
    
    Director.total_score = 0
 
    if Director.total_score <= 0:
        assert Director.is_playing == False
        
    
 
def test_play_again():
    "This test helps make sure the message input is displayed, also that the answer to the input gives the desired outcome"
    if Director != True:
        return
    answer = input("Want to play again? [y/n] ")
    assert answer == "Want to play again? [y/n] "

    answer = "n"
        
    if answer == "n":
        assert False
    
    answer ="y"
    if answer == "y":
        return True


pytest.main(["-v", "--tb=line", "-rN", __file__])