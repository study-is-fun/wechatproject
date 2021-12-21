from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

from selenium_wework_main.page.base_page import BasePage


class AddMember(BasePage):


    def add_member(self):
        # 添加成员信息
        self.find(By.ID,'username').send_keys("abc1231")
        self.find(By.ID,'memberAdd_english_name').send_keys("0")
        self.find(By.ID,'memberAdd_acctid').send_keys("12344565")
        self.find(By.ID,'memberAdd_phone').send_keys("12345678105")
        self.find(By.XPATH,'/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        # self.driver.find_element(By.ID,'username').send_keys("abc123")
        # self.driver.find_element(By.ID,'memberAdd_english_name').send_keys("0")
        # self.driver.find_element(By.ID,'memberAdd_acctid').send_keys("1234456")
        # self.driver.find_element(By.ID,'memberAdd_phone').send_keys("12345678111")
        # /html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]
        # self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()

        # self.driver.quit()
        # return True
    # 更新页面
    def update_page(self):
        # 获取页码
        contect: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        return [int(x) for x in contect.split('/',1)]

    def get_member(self, value):
        self.wait_for_click((By.CSS_SELECTOR,'.ww_checkbox'))
        # 分割页码
        cur_page, total_page = self.update_page()
        while True:
            # 获取成员信息
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td')
            # 遍历成员信息
            for element in elements:
                if value == element.get_attribute("title"):
                    return True
            # 更新页码
            cur_page = self.update_page()[0]
            # 判断是否最后一页
            if cur_page == total_page:
                return False
            # 点击下一页
            self.find(By.CSS_SELECTOR,'.js_next_page').click()

