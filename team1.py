#TEAM 1
#Greg Hall and Lucas Huffman
team_name = 'Swhallo'
strategy_name = "return 'b' 7/10 of time"
strategy_description = "Return 'c' at 0, 5, and multiples of 5"
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'c'
    if len(my_history)%5 == 0:
        return 'c'
    else:
        return 'b'
    