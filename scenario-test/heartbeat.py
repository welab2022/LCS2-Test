from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
import pytest
#from selenium.webdriver import ActionChains

s=Service('/usr/bin/chromedriver')
driver=webdriver.Chrome(service=s)
 
def test_heartbeat():
    url = 'http://localhost:8080/heartbeat'
    driver.get(url)
    driver.maximize_window()
    sleep(2)
    

def test_heartbeatWrong():
    url= 'http://localhost:8080/heartbeat1'
    driver.get(url)
    sleep(2)
   
   




