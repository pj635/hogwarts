import yaml
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver

class BasePage(object):
    def __init__(self, base_driver:webdriver = None):
        if base_driver == None:
            log_page_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
            main_page_url = "https://work.weixin.qq.com/wework_admin/frame#index"
            self.driver = webdriver.Chrome()
            self.driver.get(log_page_url)
            with open("./cookie_data", encoding="UTF-8") as f:
                cookies = yaml.safe_load(f)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            self.driver.get(main_page_url)
            self.driver.implicitly_wait(5)
        else:
            self.driver:WebDriver = base_driver
