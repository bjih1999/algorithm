import datetime
def solution(time, plans):
    answer = '호치민'

    go_home = datetime.datetime(1900, 1, 1, 18)
    go_company = datetime.datetime(1900, 1, 1, 13)
    # print(go_home)
    # print(go_company)
    # print()

    if time % 1 == 0.0:
        remaining_time = datetime.timedelta(hours=time)
    else:
        remaining_time = datetime.timedelta(hours=time//1, minutes=30)
    # print(remaining_time)
    # print()
    for plan in plans:
        dest, start, end = plan
        start = datetime.datetime.strptime(start, "%I%p")
        end = datetime.datetime.strptime(end, "%I%p")
        # print(start)
        # print(end)

        if start < go_home:
            remaining_time -= (go_home - start)
        # print(remaining_time, "?")
        if go_company < end:
            remaining_time -= (end - go_company)
        # print(remaining_time, "?")
        if remaining_time < datetime.timedelta():
            break
        answer = dest


    
    return answer

print(solution(3.5, [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]))