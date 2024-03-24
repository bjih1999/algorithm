# -*- coding: utf-8 -*-

def solution(cap, n, deliveries, pickups):
    
    # 가장 마지막 집 찾기
    cur = n - 1
    while not deliveries[cur] and not pickups[cur]:
        cur -= 1

    distance = 0
    
    cur_cap = 0
    carrying = 0
    last = 0
    while cur >= 0:
        last = cur
        while True:
            if cur < 0:
                break
            
            if cur_cap + deliveries[cur] > cap or carrying + pickups[cur] > cap:
                distance += (last + 1) * 2
                cur_cap = 0
                carrying = 0
                print(last + 1)
                break
            
            cur_cap += deliveries[cur]
            carrying + pickups[cur]
            
            cur -= 1
    
    distance += (last + 1) * 2
    return distance

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))