team_name = 'Betray' # Only 10 chars displayed.
strategy_name = 'Always betrays'
strategy_description = 'Always betrays'
    
def move(my_history, their_history, my_score, their_score):
    #always betrays
    return 'b'