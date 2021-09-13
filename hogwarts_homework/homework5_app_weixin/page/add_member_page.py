from appium.webdriver.common.mobileby import MobileBy

from hogwarts_homework.homework5_app_weixin.page.base_page import BasePage


class AddMemberPage(BasePage):

    def goto_edit_member(self):
        locator = (MobileBy.XPATH, "//*[@text='手动输入添加']")
        self.find(*locator).click()

        from hogwarts_homework.homework5_app_weixin.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)


    def find_toast(self, value):
        locator = (MobileBy.XPATH, f"//*[contains(@text, '{value}')]")
        return self.find(*locator).text
