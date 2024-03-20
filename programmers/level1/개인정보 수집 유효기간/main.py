from dateutil.parser import parse

def solution(today, terms, privacies):
    term_info = {}
    today = parse(today)
    y1 = today.year
    m1 = today.month
    d1 = today.day
    
    answer = []
    temp = []
    for term in terms:
        a, b = term.split()
        
        term_info[a] = int(b)
        
    for i, p in enumerate(privacies):
        d, type = p.split()
        d = parse(d)
        
        y2 = d.year
        m2 = d.month
        d2 = d.day
        
        y0 = y1 - y2
        m0 = m1 - m2
        d0 = d1 - d2
        
        if (d0 < 0):
            m0 -= 1
            d0 = 28 + d0
        
        if (m0 < 0):
            y0 -= 1
            m0 += 12
        
        
        diff = y0 * 12 * 28 + m0 * 28 + d0
        # temp.append((diff, term_info[type] * 28))
        if diff >= term_info[type] * 28:
            answer.append(i+1)
            
    return answer