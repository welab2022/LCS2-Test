#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
These tests open browser.
"""
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# This test will run when 'login_test' is called when invoking -m,
# e.g. 'pytest test_custom_markers.py -m "login_test"'.
# This test will run when 'empty_form_test' is called when invoking -m,
# e.g. 'pytest test_custom_markers.py -m "empty_form_test"'.
# @pytest.mark.login_test
# @pytest.mark.empty_form_test
@pytest.mark.usefixtures("open_url")
def test_empty_login_form(browser):
    assert browser.find_element(By.ID, 'basic_email').get_attribute("value") == ""
    assert browser.find_element(By.ID, 'basic_password').get_attribute("value") == ""
    browser.save_screenshot('./screenhots/test_empty_login_form.png')

@pytest.mark.usefixtures("open_url")
def test_login_with_valid_credential(browser):
    browser.find_element(By.ID, 'basic_email').send_keys("admin@example.com")
    browser.find_element(By.ID, 'basic_password').send_keys("verysecret")
    browser.find_element(By.ID, 'login').click()
    time.sleep(3)
    current_url = browser.current_url
    expected_url = "http://localhost:8080"

    assert expected_url, current_url
    # wait for entering the login page
    time.sleep(1)
    browser.save_screenshot('./screenhots/test_login_with_valid_credential.png')

@pytest.mark.usefixtures("open_url")
def test_logout(browser):
    # login
    browser.find_element(By.ID, 'basic_email').send_keys("admin@example.com")
    browser.find_element(By.ID, 'basic_password').send_keys("verysecret")
    browser.find_element(By.ID, 'login').click()
    time.sleep(1)
    
    #logout 
    actions = ActionChains(browser)
    logout_button = browser.find_element(By.XPATH, '//*[@id="root"]/section/header/div/div[2]/span[2]/img')
    actions.move_to_element(logout_button)
    actions.click()
    actions.perform()
    
    current_url = browser.current_url
    expected_url = "http://localhost:8080/login"
    assert expected_url, current_url
    time.sleep(2)
    