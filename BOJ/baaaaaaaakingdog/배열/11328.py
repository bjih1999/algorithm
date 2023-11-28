import sys

n = int(sys.stdin.readline().rstrip())
input_list = []

for _ in range(n):
    input_list.append(sys.stdin.readline().strip().split())

for input in input_list:
    a, b = input
    if sorted(a) == sorted(b):
        print('Possible')
    else:
        print('Impossible')

