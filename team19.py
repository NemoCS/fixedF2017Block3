####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'GoPsycho' # Only 10 chars displayed.
strategy_name = 'Be nice at first, then always betray'
strategy_description = 'Be nice at first, then always betray'
    
def move(my_history, their_history, my_score, their_score):
    #always collude if it is before turn 100
    if len(my_history) < 80:
        return 'c'
    #always betray starting at turn 80
    else:
    	return 'b'