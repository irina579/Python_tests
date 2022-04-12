from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By

from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.youtube.com/')
#searchbox = driver.find_element_by_xpath('//input[@id="search"]')
searchbox = driver.find_element(By.XPATH, '//input[@id="search"]')
searchbox.send_keys('natalia qa')