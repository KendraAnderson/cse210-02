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
        This method handles the settings to start the game running. 
        It´s called by the __main__ file. 
        It calls card class and its methods.
        """
        
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.get_outputs()
            
            #here comes a play_again method() or
        #a print("play_again") maybe
            
            

