from hogwarts_homework.homework3.page_object.base_page import BasePage

class ContactsPage(BasePage):
    def add_member(self, name, account, iphone, email, alias=None, landline=None, address=None, dapartment=None, position=None, identity=None):
        self.driver.find_element_by_partial_link_text("添加成员").click()
        self.driver.find_element_by_id("username").send_keys(name)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(account)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(iphone)
        self.driver.find_element_by_id("memberAdd_mail").send_keys(email)
        if alias:
            self.driver.find_element_by_id("memberAdd_english_name")