def solution(survey, choices):
    answer = ''
    board = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for index, choice in enumerate(choices):
        left = survey[index][0]
        right = survey[index][1]
        
        if choice < 4:
            board[left] += (4 - choice)
        elif choice > 4:
            board[right] += (choice - 4)
        
    if board['T'] > board['R']:
        answer += 'T'
    else:
        answer += 'R'
        
    if board['F'] > board['C']:
        answer += 'F'
    else:
        answer += 'C'
        
    if board['M'] > board['J']:
        answer += 'M'
    else:
        answer += 'J'
        
    if board['N'] > board['A']:
        answer += 'N'
    else:
        answer += 'A'

    return answer