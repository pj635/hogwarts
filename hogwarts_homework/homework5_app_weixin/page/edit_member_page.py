from appium.webdriver.common.mobileby import MobileBy

from hogwarts_homework.homework5_app_weixin.page.add_member_page import AddMemberPage
from hogwarts_homework.homework5_app_weixin.page.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phone_number):
        locator = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']")
        self.find(*locator).send_keys(name)
        locator = (MobileBy.XPATH, "//*[contains(@text, '手机')]/../..//*[@text='必填']")
        self.find(*locator).send_keys(phone_number)
        locator = (MobileBy.XPATH, "//*[@text = '保存']")
        self.find(*locator).click()

        return AddMemberPage(self.driver)
