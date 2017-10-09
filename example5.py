####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Example5'
strategy_name = 'Be dumb'
strategy_description = 'Be dumb'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'c'
    else:
        return 'b'