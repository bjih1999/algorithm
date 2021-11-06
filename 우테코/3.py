def solution(ings, menu, sell):
    parsed_ings = {}
    parsed_menu = {}

    for ing in ings:
        name, price = ing.split()
        parsed_ings[name] = int(price)
    
    for menu_info in menu:
        name, ingredients, price = menu_info.split()
        base_price = 0
        for ingredient in ingredients:
            base_price += parsed_ings[ingredient]
        parsed_menu[name] = int(price) - base_price
    
    result = 0
    for order in sell:
        name, count = order.split()
        result += parsed_menu[name] * int(count)
    return result

print(solution(["r 10", "a 23", "t 124", "k 9"], ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))
print(solution(["x 25", "y 20", "z 1000"], ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"], ["BBBB 3", "TTT 2"]))
