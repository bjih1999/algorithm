'''
���ϻ���
�ð� ����	�޸� ����	����	����	���� ���	���� ����
1 ��	128 MB	19158	11130	8783	58.139%
����
���ϻ����� �������� �ʷϻ��� ���̸� ���� ������ ���Ѵ�. ����, ���ϻ����� ����� ���� �׸��� �ƴ� ����� ���� �׸����� �� �ٸ� �� �ִ�.

ũ�Ⱑ N��N�� �׸����� �� ĭ�� R(����), G(�ʷ�), B(�Ķ�) �� �ϳ��� ��ĥ�� �׸��� �ִ�. �׸��� �� ���� �������� �������� �ִµ�, ������ ���� ������ �̷���� �ִ�. ��, ���� ������ �����¿�� ������ �ִ� ��쿡 �� ���ڴ� ���� ������ ���Ѵ�. (������ ���̸� ���� ������ ���ϴ� ��쵵 ���� �����̶� �Ѵ�)

���� ���, �׸��� �Ʒ��� ���� ��쿡

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
���ϻ����� �ƴ� ����� ���� �� ������ ���� �� 4���̴�. (���� 2, �Ķ� 1, �ʷ� 1) ������, ���ϻ����� ����� ������ 3�� �� �� �ִ�. (����-�ʷ� 2, �Ķ� 1)

�׸��� �Է����� �־����� ��, ���ϻ����� ����� ���� ���� �ƴ� ����� ���� �� ������ ���� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է�
ù° �ٿ� N�� �־�����. (1 �� N �� 100)

��° �ٺ��� N�� �ٿ��� �׸��� �־�����.

���
���ϻ����� �ƴ� ����� ���� ���� ������ ������ ���ϻ����� ����� ���� ���� ������ ���� �������� ������ ����Ѵ�.

���� �Է� 1 
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
���� ��� 1 
4 3
'''
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
picture = []
que = deque()
visited = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N):
    picture.append(list(sys.stdin.readline().rstrip()))

area_cnt = 0
i = 0
while i < N:
    j = 0
    while j < N:
        if visited[i][j] == False:
            cur_color = picture[i][j]

            visited[i][j] = True
            que.append((i, j, area_cnt))
            while que:
                y, x, _ = que.popleft()
                if 0 <= y-1 < N and visited[y-1][x] == False and picture[y-1][x] == cur_color:
                    que.append((y-1, x, area_cnt))
                    visited[y-1][x] = True
                if 0 <= y+1 < N and visited[y+1][x] == False and picture[y+1][x] == cur_color:
                    que.append((y+1, x, area_cnt))
                    visited[y+1][x] = True
                if 0 <= x-1 < N and visited[y][x-1] == False and picture[y][x-1] == cur_color:
                    que.append((y, x-1, area_cnt))
                    visited[y][x-1] = True
                if 0 <= x+1 < N and visited[y][x+1] == False and picture[y][x+1] == cur_color:
                    que.append((y, x+1, area_cnt))
                    visited[y][x+1] = True
            area_cnt += 1
        j += 1
    i += 1
print(area_cnt)
que = deque()
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'
area_cnt = 0
i = 0
while i < N:
    j = 0
    while j < N:
        if visited[i][j] == False:
            cur_color = picture[i][j]

            visited[i][j] = True
            que.append((i, j, area_cnt))
            while que:
                y, x, _ = que.popleft()
                if 0 <= y-1 < N and visited[y-1][x] == False and picture[y-1][x] == cur_color:
                    que.append((y-1, x, area_cnt))
                    visited[y-1][x] = True
                if 0 <= y+1 < N and visited[y+1][x] == False and picture[y+1][x] == cur_color:
                    que.append((y+1, x, area_cnt))
                    visited[y+1][x] = True
                if 0 <= x-1 < N and visited[y][x-1] == False and picture[y][x-1] == cur_color:
                    que.append((y, x-1, area_cnt))
                    visited[y][x-1] = True
                if 0 <= x+1 < N and visited[y][x+1] == False and picture[y][x+1] == cur_color:
                    que.append((y, x+1, area_cnt))
                    visited[y][x+1] = True
            area_cnt += 1
        j += 1
    i += 1
print(area_cnt)