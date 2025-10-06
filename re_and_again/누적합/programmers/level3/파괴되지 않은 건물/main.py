'''
누적합을 이용한 풀이.
skill 때마다 영향 범위만큼을 순회하며 얼마나 데미지를 입었는지를 체크하면 좋지만,
len(skill) < 250,000 이고 n < 1,000, m < 1,000 이라 최악의 경우 O(2.5 * 10^5 * 10^3 * 10^3) => O(10^11)이라 불가능

그래서 skill마다 어디에서 어디까지 누적합을 해야하는지 "표시"만 해둔 후에 나중에 누적합을 한번에 시키는 방식을 취해야 한다.
비슷한 문제로는 re_and_again/누적합/programmers/level3/광고 삽입 이 있다.

1. r1, c1에 -1 * degree 만큼을 더한다. (아군 힐링 스킬일 경우 -1을 곱하지 않는다.)
2. r2+1, c1에 degree 만큼을 더한다. 이는 아래로 누적합을 했을 때 1의 영향이 범위 밖으로 나가지 않도록 해준다.
3. r1, c2+1에 degree 만큼을 더해준다. 이는 오른쪽으로 누적합을 했을 때, 1의 옇양이 범위 밖으로 나가지 않도록 해준다.
4. r2+1, c2+1에 -1 * degree 만큼을 더한다. 이는 3이 아래로 누적합이 되었을 때 이에 대한 영향이 범위 밖으로 나가지 않도록 해준다.

5. 아래로 한번, 오른쪽으로 한번 누적합을 해준다.
6. _map과 board를 더해준다.
7. 체력이 0 초과인 원소의 개수를 세서 리턴한다.


처음에 틀렸던 부분)
초기에는 skill 마다 r1부터 r2+1까지를 순회하며 아래로 누적합을 먼저 하는 것을 시도했다.
근데 이렇게 하면
최약의 경우 O(2.5 * 10^5 * 10^3) 이기 때문에 시간 초과가 발생함.
따라서 skill 내부에서 아래로 누적합조차 하면 안되기 때문에, 위와 같이 수정함.

초기 코드)

def solution(board, skill):
    
    n = len(board)
    m = len(board[0])
    _map = [[0] * m for _ in range(n)]
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1

        for r in range(r1, r2+1):
            _map[r][c1] += degree
            
            if c2 + 1 < m:
                _map[r][c2 + 1] += -1 * degree

    for i in range(n):
        for j in range(1, m):
            _map[i][j] = _map[i][j] + _map[i][j-1]
    
    for i in range(n):
        for j in range(m):
            board[i][j] += _map[i][j]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                answer += 1
    
    # for b in board:
    #     print(b)
    return answer
'''
def solution(board, skill):
    
    n = len(board)
    m = len(board[0])
    _map = [[0] * m for _ in range(n)]
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1

        _map[r1][c1] += degree
        
        if r2+1 < n:
            _map[r2+1][c1] += -1 * degree
        
        if c2+1 < m:
            _map[r1][c2+1] += -1 * degree
        
        if r2+1 < n and c2+1 < m:
            _map[r2+1][c2+1] += degree
        
    for i in range(1, n):
        for j in range(m):
            _map[i][j] = _map[i][j] + _map[i-1][j]
    
    for i in range(n):
        for j in range(1, m):
            _map[i][j] = _map[i][j] + _map[i][j-1]
    
    for i in range(n):
        for j in range(m):
            board[i][j] += _map[i][j]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                answer += 1
    
    return answer