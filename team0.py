
team_name = "Team16"
strategy_name = "TBD"
strategy_description = "Switches"

import random
#my_history = ""

def move(my_history, their_history, my_score, their_score):
    if len(their_history)==0:
        return random.choice([ "c ", "b" ])
    elif their_history[-1] == ( "c", "b", "b"):
        return "c"
    elif their_history[-1] == ("c", "b", "b"):
        return "b"
    else:
        return "b"
        