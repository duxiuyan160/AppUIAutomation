from page.base_page import BasePage
from page.profile.consignee_address_page import ConsigneeAddress


class ProfilePage(BasePage):
    #跳转到->收货地址页面
    def goto_consignee_address(self):
        self.do_Scroll("收货地址")  # 滑动屏幕至出现收货地址字样
        return ConsigneeAddress(self._driver)

    #跳转到->待付款页面
    def goto_tobepaid(self):
        pass
