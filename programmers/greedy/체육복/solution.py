def solution(n, lost, reserve):
    answer = 0
    students = [1 for x in range(n)]

    for student_id in range(len(students)):
        if student_id+1 in reserve:
            students[student_id] += 1
        
        if student_id+1 in lost:
            students[student_id] -= 1
    print(students)
    for student_id in range(len(students)):
        if student_id != 0 and students[student_id] == 2 and students[student_id-1] == 0:
            students[student_id] -= 1
            students[student_id-1] += 1
        
        if student_id != len(students)-1 and students[student_id] == 2 and students[student_id+1] == 0:
            students[student_id] -= 1
            students[student_id+1] += 1
    
    print(students)
    for student in students:
        if student >= 1:
            answer += 1

    return answer