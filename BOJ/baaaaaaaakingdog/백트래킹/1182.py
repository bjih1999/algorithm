import sys

n, s = list(map(int, sys.stdin.readline().rstrip().split()))

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 0

def func(k, sum):
    global answer
    if k >= n:
        if s == sum:
            answer += 1
        return
    
    func(k + 1, sum + numbers[k])
    func(k + 1, sum)

func(0, 0)
if s == 0:
    answer -= 1
print(answer)