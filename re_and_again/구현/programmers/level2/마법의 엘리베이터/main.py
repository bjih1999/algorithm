'''
storey <= 1억 이라 O(n) 이하 풀이만 가능한 상황
DP로 풀어보려고 했지만, 뒤로 가는 변수를 컨트롤하기 어려움
  * DP는 매열이 한방향으로 채워질 때 사용 가능한 것 같다 *

문제 해결 방법:
   storey를 한자리씩 반올림하고 그 차이만큼을 answer에 증가시킨다.
   가장큰 자리수가 올림이 된 경우 엘리베이터 한번을 더 타야하기 때문에 answer에 +1 해준다.
   (ex 9000에서 반올림되어 10000이 된경우 10000 -10000 => 0으로 만들어주는 것을 1 더 고려해주어야함)
'''

def solution(storey):
    
    answer = 0
    length = len(str(storey))
    
    result = storey
    for i in range(1, length+1):
        next_result = round(result, -1 * i)
        diff = abs(next_result - result) // 10 ** (i-1)
        answer += diff
        result = next_result
    
    if result != 0:
        answer += 1
    return answer