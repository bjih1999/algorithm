import sys

n = int(sys.stdin.readline.rstrip())

space = []
wide = 0
for _ in range(n):
	row = list(map(int, list(sys.stdin.readline().rstrip())))
	wide += sum(row)
	space.append(row)
	
result = {}
# for i in range(n):
# 	for j in range(n):
# 		if space[i][j] == 1:
# 			size = 1
# 			while size**2 <= wide:
# 				for row in range(size):
# 					for col in range(size())

