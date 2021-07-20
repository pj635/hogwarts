from hogwarts_homework.homework3.page_object.main_page import MainPage

class TestWeWork:
    def setup(self):
        self.page:MainPage = MainPage()

    def tear_down(self):
        self.page.driver.quit()

    def test_add_member(self, name, account, iphone, email, alias=None, landline=None, address=None, dapartment=None, position=None, identity=None):
        self.page.goto_contacts_page().add_member()


