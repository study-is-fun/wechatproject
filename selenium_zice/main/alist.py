from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_zice.main.add_member import AddMember


class Alist():
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def AddMassage(self):
        sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        return AddMember(self.driver)



