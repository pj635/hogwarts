import yaml
from selenium import webdriver

class BasePage(object):
    def __init__(self, base_driver:webdriver=None):
        if base_driver == None:
            # 实例化 driver
            self.driver = webdriver.Chrome()
            # 访问扫码登录页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            with open("cookie_data.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                print(yaml_data)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.implicitly_wait(10)
        else:
            self.driver = base_driver

    def find(self, by, ele=None):
        if ele == None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)

