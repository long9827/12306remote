from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from info import Passenger
from login import login
from input import input
from find import find
from verify import verify
from until import until
from smtp import sendmail

import time

if __name__ == "__main__":
    until()
    driver = webdriver.Firefox()    
    passenger = Passenger()

    while True:
        try:
            login(driver, passenger)

            
            if verify(driver):
                sendmail()
                break
            input(driver, passenger)
    
            train = find(driver, passenger)
            if train:
                #有票
                # train.printInfo()
                # print('预定')
                train.ydbtn.click()
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID,"normalPassenger_0"))).click()   # 乘客1
                # WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID,"normalPassenger_1"))).click() # 乘客2
                # WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID,"normalPassenger_2"))).click() # 乘客3
                driver.find_element_by_id('submitOrder_id').click()
                print('确定')
                confirm = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID,"qr_submit_id")))
                time.sleep(2)
                confirm.click()
                # print('已确定')
                
            else:
                print('未找到合适的票')
        except:
            print('error')