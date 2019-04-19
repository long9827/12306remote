from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def input(driver, passenger):
    driver.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc')

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
            # print('ok',times)
            break
            
    """输入目的地"""
    tse = driver.find_element_by_id('toStationText')
    ActionChains(driver).double_click(tse).send_keys(passenger.toStation).perform()
    times = 20
    while times>0:
        print(tse.get_attribute('value'))
        times = times - 1
        tse.send_keys(Keys.ARROW_DOWN)	#至少执行一次
        if tse.get_attribute('value') == passenger.toStation:
            # print('ok',times)
            break

    """选择出发日"""
    js1 = "document.getElementById('train_date').removeAttribute('readonly')"
    driver.execute_script(js1)
    train_date = driver.find_element_by_id('train_date')
    train_date.clear()
    train_date.send_keys(passenger.train_date)
    driver.find_element_by_id('query_ticket').click()