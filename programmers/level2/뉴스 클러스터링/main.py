def solution(str1, str2):
    set1 = set()
    set2 = set()
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1)-1):
        target = str1[i:i+2]
        if target.isalpha():
            set1.add(target)
    
    for i in range(len(str2)-1):
        target = str2[i:i+2]
        if target.isalpha():
            set2.add(target)
            
    if (len(set1) == 0 and len(set2) == 0):
        return 1*65536
            
    union_size = len(set1.union(set2))
    intersection_size = len(set1.intersection(set2))
    return (intersection_size/union_size) * 65536