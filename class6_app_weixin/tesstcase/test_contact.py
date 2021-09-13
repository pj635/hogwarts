from faker import Faker
from class6_app_weixin.page.app import App


class TestContact():

    def setup_class(self):
        self.faker = Faker(locale='zh_CN')
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.close()

    def test_contact1(self):
        name, phone_number = self.faker.name(), self.faker.phone_number()
        self.main.goto_contact().goto_add_member().\
            goto_edit_member().edit_member(name, phone_number).find_toast()

    def test_contact2(self):
        name, phone_number = self.faker.name(), self.faker.phone_number()
        self.main.goto_contact().goto_add_member().\
            goto_edit_member().edit_member(name, phone_number).find_toast()
