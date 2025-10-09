'''
1차 풀이 -> /re_and_again/시뮬레이션/programmers/level3/표 병합

최대 시간 복잡도 => 모든 명령어에 대해 모든 셀을 탐색하는 경우: O(명령어 최대 개수 * 셀 최대 개수) = O(1000 * 50*50) = O(10^6)

union find 풀이
'''

def solution(commands):
    
    n = 51
    merged = []
    contents = []
    answer = []
    for i in range(n):
        merged.append([])
        contents.append([None] * n)
        for j in range(n):
            merged[i].append((i, j))
    def find(r, c):
        i, j = r, c
        
        while merged[i][j] != (i, j):
            i, j = merged[i][j]
            
        return i, j
    
    def merge(r1, c1, r2, c2):
        merged[r2][c2] = (r1, c1)
    
    
    for command in commands:
        instruction = command.split()
        
        #1 
        if instruction[0] == 'UPDATE' and len(instruction) == 4:
            r, c = int(instruction[1]), int(instruction[2])
            value = instruction[3]
            
            i, j = find(r, c)
            
            contents[i][j] = value
        
        #2
        elif instruction[0] == 'UPDATE' and len(instruction) == 3:
            value1, value2 = instruction[1], instruction[2]
            
            to_be_updated = []
            for i in range(n):
                for j in range(n):
                    current_x, current_y = find(i, j)
                    if contents[current_x][current_y] == value1:
                        to_be_updated.append((current_x, current_y))
            
            for current_x, current_y in to_be_updated:
                contents[current_x][current_y] = value2
        
        elif instruction[0] == 'MERGE':
            r1, c1, r2, c2 = list(map(int, instruction[1:]))
            
            x1, y1 = find(r1, c1)
            x2, y2 = find(r2, c2)
            
            if (x1, y1) == (x2, y2):
                continue
            
            content1 = contents[x1][y1]
            content2 = contents[x2][y2]
            content = None
            if content1 and content2:
                content = content1
            elif not content1 and content2:
                content = content2
            elif content1 and not content2:
                content = content1
            
            merge(x1, y1, x2, y2)
            contents[x1][y1] = content
        
        elif instruction[0] == 'UNMERGE':
            r, c = list(map(int, instruction[1:]))
            
            x, y = find(r, c)
            content = contents[x][y]
            
            to_be_unmerged = []
            for i in range(n):
                for j in range(n):
                    current_x, current_y = find(i, j)
                    if x == current_x and y == current_y:
                        to_be_unmerged.append((i, j))
            
            for i, j in to_be_unmerged:
                merged[i][j] = (i, j)
                contents[i][j] = None
            
            if content:
                contents[r][c] = content
            
        elif instruction[0] == 'PRINT':
            r, c = list(map(int, instruction[1:]))
            x, y = find(r, c)
            result = contents[x][y]
            if not result:
                result = 'EMPTY'
            answer.append(result)
        
        # print(instruction)
        # print('merged')
        # for m in merged[:5]:
        #     print(m[:5])
        # print('contents')
        # for co in contents[:5]:
        #     print(co[:5])
        # print()
    return answer