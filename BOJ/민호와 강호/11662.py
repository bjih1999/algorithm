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
	if shortest > distance:
		shortest = distance
		# answer = [Ax + delta,  m_gradient * (Ax+delta) + -m_gradient*Ax + Ay, Cx + speed*delta, g_gradient * (Cx + speed*delta) +  -g_gradient*Cx + Cy]
		answer_delta = delta
# print(answer)
# print(answer_delta)
sys.stdout.write(str(round(shortest, 10)))