#-*- encoding: utf-8 -*-
'''
알고리즘: greedy

문제링크: https://www.acmicpc.net/problem/2217

문제 핵심:

N < 100,000 이고, 제한시간 2초이므로 O(200n)의 풀이가 가능하다.

들 수 있는 최대의 무게를 w, 사용한 로프의 개수를 k개라고 했을때,
로프를 병렬적으로 연결하면 각 로프에는 w/k만큼의 중량이 걸린다. 즉, 연결된 모든 로프는 w/k 이상을 들 수 있어야한다.
모든 로프가 동일한 중량을 견뎌야하기 때문에 w는 (사용한 로프중 가장 적은 무게를 견딜 수 있는 무게) * k가 된다.
따라서 위 문제는, 로프를 계속 추가했을때, 가장 큰 w값을 찾는 문제로 정의할 수 있다.

w를 늘리기 위해 버틸 수 있는 무게가 큰 순서대로 로프를 선택해야하는 것은 자명해보인다.
이는,
(버틸 수 있는 무게 순으로 선택하지 않았을때의 w) < (버틸 수 있는 무게 순으로 선택했을때의 w) 가 항상 성립함으로 증명할 수 있다.

버틸 수 있는 무게 순으로 선택하지 않았을 때의 로프들이 버틸 수 있는 무게를 순서대로
a1, a2, a3
버틸 수 있는 무게 순으로 선택했을때의 로프들이 버틸 수 있는 무게를 순서대로
b1, b2, b3라고 했을때,

(a1 <= b1, a2 <= b2, a3 <= b3, a1 < a2 < a3)
w1 = (a1 + a2 + a3) / 3
w2 = (b1 + b2 + b3) / 3 
일때, w1 < w2가 항상 성립하기 때문이다.


'''

import sys

N = int(sys.stdin.readline().strip())

ropes = []
for _ in range(N):
    ropes.append(int(sys.stdin.readline().strip()))

# 로프를 중량 순으로 정렬
ropes = sorted(ropes, reverse=True)

result = 0
for k, rope in enumerate(ropes):
    result = max(result, rope * (k + 1))
    

print(result)


