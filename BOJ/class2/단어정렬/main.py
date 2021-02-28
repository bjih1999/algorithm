import sys

N = int(sys.stdin.readline().rstrip())

words = set()
for i in range(N):
	words.add(sys.stdin.readline().rstrip())

sorted_words = sorted(words, key=lambda x:(len(x), x))

for word in sorted_words:
	print(word)