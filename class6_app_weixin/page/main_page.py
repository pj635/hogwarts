from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from class6_app_weixin.page.base_page import BasePage
from class6_app_weixin.page.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        locator = (MobileBy.XPATH, "//*[@text='通讯录']")
        ele = WebDriverWait(self.driver, 80,).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()
        return ContactPage(self.driver)
