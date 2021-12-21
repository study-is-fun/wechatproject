from selenium_zice.main.main import Main


class Test_zi():
    def setup(self):
        self.main = Main()



    def test_add2(self):
        self.main.goto_alist().AddMassage().addmember()

        assert "aaa" in self.main.goto_alist().AddMassage().get_member()



