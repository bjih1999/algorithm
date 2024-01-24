import sys
from itertools import permutations

l, c = list(map(int, sys.stdin.readline().rstrip().split()))
letters = sorted(sys.stdin.readline().rstrip().split())
arr = [0 for _ in range(len(letters))]

def is_vowel(c):
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

def func(k, st):
    global l, c, arr

    if k == l:

        v_count = 0
        c_count = 0
        result = ''
        for i in range(l):
            result += letters[arr[i]]
            if is_vowel(letters[arr[i]]):
                v_count += 1
            else:
                c_count += 1
        
        # print(result)
        # print('v', v_count)
        if v_count >= 1 and c_count >= 2:
            print(result)
        return


    for i in range(st, c):
        arr[k] = i
        func(k+1, i + 1)

func(0, 0)