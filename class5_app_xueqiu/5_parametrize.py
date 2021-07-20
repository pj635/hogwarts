import pytest
from appium import webdriver


class TestUiParam():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noRest'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialzation'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('company, text', [("阿里巴巴", "BABA"), ("小米", "01810")])
    def test_param(self, company, text):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(company)
        locator = "//*[@resource-id='com.xueqiu.android:id/stockCode' and @text='%s']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']" %  text
        current_price = self.driver.find_element_by_xpath(locator).text
        print(current_price)