"""
收货地址页面：
    1、添加新地址
    2、编辑收货地址
    3、删除收货地址
"""
import random
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class ConsigneeAddress(BasePage):
    _receive_address = (By.XPATH, "//*[@resource-id='com.tojoy.huzhugou:id/iv_util_icon' and @text='收货地址']")  # 收货地址模块
    _btn_add_address = (By.ID, "com.tojoy.huzhugou:id/button_addNewAddress")
    _text_consignee = (By.ID, "com.tojoy.huzhugou:id/edit_Name")  # 收货人
    _text_consignee_phone = (By.ID, "com.tojoy.huzhugou:id/edit_Phone")  # 收货人联系方式
    _text_consignee_address = (By.ID, "com.tojoy.huzhugou:id/test_City")  # 收货人联系地址
    _text_consignee_detailed_address = (By.ID, "com.tojoy.huzhugou:id/edit_Address")  # 收货人详细地址
    _btn_consignee_save = (By.ID, "com.tojoy.huzhugou:id/button_addNewAddress")  # 添加新地址按钮
    _list_address_addname = (By.ID, "com.tojoy.huzhugou:id/test_Name")  # 收货地址列表中收货人

    _btn_edit = (By.ID, "com.tojoy.huzhugou:id/imv_BianJi")  # 编辑按钮
    _tmpdelname = (By.XPATH,
                   '//*[@resource-id="com.tojoy.huzhugou:id/imv_BianJi"]/..//[@resource-id="com.tojoy.huzhugou:id/test_Name"]')  # 编辑按钮所对应的收货人
    _btn_del = (By.ID, "com.tojoy.huzhugou:id/tv_right")  # 删除按钮

    # 添加新地址
    def add_address(self, consignee, consigneephone, consigneeaddress, consigneedetailsaddress):
        # # 当页面中有android.webkit.WebView出现时，切换上下文，然后进行webview的定位（原来这个页面是webview,后来改成原生）
        # WebDriverWait(self._driver, 40).until(lambda x: "WEBVIEW_com.tojoy.huzhugou" in self._driver.contexts)
        # self._driver.switch_to.context("WEBVIEW_com.tojoy.huzhugou")
        # # *************************************************************************
        self.click(self.find(*self._btn_add_address))  # 点击添加新地址按钮
        tempconsignee = consignee + str(random.randint(1000, 9999))  # 将测试用例页面传递过来的收货人加上一个4位的随机数赋给一个临时变量
        self.find(*self._text_consignee).send_keys(tempconsignee)  # 收货人框赋值
        self.find(*self._text_consignee_phone).send_keys(consigneephone)  # 收货人联系方式赋值
        self.click(self.find(*self._text_consignee_address))  # 选择收货地址的选择按钮
        self.do_Scroll("河北")
        self.do_Scroll("廊坊市")
        self.do_Scroll("三河市")
        self.do_Scroll("燕郊镇")
        self.find(*self._text_consignee_detailed_address).send_keys(consigneedetailsaddress)  # 收货人详细地址框赋值
        self.click(self.find(*self._btn_consignee_save))  # 点击添加新地址按钮

        result = False  # 初始化返回值变量
        namelist = self.finds(*self._list_address_addname)  # 取到收货地址列表中的所有收货人
        for name in namelist:  # 循环判断收货地址列表中的收货人是否有刚新增的收货人，如果有则返回True，否则返回False
            if name.text == tempconsignee:
                result = True
        self._driver.quit()  # 清理环境
        return result

    def edit_address(self):
        pass

    def delete_address(self):
        count_old = len(self.finds(*self._list_address_addname))  # 取到没删之前收货地址列表中的所有收货人个数
        self.click(self.find(*self._btn_edit))  # 点击编辑按钮
        self.click(self.find(*self._btn_del))  # 点击删除按钮
        WebDriverWait(self._driver, 10).until(
            expected_conditions.visibility_of_element_located(self._btn_consignee_save))  # 此句的意义：待列表页面再次加载后再进行后面的最新统计个数
        count_now = len(self.finds(*self._list_address_addname))  # 取到删除之后收货地址列表中的所有收货人个数
        if count_now + 1 == count_old:  # 如果删除后的列表个数+1 = 删除之前的列表个数则返回True,否则返回False
            return True
        else:
            return False
