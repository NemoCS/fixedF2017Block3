####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'HackSlash' # Only 10 chars displayed.
strategy_name = 'Handshake'
strategy_description = 'Handshake'
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history) == 0:
        return 'b'
    if len(their_history) == 1:
        return 'c'
    if their_history == my_history:
        return 'c' 
    else: 
        return 'b'
