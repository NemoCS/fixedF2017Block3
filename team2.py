# -*- coding: utf-8 -*-
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random
team_name = 'Ktspin' # Only 10 chars displayed.
strategy_name = 'random'
strategy_description = 'uses a random every turn'
    
def move(my_history, their_history, my_score, their_score):
    moves = ['c','b']
    if len(my_history) < 1:
        random.choice = moves
        return 'b'
    else:
        return 'c'