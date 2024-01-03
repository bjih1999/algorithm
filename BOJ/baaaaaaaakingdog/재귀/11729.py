import sys

def func(arrive, dest, k):
    if k == 1:
        print('{0} {1}'.format(arrive, dest))
        return
    
    func(arrive, 6 - arrive - dest, k-1)
    print('{0} {1}'.format(arrive, dest))
    func(6 - arrive - dest, dest, k-1)

n = int(sys.stdin.readline().rstrip())

print((1 << n) -1)
func(1, 3, n)