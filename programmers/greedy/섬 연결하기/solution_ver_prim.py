import heapq

def solution(n, costs):
	total_cost = 0
	visited=set()
	heap = []

	for bridge in costs:
		heapq.heappush(heap, (bridge[2], bridge[0], bridge[1]))

	visited.add(0)
	while len(heap) > 0:	# 모든 edge의 개수만큼 반복 -> 최악의 경우 E번 반복	따라서 O(E logV)
		bridge = heapq.heappop(heap)	# 힙에 다 들어가봤자 V개의 정점 -> 높이는 log V
		if (bridge[1] in visited) and (bridge[2] not in visited):
			visited.add(bridge[2])
			total_cost += bridge[0]
			for new_near_bridge in costs:
				if bridge[2] == new_near_bridge[0] or bridge[2] == new_near_bridge[1]:
					heapq.heappush(heap, (new_near_bridge[2], new_near_bridge[0], new_near_bridge[1]))
		
		elif (bridge[2] in visited) and (bridge[1] not in visited):
			visited.add(bridge[1])
			total_cost += bridge[0]
			for new_near_bridge in costs:
				if bridge[1] == new_near_bridge[0] or bridge[1] == new_near_bridge[1]:
					heapq.heappush(heap, (new_near_bridge[2], new_near_bridge[0], new_near_bridge[1]))
	
	return total_cost