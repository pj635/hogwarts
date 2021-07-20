from time import sleep

import pytest
from appium import webdriver

class TestUiParam():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        desired_caps['browser'] = 'Browser'
        desired_caps['noRest'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['appPackage'] = 'com.android.browser'
        desired_caps['appActivity'] = 'BrowserActivity'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        #self.driver.quit()
        pass

    def test_web_app(self):
        #self.driver.get("http://m.baidu.com")
        self.driver.get("http://www.qq.com")
        sleep(5)