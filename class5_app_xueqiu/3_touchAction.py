import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestElementTouchAction():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noRest'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialzation'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        #self.driver.quit()
        pass

    def test_touchAction1(self):
        # 等待加载页面
        assert self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/tab_name' and @text = '雪球']").is_displayed()
        touch = TouchAction(self.driver)
        window = self.driver.get_window_rect()
        print(window)
        x_50 = int(window['width'] * 0.5)
        y_20 = int(window['height'] * 0.2)
        y_80 = int(window['height'] * 0.8)
        print(x_50, y_20, y_80)
        touch.press(x=x_50, y=y_80).wait(500).move_to(x=x_50, y=y_20).release().perform()

    def test_touchAction2(self):
        # 等待加载页面
        assert self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/tab_name' and @text = '雪球']").is_displayed()
        touch = TouchAction(self.driver)
        window = self.driver.get_window_rect()
        print(window)
        x_50 = int(window['width'] * 0.5)
        y_20 = int(window['height'] * 0.2)
        y_80 = int(window['height'] * 0.8)
        print(x_50, y_20, y_80)
        touch.press(x=x_50, y=y_80).wait(500).move_to(x=x_50, y=y_20).release().perform()
