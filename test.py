from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from information import Passenger
from functions import *


def main():
	driver = webdriver.Firefox()
	driver.get('file:///E:/code/Repos/12306/%E8%BD%A6%E7%A5%A8%E9%A2%84%E8%AE%A2%20%20%20%E5%AE%A2%E8%BF%90%E6%9C%8D%E5%8A%A1%20%20%20%E9%93%81%E8%B7%AF%E5%AE%A2%E6%88%B7%E6%9C%8D%E5%8A%A1%E4%B8%AD%E5%BF%83.html')
	
	passenger = Passenger()
	
	#login(driver, passenger)
	
	#跳转到车票预定界面
	#driver.find_element_by_id('selectYuding').click()
	
	#find(driver, passenger)
	
	select(driver, passenger).printInfo()
	'''
	xpath = '/html/body/div[6]/div[7]/table/tbody/tr[1]/td[2]'
	ele = driver.find_element_by_xpath(xpath)
	print(ele.get_attribute('innerHTML'))
	'''

main()
