from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from class6_app_weixin.page.base_page import BasePage
from class6_app_weixin.page.main_page import MainPage

class App(BasePage):

    def start(self):
        print(self.driver)
        if self.driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['deviceName'] = 'demo'
            desired_caps['noRest'] = 'true'
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            desired_caps['autoGrantPermissions'] = 'true'
            desired_caps['dontStopAppOnReset'] = 'true'

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(20)
            print("\n第一次初始化driver")

        else:
            self.driver.launch_app()
            print("\n直接launch app")

        locator = (MobileBy.XPATH, "//*[@text='微信登录']")
        ele = WebDriverWait(self.driver, 20, ).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()
        locator = (MobileBy.XPATH, "//*[@text='同意']")
        ele = WebDriverWait(self.driver, 20, ).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()
        locator = (MobileBy.XPATH, "//*[@text='进入']")
        ele = WebDriverWait(self.driver, 20,).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()

        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)