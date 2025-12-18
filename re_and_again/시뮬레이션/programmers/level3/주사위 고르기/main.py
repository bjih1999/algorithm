'''
1. A와 B가 주사위를 절반씩 나눠 같은 경우를 combinations(range(n), n//2)로 구함
2. B가 주사위를 굴려서 나올 수 있는 눈의 경우의 수를 product(B_dice)를 통해 구함
3. B[i] = B가 주사위를 굴려서 i가 나오는 횟수. 주사위 눈은 최대 100이고, 한명이 가질 수 있는 주사위의 개수는 최대 5개이기 때문에, B 배열은 최대 크기는 501로 고정됨
4. B[i]를 재 정의하여 누적합으로 표현함. B[i]는 0~i까지의 나오는 눈의 경우의 수
5. A가 주사위를 굴려서 나올 수 있는 눈의 경우의 수를 product(A_dice)를 통해 구함
6. 5의 각 경우의 수에서 나올 수 있는 눈의 총합 total을 구함. B[total-1]을 모두 더함으로써 A가 특정 주사위를 가졌을 때, A가 B를 이기는 경우의 수를 구함
7. board 에 각 주사위를 구했을 때의 이기는 수를 저장함
8. board를 value의 오름차순으로 정렬하여 어떤 경우에 가장 이기는 경우의 수가 많은지를 알아냄
'''

from itertools import combinations, product

def solution(dice):
    n = len(dice)
    board = {}
    
    dice_candidates = combinations([i for i in range(n)], n//2)
    
    for candidates in dice_candidates:
        A_candidates = candidates
        B_candidates = []
        for i in range(n):
            if i not in A_candidates:
                B_candidates.append(i)
        
        B = [0] * (100 * n//2 + 1)
        B_dice = []
        for i in B_candidates:
            B_dice.append(dice[i])
        B_case = product(*B_dice)
        
        
        for B_c in B_case:
            total = sum(B_c)
            B[total] += 1
        
        for i in range(1, len(B)):
            B[i] = B[i-1] + B[i]
        
        A_dice = []
        for i in A_candidates:
            A_dice.append(dice[i])
        
        A_case = product(*A_dice)
        A_total = 0
        for A_c in A_case:
            total = sum(A_c)
            A_total += B[total-1]

        key = ' '.join(list(map(lambda x: str(x+1), A_candidates)))
        board[key] = A_total
    result = sorted(board.items(), key=lambda x: -1 * x[1])
    answer = sorted(list(map(int, result[0][0].split())))
    return answer


'''
2트째 좀 더 정돈된 풀이
'''
from itertools import combinations, product, accumulate

def solution(dice):
    n = len(dice)
    a_dice_picks = combinations(range(n), r=n//2)
    
    result = {}
    # a가 주사위를 고르는 경우의 수에 대해
    for a_dice_pick in a_dice_picks:
        # b가 나올 수 있는 눈의 합의 경우의 수와 그에 대한 출현 횟수를 구함.
        b_dice_pick = list(filter(lambda x: x not in a_dice_pick, range(n)))
        
        b_dices = [dice[i] for i in b_dice_pick]
        
        b_dice_cases = product(*b_dices)
        
        b_score = [0] * 501
        for b_dice_case in b_dice_cases:
            b_score[sum(b_dice_case)] += 1
        
        b_score = list(accumulate(b_score))

        # a가 나올 수 있는 눈의 합의 경우의 수를 구함
        a_dices = [dice[i] for i in a_dice_pick]
        a_dice_cases = product(*a_dices)
        

        # a가 나올 수 있는 눈의 합 보다 작은 b의 눈 출현 횟수를 구함
        a_wins = 0
        for a_dice_case in a_dice_cases:
            a_wins += b_score[sum(a_dice_case)-1]
        # a에서 나올 수 있는 모든 눈의 합에 대한 b의 눈 출현 횟수의 합을 모두 더해서 a가 주사위를 고르는 경우의 수를 키값으로 후보에 추가함.
        
        result[' '.join(list(map(str, sorted(a_dice_pick))))] = a_wins
        
    # 모든 후보에 대해 이기는 횟수를 정렬하여 가장 큰 경우의 수를 리턴함.
    result = sorted(result.items(), key = lambda x: (-1 * x[1], x[0]))
    return sorted(list(map(lambda x: int(x) + 1, result[0][0].split())))
    