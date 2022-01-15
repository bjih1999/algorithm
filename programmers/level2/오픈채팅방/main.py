def solution(record):
    
    uid_name = {}
    log = []
    result = []
    for action in record:
        inst = action.split()
        
        if inst[0] == "Change":
            uid_name[inst[1]] = inst[2] 
        elif inst[0] == "Enter":
            uid_name[inst[1]] = inst[2]
            log.append([inst[1], '���� ���Խ��ϴ�.'])
        elif inst[0] == 'Leave':
            log.append([inst[1], '���� �������ϴ�.'])
    
    for line in log:
        result.append(uid_name[line[0]] + line[1])
    
    
    return result