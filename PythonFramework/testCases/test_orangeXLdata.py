from importlib.metadata import pass_none

from pageObject.Login_page import LoginPage_Class
from utilities import Xcel_utiles
from utilities.Xcel_utiles import readData


class Test_orangeXL:
    file_path = ".\\testCases\\Test_Data\\Test_Data.xlsx"

    def test_orange_xl_login(self,setup):
        self.driver = setup
        self.lp = LoginPage_Class(self.driver)
        self.rows = Xcel_utiles.get_rowCount(self.file_path,"login_data")
        print("Number of rows in Excel Test data-->" + str(self.rows))
        List_status = []
        for r in range (2,self.rows+1):
            self.username = Xcel_utiles.readData(self.file_path,"login_data",r,2)
            self.password = Xcel_utiles,readData(self.file_path,"login_data",r,3)
            self.Ectual_Result = Xcel_utiles,readData(self.file_path, "login_data", r, 4)
            self.lp.Enter_UserName(self.username)
            self.lp.Click_LoginButton()
            if self.lp.Validate_Login_Stauts() == "LoginPass" and self.Ectual_Result == "Login_Pass":
               List_status.append("Pass")
               Xcel_utiles.writeData(self.file_path,"login_data",r,5,"pass")
               self.driver.save_screenshot(".\\Screenshots\\test_orange_xl_login_pass.png")
               self.lp.Click_Menu_Button()
               self.lp.Click_Logout_Button()

            elif self.lp.Validate_Login_Stauts() == "LoginPass" and self.Ectual_Result == "Login_Fail":
                List_status.append("Fail")
                Xcel_utiles.writeData(self.file_path, "login_data", r, 5, "fail")
                self.driver.save_screenshot(".\\Screenshots\\test_orange_xl_login_fail.png")
                self.lp.Click_Menu_Button()
                self.lp.Click_Logout_Button()

            elif self.lp.Validate_Login_Stauts() == "LoginFail" and self.Ectual_Result == "Login_Pass":
                List_status.append("Fail")
                Xcel_utiles.writeData(self.file_path, "login_data", r, 5, "fail")
                self.driver.save_screenshot(".\\Screenshots\\test_orange_xl_login_fail.png")
                self.lp.Click_Menu_Button()
                self.lp.Click_Logout_Button()

            elif self.lp.Validate_Login_Stauts() == "LoginFail" and self.Ectual_Result == "Login_Fail":
                List_status.append("Pass")
                Xcel_utiles.writeData(self.file_path, "login_data", r, 5, "pass")
                self.driver.save_screenshot(".\\Screenshots\\test_orange_xl_login_fail.png")
                self.lp.Click_Menu_Button()
                self.lp.Click_Logout_Button()
        print(List_status)
        if "Fail" not in List_status:
            assert True
        else:
            assert False


        self.driver.quit()