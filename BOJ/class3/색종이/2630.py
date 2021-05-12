import sys

def checkPaper(paper, white, blue, n):
	white = 0
	blue = 0
	cheked = [[False for _ in range(n)] for _ in range(n)]

	i = 0
	while i < n:
		j = 0
		while j < n:
			
	
	if white == n*n or blue == n*n:
		checkPaper()

def cutPaper(paper, n):


n = int(sys.stdin.readline().rstrip())

paper = []
for _ in range(n):
	paper.append(sys.stdin.readline().rstrip().split())

