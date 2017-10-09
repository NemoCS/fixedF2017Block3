####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'FailSwch-c' # Only 10 chars displayed.
strategy_name = 'Switch strategies if last turn failed (c)'
strategy_description = 'Switch after being suckered or double betray'
    
def move(my_history, their_history, my_score, their_score):
    #collude in first turn
    if len(their_history) == 0:
        return 'c'
    #switch to betray if successfully suckered last turn
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b'
    #switch to collude if both players betrayed last turn
    elif my_history[-1]=='b' and their_history[-1]=='b':
        return 'c'
    #Stay with collude if both players colluded last turn
    elif my_history[-1]=='c' and their_history[-1]=='c':
        return 'c'
    #Stay with betray if betray was successful last turn
    elif my_history[-1]=='b' and their_history[-1]=='c':
        return 'b'