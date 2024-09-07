from datetime import datetime, timedelta


'''
단순 구현
datetime의 사용법과 format의 사용법 숙지하기

'''
def solution(video_len, pos, op_start, op_end, commands):
    video_end_minute, video_end_second = list(map(int, video_len.split(':')))
    video_start = datetime(2024, 1, 1, minute=0, second=0)
    video_end = datetime(2024, 1, 1, minute=video_end_minute, second=video_end_second)
    
    current_minute, current_second = list(map(int, pos.split(':')))
    current = datetime(2024, 1, 1, minute=current_minute, second=current_second)
    
    op_start_minute, op_start_second = list(map(int, op_start.split(':')))
    op_end_minute, op_end_second = list(map(int, op_end.split(':')))
    op_start = datetime(2024, 1, 1, minute=op_start_minute, second=op_start_second)
    op_end = datetime(2024, 1, 1, minute=op_end_minute, second=op_end_second)
    
    if op_start <= current <= op_end:
            current = datetime(2024, 1, 1, minute=op_end_minute, second=op_end_second)
            
    for command in commands:        
        if command == 'next':
            current = min(current + timedelta(seconds=10), video_end)
        elif command == 'prev':
            current = max(current - timedelta(seconds=10), video_start)
        
        if op_start <= current <= op_end:
            current = datetime(2024, 1, 1, minute=op_end_minute, second=op_end_second)
    return "{0:02d}:{1:02d}".format(current.minute, current.second)