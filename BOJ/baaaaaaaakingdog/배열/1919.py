import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

count_a = {chr(letter):0 for letter in range(ord('a'), ord('z') + 1)}
count_b = {chr(letter):0 for letter in range(ord('a'), ord('z') + 1)}
for letter in a:
    count_a[letter] += 1

for letter in b:
    count_b[letter] += 1

n = len(count_a.items())
count = 0
for letter in range(ord('a'), ord('z')+1):
    count += abs(count_a[chr(letter)] - count_b[chr(letter)])

print(count)
