import copy

def solution(info, query):
    answer = []

    people = []
    for person in info:
        person_info = person.split()
        people.append([person_info[0], person_info[1], person_info[2], person_info[3], int(person_info[4])])
    
    for q in query:
        condition = q.split()
        condition = [condition[0], condition[2], condition[4], condition[6], int(condition[7])]
        answer.append(len(where(copy.deepcopy(people), condition)))
        
        
    return answer

def where(people, condition):
    
    for index, target in enumerate(condition[:-1]):
        if target != "-":
            people = list(filter(lambda x:x[index] == target, people))
    
    return list(filter(lambda x:x[4] >= condition[4], people))  