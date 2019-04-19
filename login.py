from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from code import getCode
from code import clickCodes


import time

def login(driver, passenger) :
    driver.get('https://kyfw.12306.cn/otn/login/init')
    try:
        # 输入用户名 
        username = driver.find_element_by_id('username')
        username.clear()
        username.send_keys(passenger.username)
        # 输入密码
        password = driver.find_element_by_id('password')
        password.clear()
        password.send_keys(passenger.password)
    except:
        # 找不到元素，已经登录
        return

    print('正在识别验证码...')
    times = 10 # 自动识别最大次数
    loginBtn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"loginSub")))   # 获取登录btn
    while loginBtn!=None and times>0:
        times = times - 1
        time.sleep(2)
        try:
            indexs = getCode(driver)
            clickCodes(indexs, driver)
        except:
            print('API Error！')
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

