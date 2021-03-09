'''
Z
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	512 MB	27256	8846	6547	37.262%

문제
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.



만약, N > 1이 라서 왼쪽 위에 있는 칸이 하나가 아니라면, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 22 × 22 크기의 배열을 방문한 순서이다.



N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음은 N=3일 때의 예이다.



입력
첫째 줄에 정수 N, r, c가 주어진다.

출력
r행 c열을 몇 번째로 방문했는지 출력한다.

제한
1 ≤ N ≤ 15
0 ≤ r, c < 2N

예제 입력 1 
2 3 1

예제 출력 1 
11

예제 입력 2 
3 7 7

예제 출력 2 
63
'''

import sys

N, r, c = map(int, sys.stdin.readline().rstrip().split(' '))
n = pow(2, N)
order = 0
if r < n or c < n:

	while n > 0:
		n = n//2
		# print(n, r, c)
		if r+1 <= n and c+1 > n:
			order += n*n
			c = c - n
		elif r+1 > n and c+1 <= n:
			order += n*n*2
			r = r - n
		elif r+1 > n and c+1 > n:
			order += n*n*3
			r = r - n
			c = c - n

	print(order)
else:
	print(order)
