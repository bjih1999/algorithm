# -*- coding: utf-8 -*-
import datetime

def solution(log):
    index = 0
    set_log = []
    total = datetime.timedelta()

    MINIMUM_TIME = datetime.timedelta(minutes=5)
    MAXIMUM_TIME = datetime.timedelta(minutes=105)
    while index < len(log):
        if index % 2 == 0 :
            set_log.append((log[index], log[index+1]))
            index += 2

    for interval in set_log:
        start = datetime.datetime.strptime(interval[0], "%H:%M")
        end = datetime.datetime.strptime(interval[1], "%H:%M")
        study_time = end-start
        # print(study_time)
        if study_time >= MAXIMUM_TIME:
            total += MAXIMUM_TIME
        elif MINIMUM_TIME <= study_time:
            total += study_time
        # print(total)
    time_str = str(total).split(":")
    # print(time_str)
    return '{:02d}:{:02d}'.format(int(time_str[0]), int(time_str[1]))

print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))
print(solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]))
