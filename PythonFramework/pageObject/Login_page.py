import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By


class Login_Page1:
       text_username_xpath = (By.XPATH,"//input[@placeholder='Username']")
       text_password_xpath = (By.XPATH,"//input[@placeholder='Password']")
       click_login = (By.XPATH,"//button[normalize-space()='Login']")
       click_menu = (By.XPATH,"//p[@class='oxd-userdropdown-name']")
       click_logout = (By.XPATH,"//a[normalize-space()='Logout']")

       def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 10)

       def Enter_username(self,username) :
           self.wait.until(expected_conditions.visibility_of_element_located(self.text_username_xpath))
           self.driver.find_element(*Login_Page1.text_username_xpath).send_keys(username)

       def Enter_password(self,password):
           self.wait.until(expected_conditions.visibility_of_element_located(self.text_password_xpath))
           self.driver.find_element(*Login_Page1.text_password_xpath).send_keys(password)

       def Click_login(self):
           self.driver.find_element(*Login_Page1.click_login).click()

       def Click_Manu_button(self):
           self.driver.find_element(*Login_Page1.click_menu).click()

       def Click_logout_button(self):
           self.driver.find_element(*Login_Page1.click_logout).click()

       def validate_Login_status(self):
           try:
               time.sleep(2)
               self.driver.find_element(*Login_Page1.click_menu)
               time.sleep(3)
               print("User login test case is passed")
               return "LoginPass"
           except:
               print("User login test case is failed")
               # return "LoginFail"


