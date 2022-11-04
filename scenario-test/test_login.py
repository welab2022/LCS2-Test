from selenium import webdriver
from time import sleep 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os 
from selenium.webdriver.chrome.options import Options

#Get env var
chromdrv = os.getenv("CHROMEDRV")   #Path to chrmdrv
baseURL  = os.getenv('BASEURL')     #Path to URL

s = Service(chromdrv)
driver = webdriver.Chrome(service=s)

username = 'admin@example.com', 
password = 'verysecret'

def test_login():
    print('----Log-in testing-----')

    chrome_options = Options()
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-site-isolation-trials")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromdrv)

    url = baseURL + "/login"
    driver.get(url)
    driver.maximize_window()

    driver.find_element(By.ID, 'basic_email').send_keys(username)
    sleep(2)
    driver.find_element(By.ID, 'basic_password').send_keys(password)
    sleep(2)
    driver.find_element(By.ID, 'login').click()
    sleep(2)

    try:
     s1 = driver.find_element(By.ID, 'login')
     element = s1.text
     print('Element exist '+ element)
    #NoSuchElementException thrown if not present
    except NoSuchElementException:
     print('Element does not exist')
     driver.close()

    page_title = driver.title
    assert 'LCS' in page_title
    driver.save_screenshot("image_login.png")

    print('----logout testing:----')
    actions = ActionChains(driver)

    account = driver.find_element(By.ID, 'login')
    actions.move_to_element(account)
    actions.perform()
    
    logout_button = driver.find_element(By.CLASS_NAME, 'ant-dropdown-menu-title-content')
    actions.move_to_element(logout_button)
    actions.perform()

    actions.click()
    actions.perform()
    sleep(2)

    #Verify logout result
    try:
     s2 = driver.find_element(By.ID, 'basic_email')
     element = s2.text
     print('Element exist '+element)
    except NoSuchElementException:
     print('Element does not exist')
     driver.close()    
    sleep(2)
    
    assert baseURL+"/login" in driver.current_url
    driver.save_screenshot("image_logout.png")
    driver.close()
###

def test_logout():

    print('logout without login testing...')

    url = baseURL 
    driver.get(url)
    driver.maximize_window()

    actions = ActionChains(driver)

    account = driver.find_element(By.ID, 'login')
    actions.move_to_element(account)
    actions.perform()
    sleep(2)

    logout_button = driver.find_element(By.CLASS_NAME, 'ant-dropdown-menu-title-content')
    actions.move_to_element(logout_button)
    actions.perform()

    actions.click()
    actions.perform()
    sleep(2)
    print('1')
    #Verify logout result
    try:
     s3 = driver.find_element(By.ID, 'basic_email')
     element = s3.text
     print('Element exist '+element)
    except NoSuchElementException:
     print('Element does not exist')
     driver.close()
    
    page_title = driver.title
    assert 'LCS' in page_title
    driver.save_screenshot("image_logout2.png")
    driver.close()
###

def test_loginWait():
    print('Log-in testing with 120s wait..')

    chrome_options = Options()
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-site-isolation-trials")

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromdrv)

    url = baseURL + "/login"
    driver.get(url)
    driver.maximize_window()

    driver.find_element(By.ID, 'basic_email').send_keys(username)
    sleep(2)
    driver.find_element(By.ID, 'basic_password').send_keys(password)
    sleep(2)
    driver.find_element(By.ID, 'login').click()
    sleep(2)

    #Verify login result
    try:
     s1 = driver.find_element(By.ID, 'login')
     element = s1.text
     print('Element exist '+element)
    #NoSuchElementException thrown if not present
    except NoSuchElementException:
     print('Element does not exist')
     driver.close()

    #Wait >120s for the session to expire
    try:
     sleep(130)
     driver.refresh()
     print('System shutdown....')
     driver.save_screenshot("image_login120s.png")
    except:
     print('----System keeps on living----')
     driver.close()
    
    print('Session expired -> Logout')
    driver.close()

#

if __name__ == "__main__":
    from selenium.common.exceptions import NoSuchElementException

    try:
        test_login()
        # test_logout()
        test_loginWait()
    except:
        print("Exception: unexpected error! Exit the test program... ")
        driver.quit()