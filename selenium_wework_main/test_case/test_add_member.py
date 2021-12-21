
from selenium_wework_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()


    def test_addmember(self):
        # assert self.main.goto_Add_Member().add_member()
        add_member = self.main.goto_Add_Member()
        add_member.add_member()
        assert add_member.get_member("abc1231")

