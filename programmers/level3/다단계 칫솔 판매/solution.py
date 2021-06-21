def solution(enroll, referral, seller, amount):
    
    money = {}
    refers = {}
    for name, refer in zip(enroll, referral):
        money[name] = 0
        refers[name] = refer

    for name, count in zip(seller, amount):

        refer = refers[name]
        garantee = count * 100
        money[name] += garantee
        while garantee // 10 >= 1:
            money[name] -= garantee // 10
            if refer == "-":
                break
            money[refer] += garantee // 10
            garantee = garantee // 10
            name = refer
            refer = refers[name]
    
    return list(money.values())

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	, ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	, ["sam", "emily", "jaimie", "edward"]	, [2, 3, 5, 4]	))