import sys
import math

M = int(sys.stdin.readline().rstrip())

S = 0
answer = ''
for _ in range(M):
	instruction = list(sys.stdin.readline().rstrip().split())
	if len(instruction) == 2:
		x = instruction[1]
	operator = instruction[0]
	x = int(x)
	target_bit = x-1
	if operator == 'add':
		S |= 1<<target_bit
	elif operator == 'remove':
		S &= ~(1<<target_bit)
	elif operator == 'check':
		if S>>target_bit & 1 == 0:
			answer += '0'
		else:
			answer += '1'
		answer += '\n'
	elif operator == 'toggle':
		S ^= 1<<target_bit
	elif operator == 'all':
		S = 2**20-1
	elif operator == 'empty':
		S = 0

print(answer.rstrip())