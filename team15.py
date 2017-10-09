####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Forgiving' # Only 10 chars displayed.
strategy_name = 'T4T but occasionally forgives'
strategy_description = 'T4T but occasionally forgives'
    
def move(my_history, their_history, my_score, their_score):
    import random
    #collude on first turn
    if len(their_history)==0:
        return 'c'
    elif their_history[-1] == 'b':
        #Betray 90% of the time after being betrayed
        if random.random() < 0.90:
            return 'b'
        #Collude 10% of the time after being betrayed
        else:
            return 'c'
    #collude if opponent colluded last turn
    else:
        return 'c'