import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('^[0-9a-z-_.]','', new_id)
    new_id = re.sub('\.+', '.', new_id)
    if new_id[0] == '.':
        if len(new_id) == 1:
            new_id = ''
        else:
            new_id = new_id[1:]
    
    if new_id[-1] == '.':
        if len(new_id) == 1:
            new_id = ''
        else:
            new_id = new_id[:-1]
    
    if not new_id:
        new_id = 'a'
        
    if len(new_id) >= 16:
        new_id = new_id [:16]
    
    if new_id[-1] == '.':
        if len(new_id) == 1:
            new_id = ''
        else:
            new_id = new_id[:-1]
    
    new_id_length = len(new_id)
    i = 0
    while len(new_id) <= 2:
        new_id += new_id[i % new_id_length]
        i += 1
    
    return new_id