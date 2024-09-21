'''
1 <= topping의 길이 n < 1,000,000
1 <= topping의 원소 m < 10,000
로 모든 자를수 있는 구간(n)에 대해 좌우의 토핑 개수(m)을 세는 풀이는 n*m이 10^9를 넘어가므로 불가능

풀이)
n에 대해 최대 O(n log n)이 가능

누적합을 사용하여,
a는 0 ~ i까지의 토핑 종류의 개수
b는 n-1 ~ i까지의 토핑종류의 개수
를 계산하여
a_count[i] == b_count[i+1] 인 경우를 count함
'''


def solution(topping):
    answer = 0
    n = len(topping)
    a = set()
    a_count = [-1 for _ in range(n)]
    b = set()
    b_count = [-1 for _ in range(n)]
    
    # a_count = a가 0~i까지 가져갔을때 토핑의 종류 개수
    # b_count = b가 n-1~i까지 가져갔을때 토핑의 종류 개수
    for i in range(n):
        a.add(topping[i])
        a_count[i] = len(a)
        b.add(topping[n-1-i])
        b_count[n-1-i] = len(b)
    
    # i를 기준으로 a가 0 ~ i b가 i+1 ~ n 까지 가져갔을때 토핑 개수가 같은 경우 answer ++
    for i in range(n-1):
        if a_count[i] == b_count[i+1]:
            answer += 1
    return answer