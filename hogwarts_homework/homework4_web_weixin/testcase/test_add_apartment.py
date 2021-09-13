from hogwarts_homework.homework4_web_weixin.page_object.main_page import MainPage
import yaml
from selenium import webdriver

class TestAddApartment:
    def setup_class(self):
        self.main_page = MainPage()

    def test_add_apartment(self):
        self.main_page.goto_contact().add_department("测试部", "技术部")