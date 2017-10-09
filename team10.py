####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Random' # Only 10 chars displayed.
strategy_name = 'Coin Flip'
strategy_description = 'Randomly chooses collude or betray'
    
def move(my_history, their_history, my_score, their_score):
    import random
    #choice takes a list as its input
    #the list of possible choices is ['c', 'b']
    return random.choice(['c','b'])