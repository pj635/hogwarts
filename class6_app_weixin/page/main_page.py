from class6_app_weixin.page.base_page import BasePage
from class6_app_weixin.page.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        self.driver.find_element_by_xpath("//*[@text = '通讯录']").click()
        return ContactPage(self.driver)
