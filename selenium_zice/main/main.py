from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium_zice.main.alist import Alist


class Main():
    def __init__(self):
        options = Options
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')


    def goto_alist(self):
        self.driver.find_element(By.ID,'menu_contacts').click()
        return Alist(self.driver)
