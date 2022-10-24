from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

import pytest
import os
#from selenium.webdriver import ActionChains

# Get environment variables
chromdrv = os.getenv('CHROMEDRV') # path to chromedrv
baseURL = os.getenv('BASEURL') # path to chromedrv

# s=Service('/usr/bin/chromedriver')
s=Service(chromdrv)
driver=webdriver.Chrome(service=s)
 
def test_heartbeat():
    print("starting test heartbeat...")
    url = baseURL + "/heartbeat"
    driver.get(url)
    driver.maximize_window()
    sleep(2)

    # check if the expected result equals the actual
    # ...
    
    # close browser
    driver.quit()
    

def test_heartbeatWrong():
    print ("start test heartbeat with wrong url...")
    url = baseURL + "/heartbeat"
    driver.get(url)
    sleep(2)
    
    # check if the expected result equals the actual
    # ...
    
    # close browser
    driver.quit()
   
   
if __name__ == "__main__":
    from selenium.common.exceptions import NoSuchElementException

    try:
        test_heartbeat()
        test_heartbeatWrong()
    except:
        print("Exception: unexpected error! Exit the test program... ")
        driver.quit()

    



