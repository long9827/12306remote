from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


from information import Passenger
from information import TrainInfo
from functions import *
from code import getCode
from code import clickCodes


def main():
	driver = webdriver.Firefox()
	driver.get('https://kyfw.12306.cn/otn/login/init')
	
	time.sleep(1)
	
	loginBtn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID,"loginSub")))
	print('1: ', login==None)
	
	driver.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc')
	print('start\n')
	loginBtn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID,"loginSub")))
	print('1: ', login==None)
	
	#print(getCode(driver))
	'''
	codeImage = driver.find_element_by_xpath('/html/body/div[6]/div/form/div/ul[2]/li[4]/div/div/div[3]/img')
	actions = ActionChains(driver)
	actions.move_to_element_with_offset(codeImage, 38, 74).click().perform()
	'''
	#indexs = getCode(driver)
	#clickCodes(indexs, driver)
	print(driver.title != '登录 | 客运服务 | 铁路客户服务中心')
	
main()
