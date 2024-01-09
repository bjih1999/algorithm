import sys
import math
number = sys.stdin.readline().rstrip()

count = { n:0 for n in range(0, 9)}

for n in number:
    n = int(n)
    if n == 9 or n == 6:
        count[6] += 0.5
    else:
        count[n] += 1

count[6] = int(math.ceil(count[6]))
maximum = max(count.values())

print(maximum)
