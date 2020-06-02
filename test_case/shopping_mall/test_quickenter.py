import json

import pytest
import yaml

from config.pathconfig import TEST_SHOPPING_MALL_QUICKENTER_DATA


@pytest.mark.usefixtures("init_driver")
class TestQuickEnter:
    @pytest.mark.parametrize("quickentertype",
                             yaml.safe_load(open(TEST_SHOPPING_MALL_QUICKENTER_DATA, encoding="utf-8")))
    def test_quickenter(self, quickentertype, init_driver):
        """
        1、选择如下类型的商品，进入商品展示页面
            - 食品酒水: "青岛啤酒7天原浆"
            - 生鲜特产: "春雪水蜜桃"
            - 电脑办公: "华为(HUAWEI)MateBook 14"
            - 数码电器: "华为 HUAWEI Mate 30 5G"
            - 美妆个护: "雪花秀滋盈肌本护肤礼盒"
            - 母婴保健: "同仁堂牌警醒片"
            - 箱包配饰: "Longchamp珑骧 女士手提包大号短柄"
        2、点击加入购物车--》加数量--》结算--》提交订单 操作
        :param quickentertype:
        :param init_driver:
        :return:
        """
        self.quickenter = init_driver.main().goto_shoppingmall().goto_quick_enter()
        print(quickentertype.keys())
        for key, value in quickentertype.items():
            self.quickenter.quickentertype(key)
            assert "支付剩余时间" in self.quickenter.common(value)
