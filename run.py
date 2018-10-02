from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from information import Passenger
from information import TrainInfo
from functions import *


def main():
	driver = webdriver.Firefox()
	driver.get('https://kyfw.12306.cn/otn/login/init')
	
	passenger = Passenger()
	
	login(driver, passenger)
	
	#跳转到车票预定界面
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"selectYuding"))).click()
	
	find(driver, passenger)
	
	train = select(driver, passenger)
	
	if train:
		#已查到
		train.printInfo()
		print('预定')
		train.ydbtn.click()
		WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID,"normalPassenger_0"))).click()
		driver.find_element_by_id('submitOrder_id').click()
		
		
	else:
		print('未找到合适的票')
	
main()
