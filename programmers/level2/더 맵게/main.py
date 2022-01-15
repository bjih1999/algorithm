import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1 and scoville[0] < K:
        
        first_mild = heapq.heappop(scoville)
        second_mild = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first_mild + second_mild * 2)
        count +=1 
    
    if scoville[0] < K:
        return -1
    return count