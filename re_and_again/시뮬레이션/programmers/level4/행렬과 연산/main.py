'''
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
로 예시를 들었을 때
양 끝은 세로 deque, 그 중간은 가로 deque로 관리한다.

예시)
 -     -
 1 |2| 3
 4 |5| 6
 7 |8| 9
 -     - 
 
이 때
rows는 [[2], [5], [8]]
cols는 [[1, 4, 7], [3, 6, 9]] 와 같은 형태가 된다.


1) operation이 Rotate일 경우,
    rows의 가장 마지막 deque를 꺼내 앞에 붙여서 가로 순환을 시킨다.
    cols도 가장 마지막 deque를 꺼내 앞에 붙여서 세로 순환을 시킨다.
    -     -
    4 |5| 6
    7 |8| 9
    1 |2| 3
    -     - 


2) opertion이 ShiftRow인 경우,

    1. cols[0]의 popleft()를 해서 rows[0]에 appendleft를 한다.
    -        -
      |1, 2| 3
    4 |5|    6
    7 |8|    9
    -        -
    
    2. rows[0]에 pop을 하여 cols[1]에 appendleft를 한다.
    -     -
      |1| 2
    4 |5| 3
    7 |8| 6
          9
    -     -
    
    3. cols[1]에 pop을 하여 rows[-1]에 append를 한다.
    -        -
      |1|    2
    4 |5|    3
    7 |8, 9| 6
    -        -
    
    4. rows[-1]에 popleft를 하여 cols[0]에 append를 한다.
    -     -
    4 |1| 2
    7 |5| 3
    8 |9| 6
    -     -
    

3) 모든 처리를 다 끝내고 출력을 잘 해준다.


* 시간 복잡도
    O(max(n개의 배열을 초기화 하는 시간, operation의 개수))
    => O(max(n, len(operations)))
    => O(max(5 * 10^4, 10^5))
    => O(10^5)
'''

from collections import deque

def solution(rc, operations):
    answer = [[]]
    rows = deque()
    cols = deque()
    cols.append(deque())
    cols.append(deque())
    n = len(rc)
    m = len(rc[0])
    
    for i in range(n):
        rows.append(deque(rc[i][1:-1]))
        cols[0].append(rc[i][0])
        cols[1].append(rc[i][-1])

    
    for op in operations:
        if op == 'ShiftRow':
            
            last_row = rows.pop()
            rows.appendleft(last_row)
            
            left_up = cols[0].pop()
            cols[0].appendleft(left_up)
            
            right_up = cols[1].pop()
            cols[1].appendleft(right_up)
        
        elif op == 'Rotate':
            
            left_up = cols[0].popleft()
            rows[0].appendleft(left_up)
            
            right_up = rows[0].pop()
            cols[1].appendleft(right_up)
            
            right_down = cols[1].pop()
            rows[-1].append(right_down)
            
            left_down = rows[-1].popleft()
            cols[0].append(left_down)
            
    answer = []
    
    for i in range(n):
        answer.append([cols[0][i], *list(rows[i]), cols[1][i]])
    return answer