'''
1. n//3 만큼을 hand에 넣고 시작한다. 그 외에 추가되는 카드들은 additional에 넣는다.
1. 일단 추가로 들어오는 카드들 (코인으로 사는 카드들)을 additional에 추가한다.
    1-a. additional은 코인을 주고 사야하는 카드이다. 다만, 사용할지 말지 여부를 판단하기 어렵기 때문에, 일단 추가하고 사용할 때 코인을 차감하는 용도이다.
2. check함수를 통해 hand와 additional을 통틀어서 두 합이 n + 1이 되는 수가 있는지 확인한다. 두 값이 찾아질 경우 각 배열에서 두 값을 지우며, additional에서 값을 지우는 경우 그 개수만큼 coin을 차감한다.
3. 더 이상 카드를 낼 수 없을 때(hand 내부에서 카드를 낼 수 없을 때, 소비할 수 있는 coin이 없을 때) 까지의 answer를 리턴한다.
    3-a. answer는 for문을 반복한 횟수이다.
'''

def solution(coin, cards):
    n = len(cards)
    
    def check(cards1, cards2):
        for a in cards1:
            b = n + 1 - a
            if b in cards2:
                cards1.discard(a)
                cards2.discard(b)
                return True
        
        return False
                
    
    answer = 1
    top = n // 3
    hand = set(cards[:top])
    additional = set()

    for i in range(top, n, 2):
        additional.add(cards[i])
        additional.add(cards[i+1])
        
        if check(hand, hand):
            pass
        elif coin >= 1 and check(hand, additional):
            coin -= 1
        elif coin >= 2 and check(additional, additional):
            coin -= 2
        else:
            break
        answer += 1
            
    return answer