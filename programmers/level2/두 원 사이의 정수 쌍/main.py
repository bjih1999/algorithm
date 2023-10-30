import math

def solution(r1, r2):
    
    return countLarge(r2) - countSmall(r1) 

def countLarge(r):
    count = 0
    for i in range(0, r):
        count += math.floor( math.sqrt(r ** 2 - i ** 2))
    
    return int(count * 4)

def countSmall(r):
    count = 0
    for x in range(0, r):
        y = math.sqrt(r ** 2 - x ** 2)
        count += int(math.floor(y))

        if int(math.floor(y)) == y:
            count -= 1
    return count * 4

print(solution(2, 3))

print(countLarge(3))
print(countSmall(2))
