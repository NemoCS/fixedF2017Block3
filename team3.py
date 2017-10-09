####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Tit4Tat-b' # Only 10 chars displayed.
strategy_name = 'Greedy Tit for Tat'
strategy_description = 'Greedy Tit for Tat'
    
def move(my_history, their_history, my_score, their_score):
    #betray on the first turn
    if len(their_history)==0:
      return 'b'
    #betray if opponent betrayed last turn
    elif their_history[-1] == 'b':
      return 'b'
    #collude if opponent colluded last turn
    else:
      return 'c'