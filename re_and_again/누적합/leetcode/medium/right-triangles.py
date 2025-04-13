'''
0과 1로 이루어진 n * m 배열 중 1인 원소들의 위치로 만들 수 있는 직각 삼각형의 개수를 구하는 문제 
ex)
1 1 0 0
0 1 0 1
1 0 0 0
=> 2개

0 < n,m <= 1000

풀이)
누적합 풀이.

1) 각 행과 열 별로 1의 개수의 누적합을 구함
row_count = [2, 2, 1], col_count = [2, 2, 0, 1]

2) 배열을 순회하며 값이 1인 경우를 찾음. 이 경우는 이 값을 중심으로 삼각형이 만들어지는 경우를 의미함.
grid[i][j]로 직각 삼각형이 만들어지는 경우의 수는 아래와 같이 정의할 수 있음
(row_count[i] - 1) * (col_count[j] - 1) => 같은 row의 1의 개수(본인 제외) * 같은 col의 1의 개수(본인 제외)

3) 위 경우의 수를 모두 더한 값이 답이 됨
'''

class Solution(object):
    def numberOfRightTriangles(self, grid):
        
        n = len(grid)
        m = len(grid[0])

        if n < 2 or m < 2:
            return 0
        col_count = [0] * m
        row_count = [0] * n

        for i in range(n):
            for j in range(m):
                col_count[j] += grid[i][j]
                row_count[i] += grid[i][j]

        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    answer += (row_count[i] - 1) * (col_count[j] - 1)


        return answer