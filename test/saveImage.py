from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image

import time

def savecode(driver):
	driver.get_screenshot_as_file('CrawlResult/screenshot.png')
	
	element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/form/div/ul[2]/li[4]/div/div/div[3]/img")))
	
	
	left = int(element.location['x'])
	top = int(element.location['y'])
	right = int(element.location['x'] + element.size['width'])
	bottom = int(element.location['y'] + element.size['height'])
	
	im = Image.open('CrawlResult/screenshot.png')
	im = im.crop((left, top, right, bottom))
	im.save('CrawlResult/code.png')
	





def main():
	driver = webdriver.Firefox()
	driver.get('https://kyfw.12306.cn/otn/login/init')
	#driver.quit()
	
	print('waiting')
	time.sleep(2)
	print('savecode')
	savecode(driver)
	
	'''
	action = ActionChains(driver).move_to_element(element)
	action.context_click(element)
	action.send_keys(Keys.ARROW_DOWN)
	action.send_keys('v')
	action.perform()
	'''
	
	
main()
