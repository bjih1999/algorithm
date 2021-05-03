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
		if value in S:
			S.remove(value)
	elif instruction[0] == 'check':
		if value in S:
			answers+='1\n'
		else:
			answers+='0\n'
	elif instruction[0] == 'toggle':
		if value in S:
			S.remove(value)
		else:
			S.add(value)
	elif instruction[0] == 'all':
		for i in range(21):
			S.add(i)
	elif instruction[0] == 'empty':
		S.clear()

print(answers.rstrip())