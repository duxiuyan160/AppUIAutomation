import pytest

from appium import webdriver


@pytest.mark.usefixtures("init_driver")
class TestMainShoppingFlow:

    def test_mainshoppingflow(self, init_driver):
        """
        执行用例：验证码登录->首页搜索商品->商品展示->商品加入购物车->结算->提交订单，并断言
        :param init_driver:
        :return:
        """
        assert "支付剩余时间" in init_driver.main().goto_mainshoppingflow().MainShoppingFlow()
