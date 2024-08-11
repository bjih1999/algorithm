'''
각각을 정렬하여 일치하는지 확인하기
'''
def solution(want, number, discount):
    answer = 0
    wishlist = []
    
    for product, count in zip(want, number):
        wishlist.extend([product] * count)
    
    wishlist = sorted(wishlist)
    
    n = len(discount)
    for i in range(n-9):
        candidate = discount[i:i+10]
        candidate = sorted(candidate)
        if wishlist == candidate:
            answer += 1
    return answer