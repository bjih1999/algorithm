import sys
from collections import deque

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(sys.stdin.readline().rstrip())

board = []
visited = []
answer = 0
result = []
for _ in range(n):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    visited.append([0 for _ in range(n)])

for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1
            answer += 1
            count = 1
            while queue:
                cur_i, cur_j = queue.popleft()

                for move in moves:
                    next_i, next_j = cur_i + move[0], cur_j + move[1]

                    if 0 <= next_i < n and 0 <= next_j < n and not visited[next_i][next_j] and board[next_i][next_j] == 1:
                        queue.append((next_i, next_j))
                        visited[next_i][next_j] = 1
                        count += 1
            
            result.append(count)

print(answer)
result = sorted(result)

for r in result:
    print(r)