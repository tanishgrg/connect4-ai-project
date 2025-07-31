#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        

def process_move(p,b):
    "processes a move for the player p on teh board b"
    print(str(p) + "'s turn")
    
    b.add_checker(p.checker, p.next_move(b))
    
    print()
    print(b)
    
    if b.is_win_for(p.checker):
        print(str(p) + " wins in " + str(p.num_moves) + " moves.")
        print("Congratulations!")
        return True
    elif b.is_full():
        print("It's a tie!")
        return True
    return False


class RandomPlayer(Player):
    "Subclass of Player, an unitelligent player that moves randomly"
    def next_move(self, b):
        
        columns = []
        for col in range(b.width):
            if b.can_add_to(col):
                columns += [col]
        
        result = random.choice(columns)
        self.num_moves += 1
        return result
        
    
    
    
