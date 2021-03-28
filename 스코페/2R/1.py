import sys
# from datetime import time
from datetime import timedelta

N, time_str = sys.stdin.readline().rstrip().split()
N = int(N)
time_str = time_str.split(':')
total_time = timedelta(int(time_str[0]), int(time_str[1]), int(time_str[2]))
play = []

for _ in range(N):
	temp = sys.stdin.readline().rstrip().split(':')
	play.append(timedelta(0, int(temp[0]), int(temp[1])))

print('%%',play)
maximum = 0
start = 0
print('^^', total_time)
for i in range(N):
	cur = timedelta(0)
	j = i
	while True:
		# second = cur.second + play[j].second
		# minute = cur.minute + play[j].minute
		# hour = cur.hour + play[j].hour
		# if second > 60:
		# 	second %= 60
		# 	minute += 1
		# if minute > 60:
		# 	minute %= 60
		# 	hour += 1
		# print(hour, minute, second)
		cur = cur + play[j]
		# print('##', cur)
		j += 1
		if j >= len(play) or cur >= total_time:
			if j - i > maximum:
				maximum = j - i
				start = i
			break

print(maximum, start+1)