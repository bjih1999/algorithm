'''

�ð� ����	�޸� ����	����	����	���� ���	���� ����
1 ��	256 MB	736	318	213	42.430%

����
��ȣ�� ��ȣ�� 2���� ��ǥ ��� ���� �ִ�. ��ȣ�� �� A(Ax, Ay)���� �� B(Bx, By)�� ���� �ɾ�� �ְ�, ��ȣ�� �� C(Cx, Cy)���� �� D(Dx, Dy)�� ���� �ɾ�� �ִ�. ��ȣ�� ��ȣ�� ���ÿ� ����ϰ�, ��ȣ�� �� B�� �����ϴ� ���� ��ȣ�� �� D�� �����Ѵ�. ��, �� ����� �׻� ������ �ӵ��� �ɾ��. �� ����� �Ÿ��� ���� ����� ��, �Ÿ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

�� �� (x1, y1), (x2, y2)������ �Ÿ���  �̴�.

�Է�
ù° �ٿ� Ax, Ay, Bx, By, Cx, Cy, Dx, Dy�� �־�����. �Է����� �־����� ��� ��ǥ�� 0���� ũ�ų� ����, 10000���� �۰ų� ���� �����̴�.

���
��ȣ�� ��ȣ�� ���� ������� ���� �Ÿ��� ����Ѵ�. ����/��� ������ 10-6���� ����Ѵ�.

���� �Է� 1 
0 0 1 1 2 2 3 3
���� ��� 1 
2.8284271247
���� �Է� 2 
0 0 1 1 1 0 0 1
���� ��� 2 
0.0000000000
���� �Է� 3 
0 0 10 20 30 0 5 10
���� ��� 3 
8.2416338387
���� �Է� 4 
5 5 10 10 7 2 20 30
���� ��� 4 
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