from selenium.webdriver.common.by import By
from hogwarts_homework.homework4_web_weixin.page_object.contact import ContactPage
from hogwarts_homework.homework4_web_weixin.page_object.base_page import BasePage

class MainPage(BasePage):
    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)
