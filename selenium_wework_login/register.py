
from time import sleep
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Register():
    def __init__(self, driver:WebDriver):
        self.driver = driver


    def register(self):
        # send massage
        self.driver.find_element(By.ID,'corp_name').send_keys('abc123')
        self.driver.find_element(By.ID,'manager_name').send_keys('abc123')
        self.driver.find_element(By.ID,'register_tel').send_keys('139876545678')
        sleep(5)
        self.driver.quit()
        return True

        pass