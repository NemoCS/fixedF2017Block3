team_name = 'Frenchie'
strategy_name = 'Cool stuff.'
strategy_description = 'Looks at history and uses random.'
    
def move(my_history, their_history, my_score, their_score):
    import random
    
    if len(their_history) == 0:
        return 'c'
    
    elif len(their_history) == 1:
        return 'c'
    
    elif len(their_history) >= 2:
        if their_history[-2:] == 'bb':
            return 'b'
        elif their_history[-3:] == 'bcb':
            return 'b'
        elif random.uniform(0,5) >= 1:
            return 'b'
        else:
            return 'c'
    else:
        return 'c'