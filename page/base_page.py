"""
封装公共方法
"""
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class BasePage:
    _driver: WebDriver = None
    # 黑名单列表
    _back_list = [
        (By.ID, "com.tojoy.huzhugou:id/btn_pos")  # 主页面弹出的条款框中的同意按钮
    ]
    # 计数器
    _max_num = 3
    _error_num = 0

    # 初始化driver
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # 通过find_element查找元素
    def find(self, locator, value):
        try:
            element = self._driver.find_element(locator, value)
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            # 出现异常，将隐式等待设置小一点
            self._driver.implicitly_wait(1)
            # 判断异常处理次数
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for black in self._back_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            # 处理完黑名单后，再次找原来的元素
            return self.find(locator, value)

    # 通过finds_element查找元素
    def finds(self, locator, value):
        try:
            element = self._driver.find_elements(locator, value)
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            # 出现异常，将隐式等待设置小一点
            self._driver.implicitly_wait(1)
        # 判断异常处理次数
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for black in self._back_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            # 处理完黑名单后，再次找原来的元素
            return self.finds(locator, value)

    # 点击事件封装
    def click(self, element: WebElement):
        return element.click()

    # 取控件文本内容的封装
    def get_text(self, element: WebElement):
        return element.text

    # 读取yaml文件方法
    def read_yamldata(self, filename, section, option1):
        with open(filename, encoding="utf8") as f:
            self.datas = yaml.full_load(f)
            return self.datas[section][option1]
    # 滑屏
    def do_Scroll(self, value):
        self._driver.find_element_by_android_uiautomator('new UiScrollable('
                                                            'new UiSelector().scrollable(true).instance(0))'
                                                            '.scrollIntoView('
                                                            'new UiSelector().text(' + '\"' + str(value) + '\"' + ').instance(0));').click()

    # 测试步骤封装#todoß
    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    self.click(element)
