def solution(number, k):
    number_list = list(number)
    for i in range(k):
        number_list.remove(min(number_list[:len(number)-k]))
        
    return ''.join(number_list)

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))