from selenium.webdriver.common.by import By

from selenium_wework_login.login import Login
from selenium_wework_login.register import Register
from selenium import webdriver

class Index():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        # click login
        self.driver.find_element(By.XPATH,'//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return Login(self.driver)

    def goto_register(self):
        # click register
        self.driver.find_element(By.XPATH,'//*[@id="tmp"]/div[1]/a').click()
        return Register(self.driver)
