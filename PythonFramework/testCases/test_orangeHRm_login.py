import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObject.Login_page import  Login_Page1


class Test_OrangeHRM_Login:
    def test_OrangeHRM_url(self, setup):
        self.driver = setup
        print("driver.title-->" + self.driver.title)
        if self.driver.title == "OrangeHRM":
            self.driver.save_screenshot(".\\Screenshots\\Test_OrangeHRM_Login_pass.png")
            assert True
        else:
            assert False
        self.driver.quit()

    def test_OrangeHRM_Login(self, setup):
        self.driver = setup
        self.lp =Login_Page1(self.driver)
        self.lp.Enter_username("Admin")
        time.sleep(3)
        self.lp.Enter_password("admin123")
        self.lp.Click_login()
        #
        if self.lp.validate_Login_status() == "LoginPass":
            self.driver.save_screenshot(".\\Screenshots\\Test_OrangeHRM_Login_pass.png")
            self.lp.Click_Manu_button()
            self.lp.Click_logout_button()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\Test_OrangeHRM_Login_fail.png")
            assert False

        self.driver.quit()

