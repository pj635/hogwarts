# coding=utf-8
import pytest
from appium import webdriver

class TestUiAutomator():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        #desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
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

    def test_uiAutomator_location(self):
        #外侧用 ‘’ （单引号） ，里面的字符串用 " " （双引号）
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        #self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("账号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("54321")

    def test_uiAutomator_scroll(self):
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/title_text" and @text="关注"]').click()
        #滚动定位
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()\
                .scrollable(true).instance(0)).scrollIntoView(new UiSelector().\
                text("特蕾莎小姐").instance(0))')

if __name__ == '__main__':
    pytest.main()