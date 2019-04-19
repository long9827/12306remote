from selenium.common.exceptions import NoSuchElementException

from TrainInfo import TrainInfo

# 查找
def find(driver, passenger):
    tbodyXpath = '/html/body/div[7]/div[7]/table/tbody'
    # trainsInfo = []
    checi = passenger.checi
    time = 20
    while time > 0:     # while循环等待网页加载完成
        time = time-1
        for i in range(1, 1000, 2):
            # print(checi, i)
            try:
                tmp = TrainInfo(driver, tbodyXpath, i)
                time = -1
                if tmp.checi == checi:
                    if tmp.hasTicket:
                        # print('hasTicket')
                        return tmp
                    else:
                        return None
                    # trainsInfo.append(tmp)
            except NoSuchElementException:
                print('NoSuchElementException')
                break
    return None

	#查找乘客所需车次是否有余票，若有多个返回第一个
	# checis = passenger.checis
	# train = None
	# for checi in checis:
	# 	for t in trainsInfo:
	# 		if checi == t.checi:
	# 			train = t
	# 			break
	# 	if train:
	# 		break
	# return train