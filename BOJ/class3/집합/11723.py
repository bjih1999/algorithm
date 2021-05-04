import sys
import math

M = int(sys.stdin.readline().rstrip())

S = set()
answers = ''
for _ in range(M):
	target_bit = 0
	instruction = sys.stdin.readline().rstrip().split()
	if len(instruction) > 1:
		value = int(instruction[1])

	if instruction[0] == 'add':
		S.add(value)
	elif instruction[0] == 'remove':
		S.discard(value)
	elif instruction[0] == 'check':
		if value in S:
			print(1)
		else:
			print(0)
	elif instruction[0] == 'toggle':
		if value in S:
			S.remove(value)
		else:
			S.add(value)
	elif instruction[0] == 'all':
		S = set(list(range(21)))
	elif instruction[0] == 'empty':
		S = set()