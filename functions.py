from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
#from time import sleep
from information import TrainInfo
from code import getCode
from code import clickCodes
import time

#登录
def login(driver, passenger):
	username = driver.find_element_by_id('username')
	username.clear()
	username.send_keys(passenger.username)
	password = driver.find_element_by_id('password')
	password.clear()
	password.send_keys(passenger.password)

	print('正在识别验证码...')
	times = 10
	loginBtn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"loginSub")))
	while loginBtn!=None and times>0:
		times = times - 1
		time.sleep(2)
		indexs = getCode(driver)
		clickCodes(indexs, driver)
		loginBtn.click()
		time.sleep(2)
		try:
			loginBtn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID,"loginSub")))
			#还能获取登陆按钮，验证码识别出错
		except:
			return
			
	
	#手动输入
	print("请手动输入验证码：")
	while loginBtn!=None:
		try:
			loginBtn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID,"loginSub")))
		except:
			return


#查询
def find(driver, passenger):
	if passenger.isSingle:
		"""单程"""
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"dc_label"))).click()
		#driver.find_element_by_id('dc_label').click()
	else:
		"""往返"""
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"wf_label"))).click()
		#driver.find_element_by_id('wf_label').click()
		
	"""输入出发地"""
	fse = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"fromStationText")))
	#driver.find_element_by_id('fromStationText')
	ActionChains(driver).double_click(fse).send_keys(passenger.fromStation).perform()
	times = 20
	while times>0:
		print(fse.get_attribute('value'))
		times = times - 1
		fse.send_keys(Keys.ARROW_DOWN)	#至少执行一次
		if fse.get_attribute('value') == passenger.fromStation:
			print('ok',times)
			break;
			
	"""输入目的地"""
	tse = driver.find_element_by_id('toStationText')
	ActionChains(driver).double_click(tse).send_keys(passenger.toStation).perform()
	times = 20
	while times>0:
		print(tse.get_attribute('value'))
		times = times - 1
		tse.send_keys(Keys.ARROW_DOWN)	#至少执行一次
		if tse.get_attribute('value') == passenger.toStation:
			print('ok',times)
			break;
			
	"""选择出发日"""
	js1 = "document.getElementById('train_date').removeAttribute('readonly')"
	driver.execute_script(js1)
	train_date = driver.find_element_by_id('train_date')
	train_date.clear()
	train_date.send_keys(passenger.train_date)
	driver.find_element_by_id('query_ticket').click()
	#if passenger.isSingle:

#筛选并选择
def select(driver, passenger):
	#tbody = driver.find_element_by_id('queryLeftTable')
	#rows = tbody.find_element_by_tag_name('tr')
	#print(rows.iterkeys())
	#print(rows)
	#for row in rows:
		#print(row.find_element_by_class_name('train').text())
	#test = tbody.find_element_by_xpath('//tr[1]/td[1]/div/div[4]/strong')
	#print(test.get_attribute('innerHTML'))
	#rows = tbody.find_element_by_tag_name('tr')
	#print(rows)
	tbodyXpath = '/html/body/div[6]/div[7]/table/tbody'
	trainsInfo = []
	time = 5
	while time > 0:
		
		for i in range(1, 1000, 2):
			#s = '//tr[' + str(i) + ']/td[1]/div/div[3]/strong[1]'
			#print(s)
			#test = tbody.find_element_by_xpath(s)
			#print(i,test.get_attribute('innerHTML'))
			#rowCount = tbody.find_element_by_xpath("//tr").__sizeof__()
			#print(rowCount)
			
			#print(row.find_element_by_xpath('//td[1]/div/div[3]/strong[1]').get_attribute('innerHTML'))
			try:
				tmp = TrainInfo(driver, tbodyXpath, i)
				if tmp.hasTicket:
					trainsInfo.append(tmp)
				time = -1
			except NoSuchElementException:
				break
				
	#for t in trainsInfo:
		#t.printInfo()

	#查找乘客所需车次是否有余票，若有多个返回第一个
	checis = passenger.checis
	train = None
	for checi in checis:
		for t in trainsInfo:
			if checi == t.checi:
				train = t
				break
		if train:
			break
	'''
	if train:
		#已查到
		train.printInfo()
	else:
		print('未找到')
	'''
	return train
			
	
	
	
	#for t in trainsInfo:
		#t.printInfo()
	
	#trainsInfo[0].ydbtn.click()
		
		
		
		
		
		
		
		
		
