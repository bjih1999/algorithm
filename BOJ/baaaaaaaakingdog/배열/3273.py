import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(sys.stdin.readline().rstrip())

sorted_a = sorted(a)

start = 0
end = n - 1
count = 0
while start < end:
    cur = sorted_a[start] + sorted_a[end]
    if cur == x:
        count += 1
        start += 1
        end -= 1
    elif cur > x:
        end -= 1
    else:
        start += 1

print(count)