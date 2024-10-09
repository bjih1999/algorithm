import sys

n, t = list(map(int, sys.stdin.readline().rstrip().split()))

emp_list = []
for _ in range(n):
    p, s = list(map(int, sys.stdin.readline().rstrip().split()))
    emp_list.append([p, s])

if n == 1:
    print(1)
else:
    last_pos = []
    for i in range(len(emp_list)):
        cur_pos = emp_list[i][0] + emp_list[i][1]*t
        last_pos.append(cur_pos)
    answer = 1
    slowest = last_pos[0]
    for i in range(1, len(last_pos)):
        if slowest < last_pos[i]:
            answer += 1
        
        slowest = last_pos[i]
    print(answer)