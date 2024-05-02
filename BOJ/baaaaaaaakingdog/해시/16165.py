import sys
import heapq

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

group = {}
members = {}
for _ in range(n):
    group_name = sys.stdin.readline().rstrip()
    count = int(sys.stdin.readline().rstrip())
    temp = []
    for _ in range(count):
        member_name = sys.stdin.readline().rstrip()
        temp.append(member_name)
        members[member_name] = group_name

    group[group_name] = sorted(temp)

for _ in range(m):
    question = sys.stdin.readline().rstrip()
    type = int(sys.stdin.readline().rstrip())

    if type:
        print(members[question])
    else:
       print('\n'.join(group[question]))