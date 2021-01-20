import functools

def solution(numbers):
    answer = ''
    result = []
    string_numbers = [str(number) for number in numbers]
    sorted_numbers = sorted(string_numbers, key=functools.cmp_to_key(lambda x, y: int(x+y) - int(y+x)), reverse=True)
    answer = str(int(''.join(sorted_numbers)))
    return answer