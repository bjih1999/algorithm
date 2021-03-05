import sys

N = int(sys.stdin.readline().rstrip())

PS_list = []
for i in range(N):
	PS_list.append(sys.stdin.readline().rstrip())

stack = []
answers = []
# print(PS_list)
for PS in PS_list:
	for letter in PS:
		if letter == '(':
			stack.append(letter)
		else:
			if len(stack) == 0:
				stack.append(letter)
				break
			elif stack[-1] == '(':
				stack.pop()

	if len(stack) == 0:
		answers.append('YES')
	else:
		answers.append('NO')
	stack = []

for answer in answers:
	print(answer)
	