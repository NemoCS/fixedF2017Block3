####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Example8'
strategy_name = 'Betray 50 times then collude'
strategy_description = 'Do dumb stuff'
def move(my_history, their_history, my_score, their_score):
    if len(my_history) < 50:
        return 'b'
    else:
        return 'c'