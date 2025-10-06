'''
1. 모든 start_date, end_date를 초 단위로 변환함.
2. total_times[i]를 i초에 시작한 광고, i초에 끝난 광고의 합으로 정의함
    2-a. 영상의 길이는 최대 99분 59초 59분이기때문에, 배열의 길이는 최대 360000임.
3. for 1..play_time : total_times[i] = total_times[i] + total_times[i-1] -> i초에 동시에 시청하는 유저 수
4. 위 연산을 한번 더 수행함 -> 0초부터 i초 까지의 누적 시청시간
5. for adv_time-1...playtime : maximum = total_times[i] - total_times[i-adv_time]

'''

from datetime import timedelta

def solution(play_time, adv_time, logs):
    max_time =  int(timedelta(hours=99, minutes=59, seconds=59).total_seconds() + 1)
    total_times = [0] * max_time
    play_h, play_m, play_s = list(map(int, play_time.split(':')))
    play_time = int(timedelta(hours=play_h, minutes=play_m, seconds=play_s).total_seconds())
    adv_h, adv_m, adv_s = list(map(int, adv_time.split(':')))
    adv_time = int(timedelta(hours=adv_h, minutes=adv_m, seconds=adv_s).total_seconds())
    
    for log in logs:
        start, end = log.split('-')
        start_h, start_m, start_s = list(map(int, start.split(':')))
        end_h, end_m, end_s = list(map(int, end.split(':')))
        start_time = int(timedelta(hours=start_h, minutes=start_m, seconds=start_s).total_seconds())
        end_time = int(timedelta(hours=end_h, minutes=end_m, seconds=end_s).total_seconds())
        
        total_times[start_time] += 1
        total_times[end_time] -= 1
    for i in range(1, play_time):
        total_times[i] = total_times[i] + total_times[i-1]
    for i in range(1, play_time):
        total_times[i] = total_times[i] + total_times[i-1]
    maximum = 0
    result = '00:00:00'
    for i in range(adv_time-1, play_time):
        current = total_times[i] - total_times[i - adv_time]
        current_start = i - adv_time
        if current > maximum:
            maximum = current
            hours = current_start // 3600
            minutes = (current_start - hours * 3600) // 60
            seconds = current_start % 60
            result = '{0:0>2}:{1:0>2}:{2:0>2}'.format(hours, minutes, seconds)
    
    return result