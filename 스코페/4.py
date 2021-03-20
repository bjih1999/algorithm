import sys

prefer = list(map(float, sys.stdin.readline().rstrip().split(' ')))
N, M = list(map(int, sys.stdin.readline().rstrip().split(' ')))

prefer_dict = {
	'A':prefer[0],
	'B':prefer[1],
	'C':prefer[2],
	'D':prefer[3],
	'E':prefer[4]
	}

order = {
	'Y':0,
	'O':1,
	'W':2
}
watch = []
locations = []
for i in range(N):
	line = list(sys.stdin.readline().rstrip())
	for pos, letter in enumerate(line):
		watch.extend(letter)
		locations.append((i, pos))
# print(watch)
# print(locations)
genre = []
for _ in range(N):
	line = list(sys.stdin.readline().rstrip())
	genre.extend(line)

contents = []
for i in range(len(watch)):
	if watch[i] != 'W':
		contents.append((genre[i], prefer_dict[genre[i]], locations[i], watch[i]))

# print(contents)

recommands = sorted(contents, key=lambda x:(order[x[3]], -x[1]))
for recomand in recommands:
	print(recomand[0], recomand[1], recomand[2][0], recomand[2][1])