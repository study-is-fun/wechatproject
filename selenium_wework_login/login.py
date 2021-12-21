from selenium.webdriver.common.by import By

from selenium_wework_login.register import Register
from selenium.webdriver.remote.webdriver import WebDriver

class Login():

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        # click register
        self.driver.find_element(By.XPATH,'//*[@id="wework_admin.loginpage_wx2_$"]/main/div[2]/a').click()
        return Register(self.driver)