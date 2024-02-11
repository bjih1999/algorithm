import sys
from copy import deepcopy
# input
n, m ,k = list(map(int, sys.stdin.readline().rstrip().split()))

sizes = []
stickers = []
board = []
answer = 0
r, c = 0, 0


for _ in range(n):
    board.append([0 for _ in range(m)])

for _ in range(k):
    r, c = list(map(int, sys.stdin.readline().rstrip().split()))
    sizes.append((r, c))

    temp_sticker = []
    for _ in range(r):
        temp_sticker.append(list(map(int, sys.stdin.readline().rstrip().split())))
    

    cur_sticker = []

    for i in range(10):
        cur_sticker.append([0 for _ in range(10)])

    for i, row in enumerate(temp_sticker):
        for j, col in enumerate(row):
            cur_sticker[i][j] = col

    stickers.append(cur_sticker)

# for s1 in stickers:
#     for s in s1:
#         print(s)
#     print('')

# func
def check(i, j, sticker):
    global r, c, board
    # for s in sticker:
    #     print(s)
    # print(' ')
    for x in range(r):
        for y in range(c):
            if board[i + x][j + y] == 1 and sticker[x][y] == 1:
                return False

    return True

def put(i, j, sticker):
    global r, c, answer
    for x in range(r):
        for y in range(c):
            if sticker[x][y] == 1:
                answer += 1
                board[i + x][j + y] = 1

def rotate(sticker):

    global r, c
    temp = []
    for i in range(10):
        temp.append([0 for _ in range(10)])

    for i in range(c):
        for j in range(r):
            temp[i][j] = sticker[r-1-j][i]
    
    r, c = c, r
    
    # print('s')
    # for s in sticker:
    #     print(s)
    # print('t')
    # for t in temp:
    #     print(t)
    
    return temp



# main
for index, sticker in enumerate(stickers):
    r, c = sizes[index]
    pasted = False
    for _ in range(4):
        for i in range(n-r+1):
            for j in range(m-c+1):
                if check(i, j, sticker):
                    put(i, j, sticker)
                    # for s in sticker:
                    #     print(s)
                    # print('')
                    # for b in board:
                    #     print(b)
                    # print('')
                    pasted = True
                    break
            if pasted:
                break
        sticker = rotate(sticker)
        if pasted:
            break

# for b in board:
#     print(b)
print(answer)
