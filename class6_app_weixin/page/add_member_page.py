from class6_app_weixin.page.base_page import BasePage


class AddMemberPage(BasePage):

    def goto_edit_member(self):
        self.driver.find_element_by_xpath("//*[@text = '手动输入添加']").click()

        from class6_app_weixin.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)


    def find_toast(self):
        self.driver.find_element_by_xpath("//*[contains(@text, '添加成功')]")
