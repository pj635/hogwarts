from time import sleep

import pytest
from appium import webdriver

class TestElementLocation():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        # desired_caps['browserName'] = 'Browser'   #The desired should not include both of an 'appPackage' and a 'browserName'
        desired_caps['chromedriverExecutable'] = 'D:\Downloads\log\chromedriver.exe'

        desired_caps['deviceName'] = '127.0.0.1:21503'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noRest'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialzation'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # # desired_caps['platformVersion'] = '6.0'
        # desired_caps['deviceName'] = '127.0.0.1:21503'
        # desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        # desired_caps['noRest'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        # desired_caps['skipDeviceInitialzation'] = 'true'
        # desired_caps['unicodeKeyBoard'] = 'true'
        # desired_caps['resetKeyBoard'] = 'true'


        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)
        
    def test_1(self):
        print('')
        print(self.driver.contexts)
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="交易"]').click()
        print(self.driver.contexts)
        self.driver.find_element_by_xpath('//*[@text="期货开户"]').click()
        print(self.driver.contexts)
        self.driver.find_element_by_xpath('//*[@text="海通期货"]').click()
        print(self.driver.contexts)
        sleep(8)
        print(self.driver.contexts)
    def teardown(self):
        pass