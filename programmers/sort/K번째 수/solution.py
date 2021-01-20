def solution(array, commands):
    answer = []
    for command in commands:
        trimed = array[command[0]-1:command[1]]
        sorted_arr = sorted(trimed)
        answer.append(sorted_arr[command[2]-1])
    
    return answer