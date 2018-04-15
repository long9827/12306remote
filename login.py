from selenium import webdriver


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://kyfw.12306.cn/otn/login/init')

username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')

username.send_keys('17702729698')
password.send_keys('long9827')

print('正在输入验证码...')
WebDriverWait(driver, 100).until(EC.title_is('我的12306 | 客运服务 | 铁路客户服务中心'))
print('登陆成功')
