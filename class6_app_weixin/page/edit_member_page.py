from appium.webdriver.webdriver import WebDriver


class EditMemberPage():
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def edit_member(self, name, phone_number):
        self.driver.find_element_by_xpath("//*[contains(@text, '姓名')]/..//*[@text='必填']").send_keys(name)
        self.driver.find_element_by_xpath("//*[contains(@text, '手机')]/../..//*[@text='必填']").send_keys(phone_number)
        self.driver.find_element_by_xpath("//*[@text = '保存']").click()

        from class6_app_weixin.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
