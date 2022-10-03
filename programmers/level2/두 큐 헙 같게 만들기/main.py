from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2
    len1 = len(queue1)
    len2 = len(queue2)
    max_op = (len1 + len2) * 2
    count = 0
    if total % 2 == 1:
        return -1
    
    while sum1 != sum2:
        if not queue1 and not queue2:
            return -1
        
        if max_op < count:
            return -1
        
        if sum1 > sum2:
            temp = queue1.popleft()
            queue2.append(temp)
            sum2 += temp
            sum1 -= temp
        else:
            temp = queue2.popleft()
            queue1.append(temp)
            sum1 += temp
            sum2 -= temp
        count += 1

    return count