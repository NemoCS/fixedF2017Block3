#TEAM 1
#Greg Hall and Lucas Huffman
team_name = 'Swhallo'
strategy_name = 'Rebuttle'
strategy_description = 'Collude unless betrayed then betray back'
    
def move(my_history, their_history, my_score, their_score):    
    if len(my_history) < 1:
        return 'c'
    if their_history[-1] == 'b':
        return 'b'
    else:
        return 'c'
       
#def move(my_history, their_history, my_score, their_score):
#    if 'b' in their_history:
#        return 'b'
#    else:
#        return 'c'