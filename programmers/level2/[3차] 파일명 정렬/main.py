import re

def solution(files):
    answer = []
    pattern = r"([a-zA-Z-\s]+)(\d+)([a-zA-Z0-9-\s.]*)"

    parsed_list = []
    for file in files:
        parsed = re.match(pattern, file)
        parsed_list.append(parsed.groups())
    
    sorted_files = sorted(parsed_list, key=lambda x: (x[0].lower(), int(x[1])))

    for file in sorted_files:
        answer.append(''.join(file))
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

