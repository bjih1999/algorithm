import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
adj = [[] for _ in range(n+1)]
score_board = [0 for _ in range(n+1)]

while True:
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    if a == -1 and b == -1:
        break

    adj[a].append(b)
    adj[b].append(a)


for i in range(1, n+1):

    visited = [False for _ in range(n+1)]
    visited[i] = True
    visited_count = 1
    queue = deque()
    queue.append((i, 0))
    if len(adj[i]) == n -1:
        score_board[i] = 1
    else:
        while queue:
            friend, depth = queue.popleft()

            for next_friend in adj[friend]:
                if visited[next_friend]:
                    continue

                visited[next_friend] = True
                visited_count += 1
                if visited_count == n:
                    score_board[i] = depth+1
                queue.append((next_friend, depth+1))

min_point = min(score_board[1:])
candidate_count = score_board.count(min_point)
candidate = map(lambda x:x[0], filter(lambda x: x[1] == min_point, list(enumerate(score_board))))

print(str(min_point) + ' ' + str(candidate_count))
print(' '.join(list(map(str, candidate))))