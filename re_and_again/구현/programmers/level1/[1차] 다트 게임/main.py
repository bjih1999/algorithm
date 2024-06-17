import re

option_board = {
    'S': 1,
    'D': 2,
    'T': 3,
}

prize_board = {
    '*': 2,
    '#': -1,
}

def solution(dartResult):
    global bonus
    
    answer = 0
    pattern = r'(\d{1,2})([SDT]{1})([\*\#]?)'
    dart_list = list(re.findall(pattern, dartResult))
    score_board = [0 for _ in range(3)]
    
    for index, dart in enumerate(dart_list):
        score = int(dart[0])
        option = dart[1]
        score_board[index] = score ** option_board[option]
        
        if dart[2] != '':
            prize = prize_board[dart[2]]
            score_board[index] *= prize
            
            if index > 0 and dart[2] == '*':
                score_board[index-1] *= prize
        
    return sum(score_board)