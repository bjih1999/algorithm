import re
answer = []
count = 0
removed_count = 0
def first(s):
    global answer, removed_count
    pattern = r'[0]{1}'
    removed_count += s.count('0')
    return re.sub(pattern, '', s)

def second(s):
    l = len(s)
    return format(l, 'b')
        
def solution(s):
    global count, removed_count
    while s != '1':
        s = first(s)
        s = second(s)
        count += 1
        
    
    return [count, removed_count]