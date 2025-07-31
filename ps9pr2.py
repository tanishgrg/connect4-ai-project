#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    def __init__(self, checker):
        """ Initializes a Player object with a given checker ('X' or 'O') and sets num_moves to 0. """
        assert (checker == 'X' or checker == 'O')
        self.checker = checker  
        self.num_moves = 0  
    
    def __repr__(self):
        """ Returns a string representation of the Player object. """
        return "Player " + self.checker
    
    def opponent_checker(self):
        """ Returns the opponent's checker ('X' if the player's checker is 'O', and 'O' if the player's checker is 'X'). """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
  
    def next_move(self, b):
        """Prompts the user to enter a column for their next move on the board.
        Repeats the prompt until a valid column is entered.
        """
        x = True
        while x:
            column = input("Enter a column: ")
            column = int(column)

            if 0 <= column < b.width and b.can_add_to(column):
                x = False
                self.num_moves += 1
                return column
            else:
                print("Try again!")



    

