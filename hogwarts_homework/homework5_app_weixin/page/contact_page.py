from appium.webdriver.common.mobileby import MobileBy

from hogwarts_homework.homework5_app_weixin.page.add_member_page import AddMemberPage
from hogwarts_homework.homework5_app_weixin.page.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        locator = (MobileBy.XPATH, "//*[@text = '添加成员']")
        ele = self.swipe_find(locator)
        ele.click()
        return AddMemberPage(self.driver)

