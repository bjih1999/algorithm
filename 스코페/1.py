# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from datetime import time

n = int(sys.stdin.readline().rstrip())

start = time(0, 00)
end = time(23, 59)
# print(start)
# print(end)
for _ in range(n):
	temp_time = sys.stdin.readline().rstrip().split('~')
	start_time = temp_time[0].split(':')
	temp = time(int(start_time[0]), int(start_time[1]))
	if start < temp:
		start = temp
	end_time = temp_time[1].split(':')
	temp = time(int(end_time[0]), int(end_time[1].rstrip()))
	if end > temp:
		end = temp

if end > start:
	print(start.strftime('%H:%M')+' ~ '+end.strftime('%H:%M'))
else:
	print(-1)