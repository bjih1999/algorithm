'''
문제)
n, m 행렬 grid가 주어지고, 정수 health가 주어짐.
0, 0부터 시작하여 n-1, m-1까지 도달해야하며, 상하좌우 1칸 씩 이동 가능.
grid[x][y]에는 정수 값이 있으며 해당 칸에 도달할 때 마다, health가 해당 값만큼 깎임.
주어진 health로 n-1, m-1까지 도달할 수 있는 지 확인

제약 조건)
1 <= n, m <= 50             -> 완전탐색 풀이 가능
grid[i][j] is either 0, 1



풀이)
1. BFS로 0, 0 부터 상하좌우 탐색.
2. visited[x][y] = n+m (최댓값) 으로 초기화.
3. visited[nx][ny] < visited[x][y] + grid[nx][y] 일 경우에만 방문함.
    방문한 nx, ny에 대해 visited[nx][ny] = visited[x][y] + grid[nx][y]를 하여,
    visited[x][y]를 해당 칸에 도달했을 때 최소한으로 지불해야할 health 값을 만듦
4. visited[-1][-1] < health 리턴

'''


from collections import deque

class Solution:
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])
        _max = m + n + 100
        visited = [[_max for _ in range(m)] for _ in range(n)]
        queue = deque()
        queue.append((0, 0))
        visited[0][0] = grid[0][0]

        while queue:
            x, y = queue.popleft()
            for dx, dy in self.moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] + visited[x][y] < visited[nx][ny]:
                    visited[nx][ny] = grid[nx][ny] + visited[x][y]
                    queue.append((nx, ny))

        return visited[-1][-1] < health

