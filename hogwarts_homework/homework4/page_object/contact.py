from time import sleep

from selenium.webdriver.common.by import By
from hogwarts_homework.homework4.page_object.base_page import BasePage

class ContactPage(BasePage):
    def add_department(self, dapart_name, father_depart):
        self.find(By.XPATH, "//*[@class='member_colLeft_top_addBtn']").click()
        self.find(By.PARTIAL_LINK_TEXT, "添加部门").click()
        self.find(By.XPATH, "//*[@class='qui_inputText ww_inputText']").send_keys(dapart_name)
        self.find(By.XPATH, '//*[contains(text(), "选择所属部门")]').click()
        ele_father_depart = "\"//*[@class='qui_dialog_body ww_dialog_body']//*[contains(text(), '%s')]\"" % father_depart
        print("*"*100)
        print(ele_father_depart)
        #self.find(By.XPATH, ele_father_depart).click()
        self.find(By.XPATH, "//*[@class='qui_dialog_body ww_dialog_body']//*[contains(text(), '技术部')]").click()
        #self.find(By.XPATH, '//*[contains(text(), "确定")]').click()