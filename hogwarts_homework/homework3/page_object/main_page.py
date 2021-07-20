from hogwarts_homework.homework3.page_object.base_page import BasePage
from hogwarts_homework.homework3.page_object.contacts_page import ContactsPage

class MainPage(BasePage):
    def goto_contacts_page(self):
        self.driver.find_element_by_id("menu_contacts").click()
        return ContactsPage(self.driver)