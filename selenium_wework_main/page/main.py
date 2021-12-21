
from selenium.webdriver.common.by import By

from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_Add_Member(self):
        #click addmember
        #设置显式等待
        locator = (By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]')
        self.wait_for_click(locator)
        self.find(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
        return AddMember(self.driver)




