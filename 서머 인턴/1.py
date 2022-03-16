from datetime import date, datetime

def solution(code, day, data):
    answer = []
    
    stockData = []
    # print(day[:4])
    # print(day[4:6])
    # print(day[6:])
    day = datetime(int(day[:4]), int(day[4:6]), int(day[6:]))
    for stock in data:
        stockInfo = stock.split()
        price = stockInfo[0].split('=')[1]
        code = stockInfo[1].split('=')[1]
        time = stockInfo[2].split('=')[1]
        time = datetime(int(time[:4]), int(time[4:6]), int(time[6:8]), int(time[8:]))
        stockData.append((price, code, time))

    # print(stockData)
    dataForCompany = []

    for info in stockData:

        if info[1] == code and info[2].date() == day.date():
            # print(info[1])
            dataForCompany.append(info)
    
    dataForCompany = sorted(dataForCompany, key=lambda x: (x[2].time()))
    # print(dataForCompany[0][2].time())
    for info in dataForCompany:
        answer.append(int(info[0]))
    return answer

print(solution("012345", "20190620"	, ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]	))