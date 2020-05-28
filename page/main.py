"""
主页面，进行分管跳转到各个模块
"""
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.profile.profile_page import ProfilePage


class Main(BasePage):
    _btn_my = (By.ID, "com.tojoy.huzhugou:id/navigation_me")  # 底部导航栏我的按钮

    # 跳转主流程购物页面
    def goto_mainshoppingflow(self):
        pass

    # 跳转到我的页面
    def goto_profile(self):
        # 点击底部导航栏的我的按钮
        self.click(self.find(*self._btn_my))
        return ProfilePage(self._driver)
