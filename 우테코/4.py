def solution(s):

    index = 0
    answer = []
    count = 1
    while index < len(s):
        if index == len(s)-1:
            if s[0] == s[-1]:
                answer.append(answer[0] + count)
                del answer[0]
            else:
                answer.append(count)
        else:
            if s[index] == s[index+1]:
                count += 1
            else:
                answer.append(count)
                count = 1
        index += 1
    return sorted(answer)

print(solution("aaabbaaa"))
print(solution("wowwow"))