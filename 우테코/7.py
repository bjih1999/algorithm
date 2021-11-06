def solution(grid, clockwise):
    answer = []
    grid.reverse()
    if clockwise:
        for index in range(len(grid)):
            grid[index] = grid[index][::-1]

        print(grid)
        temp_row = ''
        while len(grid):
            for index in range(len(grid)):
                if len(grid[index]) >= 2:
                    temp_row += grid[index][:2]
                    grid[index] = grid[index][2:]
                else:
                    temp_row += grid[index]
                    grid[index] = ''
            print(grid)
            if '' in grid:
                grid.remove('')
            answer.append(temp_row)
            temp_row = ''
    answer.reverse()
    return answer

print(solution(["1","234","56789"], True))