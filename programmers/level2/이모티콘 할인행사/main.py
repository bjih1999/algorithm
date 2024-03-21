from copy import deepcopy

sales = [10, 20 , 30 , 40]
users = []
emoticons = []
m = 0
n = 0
count = 0
price = 0
temp = []
def func(percent, i):
    global count, price, users, n
    if i == m:
        join = 0
        paid_list = {i:0 for i in range(n)}
        for cur, p in enumerate(percent[:m]):
            for index in range(n):
                if users[index][0] <= p:
                    paid_list[index] += int(emoticons[cur] * ((100 - p) / 100))
        
        cur_price = 0
        for index, paid in enumerate(paid_list.items()):
            if paid[1] >= users[index][1]:
                paid_list[index] = 0
                join += 1
            
            cur_price += paid_list[index]
                  
        if join > count:
            count = join
            price = cur_price
        
        elif join == count and cur_price >= price:
            count = join
            price = cur_price
        return
    
    for sale in sales:
        next_percent = deepcopy(percent)
        next_percent[i] = sale
        func(next_percent, i+1)
        
    
def solution(_users, _emoticons):
    global users, emoticons, m, n, count, price, temp
    users = _users
    emoticons = _emoticons
    m = len(emoticons)
    n = len(users)
    
    percent = [0 for _ in range(m+2)]
    i = 0
    
    func(percent, i)
    return [count, price]


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))