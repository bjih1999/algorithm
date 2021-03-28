import sys

N = int(sys.stdin.readline().rstrip())

# network = {}
# for _ in range(N):
# 	var = sys.stdin.readline().rstrip().split()
# 	if var[0] not in network:
# 		network[var[0]] = [(var[1], int(var[2]))]
# 	else:
# 		network[var[0]].append((var[1], int(var[2])))
	
# 	if var[1] not in network:
# 		network[var[1]] = [(var[2], int(var[2]))]
# 	else:
# 		network[var[1]].append((var[0], int(var[2])))
	
# links = network.items()

# print(links)

network = []
worlds = set()
for _ in range(N):
	link = sys.stdin.readline().rstrip().split()
	network.append((link[0], link[1], int(link[2])))
	worlds.add(link[0])
	worlds.add(link[1])
sorted_link = sorted(network, key=lambda x:x[2])

id_set = {}
for world in worlds:
	id_set[world] = world

resource = 0
for link in sorted_link:
	node1 = link[0]
	while id_set[node1] != node1:
		node1 = id_set[node1]
	node2 = link[1]
	while id_set[node2] != node2:
		node2 = id_set[node2]
	
	if id_set[node1] != id_set[node2]:
		id_set[node2] = id_set[node1]
			
		resource += link[2]

print(resource)

# seoul beijing 3
# beijing hawaii 10
# seoul tokyo 5
# seoul hawaii 6
# tokyo hawaii 4
# beijing tokyo 5