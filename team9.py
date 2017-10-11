#team - Griffin,Thomas

team_name = "Random65"
strategy_name = 'Betray 65 percent'
strategy_description = 'Betray 65 percent of the time'

def move(my_history,their_history,my_score,their_score):
    import random
    if not their_history:
        return 'c'
    else:
        return random.choice(['b','b','b','c','c'])