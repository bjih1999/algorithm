'''
문제 설명
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

예를들어

- 0ms 시점에 3ms가 소요되는 A작업 요청
- 1ms 시점에 9ms가 소요되는 B작업 요청
- 2ms 시점에 6ms가 소요되는 C작업 요청

- A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
- B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
- C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)
이 때 각 작업의 요청부터 종료까지 걸린 시간의 평균은 10ms(= (3 + 11 + 16) / 3)가 됩니다.

하지만 A → C → B 순서대로 처리하면

- A: 3ms 시점에 작업 완료(요청에서 종료까지 : 3ms)
- C: 2ms부터 대기하다가, 3ms 시점에 작업을 시작해서 9ms 시점에 작업 완료(요청에서 종료까지 : 7ms)
- B: 1ms부터 대기하다가, 9ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 17ms)
이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.

각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

제한 사항
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

입출력 예
jobs	return
[[0, 3], [1, 9], [2, 6]]	9

입출력 예 설명
문제에 주어진 예와 같습니다.

0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.
1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.
2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.

https://programmers.co.kr/learn/courses/30/lessons/42627
'''

import heapq

def solution(jobs):
    answer = 0
    sec = 0
    index = 0
    total_waiting_time = 0
    heap = []
    
    jobs = sorted(jobs, key=lambda x: x[0])
    
    while True:
        while index < len(jobs) and jobs[index][0] <= sec:
            # print(sec)
            # print(jobs[index])
            
            heapq.heappush(heap, (jobs[index][1], jobs[index][0]))
            index += 1
        
        if len(heap) <= 0:
            sec += 1
        else:
            # print('heap : ', heap)
            current_job = heapq.heappop(heap)
            # print('!', (sec - current_job[1] + current_job[0]))
            total_waiting_time += (sec - current_job[1] + current_job[0])
            sec += current_job[0]
            # print('sec : ', sec)

        if index >= len(jobs) and len(heap) <= 0:
            break

    return int(total_waiting_time / len(jobs))

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 3], [0, 3]]))
print(solution([[0, 9], [1, 1], [1, 1], [1, 1], [1, 1]]))
print(solution([[0, 10], [2,10], [9,10], [15,2]]))
print(solution([[0, 10], [2,10], [25,10], [25,2]]))
print(solution([[0, 3], [1, 9], [500, 6]]))
print(solution([[0, 5], [1, 2], [5, 5]]))
print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))
print(solution([[0, 5], [1, 2], [5, 5]]))
print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))