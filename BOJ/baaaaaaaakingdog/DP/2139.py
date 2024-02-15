import sys 

n = int(sys.stdin.readline().strip())


a = 1
b = 1
c = 1
for i in range(3, n+1):
    c = a + b
    a = b
    b = c

print(c)