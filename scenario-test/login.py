# from ast import Assert
# from cgi import test
from selenium import webdriver
from time import sleep 
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import unittest
from selenium.webdriver.chrome.options import Options

#Get env var
chromdrv = os.getenv("CHROMEDRV")   #Path to chrmdrv
baseURL  = os.getenv('BASEURL')     #Path to URL

s = Service(chromdrv)
driver = webdriver.Chrome(service=s)

username = 'admin@example.com', 
password = 'verysecret'

def test_login():
    print('Log-in testing..')

    chrome_options = Options()
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-site-isolation-trials")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromdrv)

    url = baseURL + "/login"
    driver.get(url)
    driver.maximize_window()

    #Check the site
    # assert 'LCS' in driver.title
    # sleep(2)

    print('1')

    driver.find_element(By.ID, 'basic_email').send_keys(username)
    sleep(2)
    driver.find_element(By.ID, 'basic_password').send_keys(password)
    sleep(2)
    driver.find_element(By.ID, 'login').click()
    sleep(2)

    #Verify the login result:

    # try:
    #     element = WebDriverWait(driver, 3).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, ""))
    #     )
    # finally: 
    #     driver.quit()

    try:
     s1 = driver.find_element(By.ID, 'login')
     element = s1.text
     print('Element exist '+element)

    #NoSuchElementException thrown if not present
    except NoSuchElementException:

     print('Element does not exist')
     driver.close()

    #

    print('logout testing')
    url = baseURL
    driver.get(url)
    driver.maximize_window()

    account = driver.find_element(By.CLASS_NAME, 'ant-avatar ant-avatar-lg ant-avatar-circle ant-avatar-image ant-dropdown-trigger')
    logout_button = driver.find_element(By.CLASS_NAME, 'ant-dropdown ant-dropdown-show-arrow ant-dropdown-placement-bottomRight  ant-dropdown-hidden')

    actions = ActionChains(driver)
    actions.move_to_element(account).move_to_element(logout_button).click().perform()
    sleep(2)

    #Verify logout result
    try:
     s2 = driver.find_element(By.ID, 'basic_login')
     element = s2.text
     print('Element exist '+element)

    except NoSuchElementException:

     print('Element does not exist')
     driver.close()

    driver.close()

###

def test_logout(self):

    print('logout without login testing...')
    url = baseURL
    driver.get(url)
    driver.maximize_window()

    account = driver.find_element(By.XPATH, '/html/body/div[1]/section/header/div/div[2]/span[2]/img')
    logout_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/ul/li')

    actions = ActionChains(driver)
    actions.move_to_element(account).move_to_element(logout_button).click().perform()
    sleep(2)

    #Verify logout result
    try:
     s3 = driver.find_element(By.ID, 'basic_login')
     element = s3.text
     print('Element exist '+ element)

    except NoSuchElementException:
     print('Element does not exist')
     driver.close()
    
    driver.close()

###

def test_loginWait():
    print('Log-in testing with 120s wait..')

    url = baseURL + "/login"
    driver.get(url)
    driver.maximize_window()

    driver.find_element(By.NAME, 'email').send_keys(username)
    sleep(2)
    driver.find_element(By.NAME, 'password').send_keys(password)
    sleep(2)
    driver.find_element(By.ID, 'login').click()
    sleep(2)

    #Verify login 
    try:
     s4 = driver.find_element(By.ID, 'login')
     element = s4.text
     print('Element exist ' + element)

    #NoSuchElementException thrown if not present
    except NoSuchElementException:
     print('Element does not exist')
     driver.close()


    #Wait >120s for the session to expire
    try:
     sleep(130)
    except:
     print('System keeps living...')
        
     
 #

    print('expired logout testing')
    url = baseURL
    driver.get(url)
    driver.maximize_window()

    account = driver.find_element(By.CLASS_NAME, 'ant-avatar ant-avatar-lg ant-avatar-circle ant-avatar-image ant-dropdown-trigger')
    logout_button = driver.find_element(By.CLASS_NAME, 'ant-dropdown ant-dropdown-show-arrow ant-dropdown-placement-bottomRight  ant-dropdown-hidden')

    actions = ActionChains(driver)
    actions.move_to_element(account).move_to_element(logout_button).click().perform()
    sleep(2)

    #Verify logout result
    try:
     s3 = driver.find_element(By.ID, 'basic_login')
     element = s3.text
     print('Element exist '+ element)

    except NoSuchElementException:
     print('Element does not exist')
     driver.close()

    driver.close()



#


if __name__ == "__main__":
    from selenium.common.exceptions import NoSuchElementException

    try:
        test_login()
        test_logout()
        test_loginWait()
        
    except:
        print("Exception: unexpected error! Exit the test program... ")
        driver.quit()