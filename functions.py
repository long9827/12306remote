from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

#登录
def login(driver, passenger):
	username = driver.find_element_by_id('username')
	username.clear()
	username.send_keys(passenger.username)
	password = driver.find_element_by_id('password')
	password.clear()
	password.send_keys(passenger.password)

	print('正在输入验证码...')
	#手动输入
	WebDriverWait(driver, 100).until(EC.title_is('我的12306 | 客运服务 | 铁路客户服务中心'))
	print('登陆成功')

#查询
def find(driver, passenger):
	if passenger.isSingle:
		"""单程"""
		driver.find_element_by_id('dc_label').click()
	else:
		"""往返"""
		driver.find_element_by_id('wf_label').click()
		
	"""输入出发地"""
	fse = driver.find_element_by_id('fromStationText')
	fse.clear()
	fse.send_keys(passenger.fromStation)
	times = 10
	while times>0:
		times = times - 1
		fse.send_keys(Keys.ARROW_DOWN)
		if fse.get_attribute('value') == passenger.fromStation:
			print('ok',times)
			break;
			
	"""输入目的地"""
	tse = driver.find_element_by_id('toStationText')
	tse.clear()
	tse.send_keys(passenger.toStation)
	times = 10
	while times>0:
		times = times - 1
		tse.send_keys(Keys.ARROW_DOWN)
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





