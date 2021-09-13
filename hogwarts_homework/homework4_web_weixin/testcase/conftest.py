import yaml
from selenium import webdriver

# chrome --remote-debugging-port=9222:开启浏览器debug模式，复用浏览器
# 通过浏览器复用的方法获取上次登录的cookie值并保存至文档
def test_wework_cookies():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    cookie = driver.get_cookies()
    with open("./cookie_data.yaml", "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)