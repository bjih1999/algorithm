def solution(s):
    s_list = s.lower().split(' ')
    result_list = []
    
    for s in s_list:
        result_list.append(s.capitalize())
    
    return ' '.join(result_list)