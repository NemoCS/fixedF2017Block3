####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'SneakyT4T' # Only 10 chars displayed.
strategy_name = 'T4T but occasionally betrays randomly'
strategy_description = 'T4T but occasionally betrays randomly'
    
def move(my_history, their_history, my_score, their_score):
    import random
    if len(their_history)==0:
        return 'c'
    elif their_history[-1] == 'b':
        return 'b'
    else:
        #Collude 90% of the time after opponent colludes
        if random.random() < 0.90:
            return 'c'
        #Betray 10% of the time after opponent colludes
        else:
            return 'b'          
