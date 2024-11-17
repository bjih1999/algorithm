'''
특정 값보다 적으면서 조건을 만족하는 가장 큰 수를 찾는 문제

** level이 낮을 수록 시간이 오래 갈리는 상황 **에서, 문제 푸는 총 시간이 limit보다 작은 가장 큰 level을 구해야함

level을 계산하는데 드는 시간 복잡도는 O(n), n <= 300,000
level의 범위는 1 < level < 100,000 으로 모든 level을 확인하기에는 최대 100,000 * 300,000 의 시간이 소요됨

시간을 계산하는 함수는 f라고 했을 때,
이때, 현재 level에 대한 f(level)이 limit보다 작을 경우 최적의 limit 값은 무조건 현재 level 이상이기 때문에, 이분 탐색 접근이 가능하다.
이분 탐색으로 level을 찾는다면 log(100,000) * 300,000 풀이가 가능하다.

정답 값을 answer이라고 할때,
f(level) < limit인 경우, answer은 무조건 answer > level + 1 이고
f(level) > limit인 경우, answer은 무조건 answer < level - 1 이기 때문에

level에 대한 이분 탐색으로 문제를 정의할 수 있다.

'''
def calculate_time(diffs, times, prev_times, level):
    time = 0
    for i, d in enumerate(diffs):
        if d > level:
            time += (d - level) * (prev_times[i] + times[i])
        time += times[i]
    return time

def solution(diffs, times, limit):
    
    prev_times = [0] + times
    left = 1
    right = max(diffs)
    while left <= right:
        mid = (left + right) // 2
        current_time = calculate_time(diffs, times, prev_times, mid)
        
        if current_time > limit:
            left = mid + 1
        else:
            right = mid - 1
        
    return left