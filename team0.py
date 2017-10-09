####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Collude' # Only 10 chars displayed.
strategy_name = 'Always Colludes'
strategy_description = 'Always Colludes'
    
def move(my_history, their_history, my_score, their_score):
    #always collude
    return 'c'