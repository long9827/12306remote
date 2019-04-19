from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from smtp import sendmail
from info import Passenger
from login import login

def verify(driver):
    driver.get('https://kyfw.12306.cn/otn/view/train_order.html')
    try:
        countdown0 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID,"countdown0"))) 
        if countdown0:
            print('ok')
            # sendmail()
            return True
        else:
            return False
    except:
        return False

if __name__ == "__main__":
    driver = webdriver.Firefox()    
    passenger = Passenger()
    while True:
        try:
            login(driver, passenger)
            if verify(driver):
                break
        except:
            print('error')