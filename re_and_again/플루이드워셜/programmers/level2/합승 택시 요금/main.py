from collections import deque
import heapq
MAX_COST = 999999


'''
다익스트라로 풀었던 합승 택시 요금 문제를 플루이드-워셜 알고리즘으로 다시 풀어봄.

3 <= n <= 200이라 O(n^3)인 플루이드 워셜 풀이가 가능했음
점화식: min_cost = min(min_cost, board[s][k] + board[k][a] + board[k][b]) 으로 깔끔하게 구현 가능했다.

'''
def solution(n, s, a, b, fares):
    global MAX_COST
    
    board = [[MAX_COST for _ in range(n+1)] for _ in range(n+1)]
    
    for c, d, cost in fares:
        board[c][d] = cost
        board[d][c] = cost
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    board[i][j] = 0
                if board[i][k] + board[k][j] < board[i][j]:
                    board[i][j] = board[i][k] + board[k][j]
    
    min_cost = board[s][a] + board[s][b]
    
    for k in range(1, n+1):
        min_cost = min(min_cost, board[s][k] + board[k][a] + board[k][b])
        
    return min_cost
