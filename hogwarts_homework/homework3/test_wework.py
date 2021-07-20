import yaml
from selenium import webdriver

# chrome --remote-debugging-port=9222:开启浏览器debug模式，复用浏览器
# 通过浏览器复用的方法获取上次登录的cookie值并保存至文档
def test_get_wework_cookies():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    # self.driver.implicitly_wait(10)
    cookie = driver.get_cookies()
    with open("./cookie_data", "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)

class TestWeWork:
    def setup(self):
        log_page_url="https://work.weixin.qq.com/wework_admin/loginpage_wx"
        main_page_url="https://work.weixin.qq.com/wework_admin/frame#index"
        self.driver = webdriver.Chrome()
        self.driver.get(log_page_url)
        with open("./cookie_data", encoding="UTF-8") as f:
            cookies = yaml.safe_load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get(main_page_url)

    def tear_down(self):
        self.driver.quit()

    def test_add_member(self):
        self.driver.find_element_by_id("menu_contacts").click()


