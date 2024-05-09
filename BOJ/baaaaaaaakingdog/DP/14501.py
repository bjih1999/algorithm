import sys

n = int(sys.stdin.readline().rstrip())
dp = []
period = []
for _ in range(n):
    list(map(int, sys.stdin.readline().rstrip().split()))