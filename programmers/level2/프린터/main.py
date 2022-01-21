from collections import deque

def solution(priorities, location):
    answer = 1
    q = deque()
    
    rank = sorted(priorities, reverse=True)
    rank = deque(rank)
    for index, priority in enumerate(priorities):
        q.append((index, priority))

    while q:
        if q[0][1] == rank[0]:
            if q[0][0] == location:
                break
            q.popleft()
            rank.popleft()
            answer += 1            
        else:
            q.rotate(-1)
    return answer