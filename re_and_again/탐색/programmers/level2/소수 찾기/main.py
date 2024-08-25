from itertools import permutations
'''
에라토스테네스의 체
[False, False] + [True] * (n+1) 인 배열을 만든다.

최초의 소수인 2부터 n+1까지 순회하며, 해당 숫자가 소수인 경우 n+1보다 작은 현재 숫자의 배수들을 모두 False로 바꾼다.

itertools.permutations으로 숫자를 조합할 수 있는 모든 경우를 계산하여 소수인지 아닌지 확인한다.
이때 숫자가 중복될 수 있으니 집합으로 중복을 제거한 후 숫자를 계산한다. 

'''
def solution(numbers):
    
    max_num = int(''.join(sorted(numbers, key = lambda x:-int(x))))
    primes = [False, False] + [True] * (max_num + 1)
    result = set()
    for i in range(2, max_num+1):
        if primes[i] == True:
            for j in range(2*i, max_num+1, i):
                primes[j] = False
    
    for i in range(1, len(numbers) + 1):
        candidates = list(permutations(numbers, i))
        
        for c in candidates:
            temp = int(''.join(c))

            if primes[temp]:
                result.add(temp)
    
    return len(result)