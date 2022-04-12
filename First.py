from lib2to3.pgen2 import driver
from ast import Assert
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import selenium
#driver = webdriver.Chrome("D:\\Chromedriver.exe")
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://10.94.6.100/Login?ReturnUrl=%2f')
driver.fullscreen_window
#searchbox=driver.find_element(By.XPATH,'//*[@id="search"]')
login=driver.find_element(By.ID,'UserName')
password=driver.find_element(By.ID,'Password')
login.send_keys('global')
password.send_keys('global')
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
assert driver.find_element(By.XPATH,"//div[contains(text(), 'Welcome back')]").is_displayed
driver.quit()