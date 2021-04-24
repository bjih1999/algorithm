import sys
import math

M = int(sys.stdin.readline().rstrip())

S = 0
output = []
for _ in range(M):
	instruction = list(sys.stdin.readline().rstrip().split())
	if len(instruction) == 2:
		x = instruction[1]
	operator = instruction[0]
	x = int(x)
	target_bit = 1<<(x-1)
	S = int(S)
	if operator == 'add':
		S |= 1<<target_bit
	elif operator == 'remove':
		S &= ~(1<<target_bit)
	elif operator == 'check':
		if S & 1<<target_bit == 0:
			output.append(0)
		else:
			output.append(1)
	elif operator == 'toggle':
		S ^= 1<<target_bit
	elif operator == 'all':
		S = math.pow(2, 21)-1
	elif operator == 'empty':
		S = 0

for x in output:
	print(x)