import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

board1 = []
board2 = []
for i in range(8):
	row1 = []
	row2 = []
	for j in range(8):
		if (i+j) % 2 == 0:
			row1.append('W')
			row2.append('B')
		else:
			row1.append('B')
			row2.append('W')
	board1.append(row1)
	board2.append(row2)
# print(board1)
# print(board2)

board = []
for i in range(N):
	board.append(list(sys.stdin.readline().rstrip()))
# print(board)
minimum = 64
for i in range(N+1-8):
	for j in range(M+1-8):
		cnt1 = 0
		cnt2 = 0
		# print('!!', i, j)
		for row in range(8):
			for col in range(8):
				if board[i+row][j+col] != board1[row][col]:
					# print('1')
					# print('??', i+row, j+col)
					# print(board[row][col] != board1[row][col])
					# print(board[row][col], board1[row][col])
					cnt1 += 1
				if board[i+row][j+col] != board2[row][col]:
					# print('2')
					# print('??', i-1+row, j-1+col)
					# print(board[row][col] != board1[row][col])
					# print(board[row][col], board1[row][col])
					cnt2 += 1
		# print('cnt1', cnt1)
		# print('cnt2', cnt2)
		less_diff = min(cnt1, cnt2)
		# print(less_diff)
		if minimum > less_diff:
			minimum = less_diff

print(minimum)
		