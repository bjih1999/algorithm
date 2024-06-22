def cal(arr1, arr2, i, j, n):
    result = 0
    for x in range(n):
        result += arr1[i][x] * arr2[x][j]
    
    return result

def solution(arr1, arr2):
    a = len(arr1)
    n = len(arr1[0])
    b = len(arr2[0])
    answer = []

    for i in range(a):
        row = []
        for j in range(b):
            row.append(cal(arr1, arr2, i, j, n))
        answer.append(row)
    return answer