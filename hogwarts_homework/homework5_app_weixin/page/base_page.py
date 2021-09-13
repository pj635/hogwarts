from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, driver:WebDriver = None):
        self.driver = driver

    def swipe_find(self, locator, times=10):
        window_rect = self.driver.get_window_rect()
        x = window_rect['width'] / 2
        y_start = window_rect['height'] * 0.8
        y_end = window_rect['height'] * 0.2
        self.driver.implicitly_wait(2)
        for i in range(times):
            try:
                ele = self.find(*locator)
                self.driver.implicitly_wait(20)
                return ele  # 找到指定的元素
            except NoSuchElementException:
                print("%d:not find the element" % i)
            self.driver.swipe(x, y_start, x, y_end, duration=2000)  # 未找到指定元素，向下滑动
        self.driver.implicitly_wait(20)
        raise NoSuchElementException("find the element %d times, and find failed")  # 查找元素失败，抛出异常

    #封装find方法
    def find(self, by, value):
        return self.driver.find_element(by, value)