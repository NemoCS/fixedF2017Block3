####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Retal-b' # Only 10 chars displayed.
strategy_name = 'Greedy Retaliator'
strategy_description = 'Greedy Retaliator'
    
def move(my_history, their_history, my_score, their_score):
    #betray on the first turn
    if len(their_history)==0:
      return 'b'
    #betray if opponent successfully betrayed last turn
    #(this does not include cases when both players betrayed)
    elif their_history[-1] == 'b' and my_history[-1] == 'c':
      return 'b'
    #otherwise collude
    else:
      return 'c'