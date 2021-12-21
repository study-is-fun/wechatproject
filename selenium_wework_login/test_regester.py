from selenium_wework_login.index import Index


class TestRegester():
    def setup(self):
        self.index = Index()

    def test_regester(self):
        self.index.goto_login().goto_register().register()
        # self.index.goto_register()


