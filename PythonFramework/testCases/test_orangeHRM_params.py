import pytest
from pageObject.Login_page import Login_Page1
from utilities.readConfigFile import ReadConfig_Class
import time

class Test_LoginPage_params:
    # Username = ReadConfig_Class.getUsername()
    # Password = ReadConfig_Class.getPassword()
    def test_OrangeHRM_Login_params(self, setup, getDataForLogin):
        self.driver = setup
        self.lp = Login_Page1(self.driver)
        self.lp.Enter_username(getDataForLogin[0])
        time.sleep(3)
        self.lp.Enter_password(getDataForLogin[1])
        time.sleep(3)
        self.lp.Click_login()
        if self.lp.validate_Login_status() == "LoginPass" and getDataForLogin[2]=="Login_Pass":
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_pass.png")
            self.lp.click_menu()
            self.lp.click_logout()
            assert True
        elif self.lp.validate_Login_status() == "LoginPass" and getDataForLogin[2] == "Login_Fail":
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_fail.png")
            self.lp.click_menu()
            self.lp.click_logout()
            assert False
        elif self.lp.validate_Login_status() == "LoginFail" and getDataForLogin[2] == "Login_Pass":
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_fail.png")
            self.lp.click_menu()
            self.lp.click_logout()
            assert False
        elif self.lp.validate_Login_status() == "LoginFail" and getDataForLogin[2] == "Login_Fail":
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_fail.png")
            self.lp.click_menu()
            self.lp.click_logout()
            assert True
        self.driver.quit()