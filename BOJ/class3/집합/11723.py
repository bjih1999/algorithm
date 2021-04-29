import sys
import math

M = int(sys.stdin.readline().rstrip())

S = 0
answer = ''
for _ in range(M):
	target_bit = 0
	instruction = list(sys.stdin.readline().rstrip().split())
	if len(instruction) > 1:
		target_bit = int(instruction[1]) - 1

	if instruction[0] == 'add':
		S |= 1<<target_bit
	elif instruction[0] == 'remove':
		S &= ~(1<<target_bit)
	elif instruction[0] == 'check':
		if S>>target_bit & 1 == 0:
			answer += '0'
		else:
			answer += '1'
		answer += '\n'
	elif instruction[0] == 'toggle':
		S ^= 1<<target_bit
	elif instruction[0] == 'all':
		S = 2**20-1
	elif instruction[0] == 'empty':
		S = 0

print(answer.rstrip())