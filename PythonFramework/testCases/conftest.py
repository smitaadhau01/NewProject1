import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return driver

@pytest.fixture(params=[
    ("Admin", "admin123", "Login_Pass"),
    ("Admin1", "admin123", "Login_Fail"),
    ("Admin", "admin1231", "Login_Fail"),
    ("Admin1", "admin1231", "Login_Fail")
])
def getDataForLogin(request):
    return request.param