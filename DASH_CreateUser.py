# -*- coding: utf-8 -*-
#from random import randint, random
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class CreateNewUserDynamicEmailUsernameVerifyAssert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\\Chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.94.6.100"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_new_user_dynamic_email_username_verify_assert(self):
        driver = self.driver
        #environment = "http://10.94.6.100:60000/"
        #username = driver.execute_script("var environment = \"" + str(environment) + "\";var storedVars = { 'environment': environment }; return " + "'user'+Math.floor(Math.random() * 10000)")
        GlobalId=randint(1000,50000)
        username='Testuser'+str(GlobalId)
        email = username + "@mail.ru"
        driver.get("http://10.94.6.100")
        loginform = self.is_element_present(By.ID, "UserName")
        driver.find_element_by_id("UserName").clear()
        driver.find_element_by_id("UserName").send_keys("global")
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("global")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//span[@class='header-banner__close-button']").is_displayed()
        driver.find_element_by_xpath("//span[@class='header-banner__close-button']").click()
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element_by_xpath("//div[contains(text(), 'Users')]")).perform()
        


        driver.find_element_by_xpath("//div[contains(text(), 'Users')]").is_displayed()
        driver.find_element_by_xpath("//div[contains(text(), 'Users')]").click()
        driver.find_element_by_xpath("//span[contains(text(), 'Create new user')]").is_displayed()
        driver.find_element_by_xpath("//span[contains(text(), 'Create new user')]").click()
        driver.find_element_by_xpath("//span[contains(text(), 'MPC Film')]").is_displayed()
        driver.find_element_by_xpath("//span[contains(text(), 'Username')]/following::input").clear()
        driver.find_element_by_xpath("//span[contains(text(), 'Username')]/following::input").send_keys(username)
        driver.find_element_by_xpath("//span[contains(text(), 'Email Address')]/following::input").clear()
        driver.find_element_by_xpath("//span[contains(text(), 'Email Address')]/following::input").send_keys(email)
        driver.find_element_by_xpath("//span[contains(text(), 'First Name')]/following::input").clear()
        driver.find_element_by_xpath("//span[contains(text(), 'First Name')]/following::input").send_keys("Simba")
        driver.find_element_by_xpath("//span[contains(text(), 'Last Name')]/following::input").clear()
        driver.find_element_by_xpath("//span[contains(text(), 'Last Name')]/following::input").send_keys("Lorris")
        driver.find_element_by_xpath("//span[contains(text(), 'Comment')]/following::input").clear()
        driver.find_element_by_xpath("//span[contains(text(), 'Comment')]/following::input").send_keys("Simple text in a comment")
        driver.find_element_by_xpath("//span[contains(text(),'Global')]/following::input[1]").send_keys(GlobalId)
        time.sleep(2)
        driver.find_element_by_xpath("(//label[contains(text(), 'Select all')])[1]").click()
        actions.move_to_element(driver.find_element_by_xpath("(//label[contains(text(), 'Select all')])[2]")).perform()
        driver.find_element_by_xpath("(//label[contains(text(), 'Select all')])[2]").click()
        actions.move_to_element(driver.find_element_by_xpath("(//label[contains(text(), 'Select all')])[3]")).perform()
        driver.find_element_by_xpath("(//label[contains(text(), 'Select all')])[3]").click()
       # driver.find_element_by_xpath("(//div[@class='ui-checkbox table-row-group__btns__checkbox ui-checkbox_default'])[1]").click()
        i = 1
        while i<=5 :
            index=str(i)
            driver.find_element_by_xpath("(//div[@class='ui-checkbox table-row-group__btns__checkbox ui-checkbox_default'])["+index+"]").click()
            i = i + 1

        driver.find_element_by_xpath("//span[contains(text(), 'Create')]").click()
        driver.find_element_by_xpath("//div[contains(text(), 'This global ID does')]").is_displayed()
        time.sleep(2)
        driver.find_element_by_xpath("//span[contains(text(), 'Yes')]").click()
        time.sleep(3)

        # verification
        driver.find_element_by_xpath("//span[contains(text(), 'Authorised by')]").is_displayed()
        driver.find_element_by_xpath("//span[contains(text(), 'MPC Film')]").is_displayed()
        try: self.assertEqual(username, driver.find_element_by_xpath("//span[contains(text(), 'Username')]/following::input").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(email, driver.find_element_by_xpath("//span[contains(text(), 'Email Address')]/following::input").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Simba", driver.find_element_by_xpath("//span[contains(text(), 'First Name')]/following::input").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual("Lorris", driver.find_element_by_xpath("//span[contains(text(), 'Last Name')]/following::input").get_attribute("value"))
        self.assertEqual("Simple text in a comment", driver.find_element_by_xpath("//span[contains(text(), 'Comment')]/following::input").get_attribute("value"))
        try: self.assertTrue(driver.find_element_by_xpath("(//div[contains(@class,'ui-checkbox table-content__column__item__select-all ui-checkbox_default')]/input)").is_selected())
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(driver.find_element_by_xpath("(//div[contains(@class,'ui-checkbox table-content__column__item__select-all ui-checkbox_default')]/input)[2]").is_selected())
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(driver.find_element_by_xpath("(//div[contains(@class,'ui-checkbox table-content__column__item__select-all ui-checkbox_default')]/input)[3]").is_selected())
        except AssertionError as e: self.verificationErrors.append(str(e))
        i = 1
        while i<=5 :
            index=str(i)
            try: self.assertTrue(driver.find_element_by_xpath("(//div[contains(@class,'ui-checkbox table-row-group__btns__checkbox ui-checkbox_default')]/input)[" + index + "]").is_selected())
            except AssertionError as e: self.verificationErrors.append(str(e))
            i = i+1

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
