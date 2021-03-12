'''
수 찾기
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	78657	24338	15975	30.220%

문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

예제 입력 1 
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1 
1
1
0
0
1
'''
import sys

N = int(sys.stdin.readline().rstrip())

src_list = list(set(map(int, sys.stdin.readline().rstrip().split())))

M = int(sys.stdin.readline().rstrip())

dest_list = list(map(int, sys.stdin.readline().rstrip().split()))

answers = []

sorted_src_list = sorted(src_list)

pos = 0
for num in dest_list:
	if num in sorted_src_list:
		answers.append(1)
	else:
		answers.append(0)
		
for answer in answers:
	print(answer)