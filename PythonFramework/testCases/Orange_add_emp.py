import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Smita")
driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("R")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Adhau")
time.sleep(3)
file = r"C:\Users\ASUS\Pictures\Saved Pictures\nature.jpg"
time.sleep(3)
driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file)
time.sleep(4)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
success_msg = driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']").text
print(success_msg)
if success_msg == "Successfully Saved" :
    print("Add employee test case is passed")
else:
    print("Add employee test case is failed")