from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMember():
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def addmember(self):
        self.driver.find_element(By.ID,'username').send_keys("aaa")
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys("aaa")
        self.driver.find_element(By.ID,'memberAdd_phone').send_keys("12212121212")
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()

    def get_member(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td')
        list = [element.get_attribute('title') for element in elements]

        return list

