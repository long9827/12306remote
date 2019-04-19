import datetime

def until():
    buyTime = '2018-12-29 09:57:59'
    while True:
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(nowTime)
        if nowTime>buyTime:
            break

if __name__ == "__main__":
    until()