'''
유클리드 호제법
a > b일 때,
a와 b의 최소 공배수는
r = a % b
b와 r의 최소 공배수와 같다.
'''

def gcd(a, b):
    temp = [a, b]
    sorted(temp, key=lambda x:-1)
    a, b = temp

    while b != 0:
        r = a % b
        a = b
        b = r
    
    return a

def lcm(a, b):

    return a * b / gcd(a, b)

def solution(arr):
    answer = 0
    n = len(arr)
    cur = arr[0]
    arr = arr[1:]
    for num in arr:
        
        cur = lcm(cur, num)
    return cur