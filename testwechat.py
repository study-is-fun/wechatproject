import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testdemo():
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    # def teardown(self):
    #     self.driver.quit()

    def test_wechat(self):
        #免登陆操作
        #01打开网站
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        db = shelve.open("cookies")
        # db['cookie'] = self.driver.get_cookies()
        #02输入cookies
        cookies = db['cookie']
        for i in cookies:
            if "expiry" in i.keys():
                i.pop("expiry")
            self.driver.add_cookie(i)
        #重新打开该网站
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        db.close()