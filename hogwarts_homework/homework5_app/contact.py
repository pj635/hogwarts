import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class TestContact():
    implicitly_wait = 20
    def setup(self):
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
        self.driver.implicitly_wait(self.implicitly_wait)

        self.driver.find_element_by_xpath("//*[@text='微信登录']").click()
        self.driver.find_element_by_xpath("//*[@text='同意']").click()
        self.driver.find_element_by_xpath("//*[@text='进入']").click()

    def teardown(self):
        self.driver.quit()
        pass

    def __swipe_find(self, locator, times = 3):
        window_rect = self.driver.get_window_rect()
        x = window_rect['width'] / 2
        y_start = window_rect['height'] * 0.8
        y_end = window_rect['height'] * 0.2
        self.driver.implicitly_wait(2)
        for i in range(times):
            try:
                ele = self.driver.find_element(*locator)
                self.driver.implicitly_wait(self.implicitly_wait)
                return ele       #找到指定的元素
            except NoSuchElementException:
                print("%d:not find the element" % i)
            self.driver.swipe(x, y_start, x, y_end, duration=2000) #未找到指定元素，向下滑动
        self.driver.implicitly_wait(self.implicitly_wait)
        raise NoSuchElementException("find the element %d times, and find failed")  #查找元素失败，抛出异常


    @pytest.mark.parametrize('name, phone_number', [
        ('赵六', '18840839909')
    ])
    def test_web_app(self, name, phone_number):
        self.driver.find_element_by_xpath("//*[@text = '通讯录']").click()
        #self.driver.find_element_by_xpath("//*[@text = '添加成员']").click()
        locator = (MobileBy.XPATH, "//*[@text = '添加成员']")
        ele = self.__swipe_find(locator)
        ele.click()
        self.driver.find_element_by_xpath("//*[@text = '手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text, '姓名')]/..//*[@text='必填']").send_keys(name)
        self.driver.find_element_by_xpath("//*[contains(@text, '手机')]/../..//*[@text='必填']").send_keys(phone_number)
        self.driver.find_element_by_xpath("//*[@text = '保存']").click()
        self.driver.find_element_by_xpath("//*[contains(@text, '添加成功') or contains(@text, '已存在于通讯录')]")


