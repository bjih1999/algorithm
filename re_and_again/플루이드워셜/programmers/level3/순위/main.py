'''
플루이드-워셜 알고리즘을 사용하여 풀이함.

플루이드-워셜 알고리즘은 O(n^3)의 풀이로,
다익스트라와 같은 최단 경로 알고리즘이지만, 한 노드에서의 최단거리만 계산하는 다익스트라와 달리
모든 노드에 대해 최단 경로를 계산한다.

a->b를 계산할때, a->k->b와 비교하여 더 작은 값을 최단 거리로 취한다.
플루이드-워셜 알고리즘은 DP에 기반한 최단경로 알고리즘으로, 점화식은 board[i][j] = min(board[i][j], board[i][k] + board[k][j])이다.

a->b이면, a->k->b가 성립할 때, 모든 간선에 대한 최단 거리를 계산해야할 경우 플루이드-워셜 알고리즘을 사용할 수 있을것 같다.
'''

def solution(n, results):
    board = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for r in results:
        winner, loser = r
        board[winner][loser] = 1
        board[loser][winner] = -1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if board[i][k] == 1 and board[k][j] == 1:
                    board[i][j] = 1
                    board[k][i] = -1
                    board[j][k] = -1
                    board[j][i] = -1
    
    count = 0
    for b in board:
        if len(list(filter(lambda x: x!= 0, b))) == n-1:
            count += 1
    return count