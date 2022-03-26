def solution(n, words):
    answer = []
    previous = []
    count = [0 for _ in range(len(words))]
    turn = 0
    is_game_set = False
    for index, word in enumerate(words):
        turn = index%n
        count[turn] += 1
        if word in previous or (previous and previous[-1][-1] != word[0]):
            is_game_set = True
            break
        previous.append(word)
    if is_game_set:
        return [turn+1, count[turn]]
    return [0, 0]