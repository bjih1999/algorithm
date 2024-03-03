import sys

n, k = list(map(int, list(sys.stdin.readline().rstrip().split())))
a = []

for _ in range(n):
    a.append(int(sys.stdin.readline().rstrip()))

reversed(a)

cur = k
count = 0

index = len(a) - 1
while cur > 0 or index >= 0:
    if a[index] <= cur:
        count += cur // a[index]
        cur -= a[index] * (cur // a[index])
    else:
        index -= 1

print(count)