'''

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	736	318	213	42.430%

문제
민호와 강호가 2차원 좌표 평면 위에 있다. 민호는 점 A(Ax, Ay)에서 점 B(Bx, By)를 향해 걸어가고 있고, 강호는 점 C(Cx, Cy)에서 점 D(Dx, Dy)를 향해 걸어가고 있다. 민호와 강호는 동시에 출발하고, 민호가 점 B에 도착하는 순간 강호도 점 D에 도착한다. 또, 두 사람은 항상 일정한 속도로 걸어간다. 두 사람의 거리가 가장 가까울 때, 거리를 구하는 프로그램을 작성하시오.

두 점 (x1, y1), (x2, y2)사이의 거리는  이다.

입력
첫째 줄에 Ax, Ay, Bx, By, Cx, Cy, Dx, Dy가 주어진다. 입력으로 주어지는 모든 좌표는 0보다 크거나 같고, 10000보다 작거나 같은 정수이다.

출력
민호와 강호가 가장 가까웠을 때의 거리를 출력한다. 절대/상대 오차는 10-6까지 허용한다.

예제 입력 1 
0 0 1 1 2 2 3 3
예제 출력 1 
2.8284271247
예제 입력 2 
0 0 1 1 1 0 0 1
예제 출력 2 
0.0000000000
예제 입력 3 
0 0 10 20 30 0 5 10
예제 출력 3 
8.2416338387
예제 입력 4 
5 5 10 10 7 2 20 30
예제 출력 4 
2.8745554697
'''

import sys
import math

def _get_distance(x1, y1, x2, y2):
	return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

arr = list(map(int, sys.stdin.readline().split()))

Ax = arr[0]
Ay = arr[1]
Bx = arr[2]
By = arr[3]
Cx = arr[4]
Cy = arr[5]
Dx = arr[6]
Dy = arr[7]
# print(arr)
m_gradient = (By-Ay) / (Bx-Ax)
# print('m_gradient', m_gradient)
g_gradient = (Dy-Cy) / (Dx-Cx)
# print('g_gradient', g_gradient)

speed = (Dx-Cx) / (Bx-Ax)
# print('speed', speed)
shortest = 10000
for x in range(0, 1000000):
	delta = x/1000000

	distance = _get_distance(Ax + (Bx-Ax)*delta, Ay + (By-Ay)*delta, Cx + (Dx-Cx)*delta, Cy + (Dy-Cy)*delta)
	if shortest >= distance:
		shortest = distance
		answer = [Ax + delta,  m_gradient * (Ax+delta) + -m_gradient*Ax + Ay, Cx + speed*delta, g_gradient * (Cx + speed*delta) +  -g_gradient*Cx + Cy]
		answer_delta = delta
	else:
		break
# print(answer)
# print(answer_delta)
sys.stdout.write(str(round(shortest, 10)))