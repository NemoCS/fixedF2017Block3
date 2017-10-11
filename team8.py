####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'T4T+random' # Only 10 chars displayed.
strategy_name = 'T4T but occasionally does opposite'
strategy_description = 'T4T but occasionally does opposite'
    
def move(my_history, their_history, my_score, their_score):
    import random

    #random.random() returns a decimal number from 0 and 1.
    #collude on the first turn 90% of the time
    if len(their_history)==0:
        #random.random() is less than 0.90 90% of the time.
        if random.random() < 0.90:
            return 'c'
        else:
            return 'b'
    elif their_history[-1] == 'b':
        #Betray 90% of the time after being betrayed
        if random.random() < 0.90:
            return 'b'
        #Collud 10% of the time after being betrayed
        else:
            return 'c'
    #When opponent colled last turn:
    else:
        #Collude 90% of the time after opponent colludes
        if random.random() < 0.90:
            return 'c'
        #Betray 10% of the time after opponent colludes
        else:
            return 'b'          
