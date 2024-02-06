import sys

# input
n, m ,k = list(map(int, sys.stdin.readline().rstrip().split()))

sizes = []
stickers = []
board = []

r, c = 0, 0


for _ in range(n):
    board.append([0 for _ in range(m)])

for _ in range(k):
    r, c = list(map(int, sys.stdin.readline().rstrip().split()))
    sizes.append((r, c))

    cur_sticker = []
    for _ in range(r):
        cur_sticker.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    stickers.append(cur_sticker)


# func
def 


# main
for sticker, index in enumerate(stickers):
    
    for i in range(n - sizes[index][0]):
        for j in range(m - sizes[index][1]):

