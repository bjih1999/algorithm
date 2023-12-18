import sys
result = []
temp = []
while True:
    sent = sys.stdin.readline().rstrip()
    temp.append(sent)
    if sent == '.':
        break
    stack = []
    is_valid = True
    for letter in sent:
        if letter == '(' or letter == '[':
            stack.append(letter)
        elif letter == ')':
            if not stack or stack[-1] != '(':
                is_valid = False
                break
            stack.pop()
        elif letter == ']':
            if not stack or stack[-1] != '[':
                is_valid = False
                break
            stack.pop()
    if stack:
        is_valid = False

    answer = 'yes' if is_valid else 'no'
    result.append(answer)

for index, r in enumerate(result):
    # print(temp[index])
    print(r)