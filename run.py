from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from information import Passenger
from functions import *


def main():
	driver = webdriver.Firefox()
	driver.get('https://kyfw.12306.cn/otn/login/init')
	
	passenger = Passenger()
	
	login(driver, passenger)
	
	#跳转到车票预定界面
	driver.find_element_by_id('selectYuding').click()
	
	find(driver, passenger)
	
	select(driver, passenger)

main()
