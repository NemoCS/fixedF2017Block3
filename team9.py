####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '3Pattern' # Only 10 chars displayed.
strategy_name = 'Betrays every third round'
strategy_description = 'Betrays every third round'
    
def move(my_history, their_history, my_score, their_score):
    #Betray on first turn
    if len(my_history) == 0:
        return 'b'
    #Betray on every third turn
    #The % operator divides and gives the remainder
    #Every number divisible by 3 will have a remainder of 0
    #So every third turn will have length % 3 = 0
    elif len(my_history) % 3 == 0:
        return 'b'
    #collude on the other 2/3 of the turns
    else: 
        return 'c'