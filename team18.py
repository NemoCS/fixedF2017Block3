####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Opposite' # Only 10 chars displayed.
strategy_name = 'Opposite of T4T'
strategy_description = 'Opposite of T4T'
    
def move(my_history, their_history, my_score, their_score):
    #collude on the first turn
    if len(their_history)==0:
      return 'c'
    #betray if opponent colluded last turn
    elif their_history[-1] == 'c':
      return 'b'
    #collude if opponent betrayed last turn
    else:
      return 'c'