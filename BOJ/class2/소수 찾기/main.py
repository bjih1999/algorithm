'''
소수 찾기 

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	65380	30792	25299	48.231%

문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1 
4
1 3 5 7

예제 출력 1 
3
'''

import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 0

maximum = max(numbers)

prime_set = set([i for i in range(2, maximum+1)])
for i in range(2, maximum):
	if i in prime_set:
		prime_set -= set(range(2*i, maximum+1, i))

for number in numbers:
	if number in prime_set:
		answer += 1

print(answer)