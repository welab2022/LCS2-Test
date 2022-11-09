"""
This module contains shared fixtures.
"""

import pytest
import time

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(autouse=True)
def browser():

  # Initialize the ChromeDriver instance
  b = selenium.webdriver.Chrome()
  
  b.maximize_window()

  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(10)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.close()
  b.quit() 
  
  
# This fixture opens the URL waits
# until a page is visible before proceeding.
@pytest.fixture()
def open_url(browser):
  browser.get("http://localhost:8080")


# This fixture enters the admin credential for the login
# @pytest.mark.usefixtures("open_url")
# @pytest.fixture()
# def enter_admin_credential(browser):
#   # open_url()
#   browser.find_element(By.ID, 'basic_email').send_keys("admin@example.com")
#   browser.find_element(By.ID, 'basic_password').send_keys("verysecret")
#   browser.find_element(By.ID, 'login').click()
#   time.sleep(3)