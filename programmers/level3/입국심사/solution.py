def solution(n, times):
    times = sorted(times, key=lambda x:x)
    wait_time = [0 for i in range(len(times))]
    for i in range(n):
        index = 0
        while index+1 < len(times):
            print(wait_time)
            print(wait_time[index+1] + times[index+1])
            print(wait_time[index] + times[index])
            if wait_time[index+1] + times[index+1] > wait_time[index] + times[index]:
                wait_time[index] += times[index]
                break
            index += 1
    print(wait_time)
    answer = max(wait_time)
    return answer

print(solution(6, [7, 10]))