from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    driver = None
    _base_url = ""

    def __init__(self,driver: WebDriver = None):

        if driver is None:
            options = Options
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver
            self.driver.implicitly_wait(5)

        if self._base_url !="":
            self.driver.get(self._base_url)

    # 将self.driver.find_element改名
    def find(self, by, locater):
        return self.driver.find_element(by, locater)

    # 将self.driver.find_elements改名
    def finds(self, by, locater):
        return self.driver.find_elements(by, locater)

    # 显式等待
    def wait_for_click(self, locator, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))