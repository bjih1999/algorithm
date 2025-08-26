'''
기초 BFS
'''

from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        queue = deque()
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        answer = 0

        for x in range(n):
            for y in range(m):
                if not visited[x][y] and grid[x][y] == '1':
                    queue.append((x, y))
                    visited[x][y] = True

                    while queue:
                        i, j = queue.popleft()

                        for dx, dy in moves:
                            nx, ny = i + dx, j + dy
                            
                            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '1':
                                visited[nx][ny] = True
                                queue.append((nx, ny))

                    answer += 1
        return answer

        
