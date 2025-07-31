#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *


class AIPlayer(Player):
    "An AI player that'll evaluate moves intelligently"
        
    def __init__(self, checker, tiebreak, lookahead):
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        
        "returns a string representation of the AIPlayer object"
        return "Player " + self.checker + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"
    
    def max_score_column(self, scores):
        """returns the index of the column with higest score"""
        max_score = max(scores)
        max_pair = []
        
        for i in range(len(scores)):
            if scores[i] == max_score:
                max_pair += [i]
        
        if self.tiebreak == "LEFT":
            return max_pair[0]
        elif self.tiebreak == "RIGHT":
            return max_pair[-1]
        else:
            return random.choice(max_pair)
        
    def scores_for(self, b):
       """takes a Board object b and determines the called AIPlayer‘s scores for the columns in b"""
       
       scores = [50] * b.width
       
       for col in range(b.width):
           if b.can_add_to(col) == False:
               scores[col] = -1
           else:
               if self.checker == 'X':
                   opponent_checker = 'O'
               else:
                   opponent_checker = 'X'
               
               if b.is_win_for(self.checker):
                   scores[col] = 100
               elif b.is_win_for(opponent_checker):
                   scores[col] = 0
               elif self.lookahead == 0:
                   scores[col] = 50
               else:
                   b.add_checker(self.checker, col)
                   opponent = AIPlayer(opponent_checker, self.tiebreak, self.lookahead - 1)
                   opponent_scores = opponent.scores_for(b)
                   b.remove_checker(col)
                   
                   
                   if self.lookahead % 2 == 1:
                       scores[col] = max(opponent_scores)
                   else:
                       scores[col] = min(opponent_scores)
       return scores
   
    def next_move(self, b):
        """Returns the column of the AI's best move"""
        scores = self.scores_for(b)
        best_column = self.max_score_column(scores)
        b.add_checker(self.checker, best_column)
        self.moves += 1
        return best_column
   
    
   