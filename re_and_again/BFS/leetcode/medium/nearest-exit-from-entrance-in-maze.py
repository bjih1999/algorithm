'''
BFS
n * m 길이의 미로를 탐색.
가장 자리 중 벽이 아닌 곳이 출구
입구를 제외한 출구 중 가장 가까운 출구의 길이를 구하기

O(n*m) = O(100 * 100)

https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/?envType=study-plan-v2&envId=leetcode-75
'''

from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        n = len(maze)
        m = len(maze[0])
        entrance_x, entrance_y = entrance

        dist = [[-1] * m for _ in range(n)]
        queue = deque()

        queue.append((entrance_x, entrance_y))
        dist[entrance_x][entrance_y] = 0

        while queue:
            x, y = queue.popleft()

            for dx, dy in moves:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and maze[nx][ny] == '.':
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

        has_exit = False
        answer = n*m + 100
        
        for i in range(n):
            for j in range(m):
                if maze[i][j] == '+':
                    continue
                
                if 1 <= i <= n-2 and 1 <= j <= m-2:
                    continue
                
                if i == entrance_x and j == entrance_y:
                    continue

                if dist[i][j] == -1:
                    continue

                has_exit = True
                answer = min(answer, dist[i][j])
        if not has_exit:
            return -1
        
        return answer
        