"""
封装公共方法
"""
import inspect
import json

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from page.wrapper import handle_black


class BasePage:
    _driver: WebDriver = None
    _params = {}
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
    @handle_black
    def find(self, locator, value):
        element = self._driver.find_element(locator, value)
        return element

    # 通过finds_element查找元素
    @handle_black
    def finds(self, locator, value):
        element = self._driver.find_elements(locator, value)
        return element

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
                                                         'new UiSelector().text(' + '\"' + str(
            value) + '\"' + ').instance(0));').click()

    # 测试步骤封装
    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            # 取到调用方法的方法名称
            name = inspect.stack()[1].function
            # 取到要操作的ymal文件的模块
            steps = yaml.safe_load(f)[name]
            # 将元素的信息转换成字符串格式
            raw = json.dumps(steps)
            # 将串中带有${name}的地方用self._param的value值替换
            for key, value in self._params.items():
                raw = raw.replace('${' + key + '}', value)
            # 最后再将元素的字符串转换成json格式
            steps = json.loads(raw)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                # click
                if action == "click":
                    self.find(step["by"], step["locator"]).click()
                # send_keys
                if action == "send":
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if action == "getText":
                    result = self.find(step["by"], step["locator"]).text
                    return result
                # send_keys
                if action == "webview_click":
                    WebDriverWait(self._driver, 40).until(
                        lambda x: "WEBVIEW_com.tojoy.huzhugou" in self._driver.contexts)
                    self._driver.switch_to.context("WEBVIEW_com.tojoy.huzhugou")
                    self.find(step["by"], step["locator"]).click()
                    self._driver.switch_to.context("NATIVE_APP")
