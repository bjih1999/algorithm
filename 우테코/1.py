def solution(arr):
    count_arr = []
    sorted_arr = sorted(arr)
    answer = []
    for i in range(3):
        count_arr.append(sorted_arr.count(i+1))
    
    maximum = max(count_arr)
    
    for count in count_arr:
        answer.append(maximum - count)
    return answer

print(solution([2, 1, 3, 1, 2, 1]))
print(solution([3, 3, 3, 3, 3, 3]))
