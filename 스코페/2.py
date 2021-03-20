# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

total = 0

def dfs(index, path, n):
	global total
	if index == n-1:
		total += 1
		return
	
	if index + 1 < n:
		if path[index + 1] == 1:
			dfs(index+1, path, n)
	
	if index + 2 < n:
		if path[index + 2] == 1 :
			dfs(index+2, path, n)

n = int(sys.stdin.readline().rstrip())
path = list(map(int, list(sys.stdin.readline().rstrip())))
dfs(0, path, n)

print(total)
