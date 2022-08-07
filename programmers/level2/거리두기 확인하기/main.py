def solution(places):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1),]
    length = 5
    rooms = []
    answer = []
    
    for place in places:
        room = []
        for row in place:
            room.append(list(row))
        rooms.append(room)
    
    for roomnuber, room in enumerate(rooms):
        visited = [[False for _ in range(length)] for _ in range(length)]
        try:
            for y, row in enumerate(room):
                for x, person in enumerate(row):
                    if person == 'P':
                        visited[y][x] = True
                        for move in moves:
                            if 0 <= x + move[1] < length and 0 <= y + move[0] < length:
                                if room[y + move[0]][x + move[1]] == 'P':
                                    raise Exception('1', roomnuber, y, x)
                                elif room[y + move[0]][x + move[1]] == 'O':
                                    for more_move in moves:
                                        if 0 <= y + move[0] + more_move[0] < length and 0 <= x + move[1] + more_move[1] < length:
                                            if not visited[y + move[0] + more_move[0]][x + move[1] + more_move[1]] and room[y + move[0] + more_move[0]][x + move[1] + more_move[1]] == 'P':
                                                raise Exception('2', roomnuber, y, x)

            answer.append(1)
        except Exception as e:
            # print(e)
            answer.append(0)
    
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))