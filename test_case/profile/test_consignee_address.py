"""
收货地址功能测试用例：
    1、新增收货地址
    2、编辑收货地址
    3、删除收货地址
"""
import pytest
import yaml

from config.pathconfig import ADD_ADDRESS_DATA_PATH
from page.app import App
from page.main import Main


@pytest.mark.usefixtures("init_driver")
class TestConsigneeAddress:
    @pytest.mark.parametrize("consigneedata", yaml.safe_load(open(ADD_ADDRESS_DATA_PATH)))
    def test_add_address(self, init_driver, consigneedata):
        """
        1、点击底部导航栏的我的铵扭
        2、滑屏点击收货地址按钮
        3、点击添加新地址按钮，输入新增收货人信息
        4、保存，并断言
        :param init_driver:
        :param consigneedata:
        :return:
        """
        consignee = consigneedata["consignee"]  # 获取收货人测试数据
        consigneephone = consigneedata["consigneephone"]  # 获取收货人联系方式测试数据
        consigneeaddress = consigneedata["consigneeaddress"]  # 获取收货人地址测试数据
        consigneedetailsaddress = consigneedata["consigneedetailsaddress"]  # 获取收货人详细地址测试数据
        assert init_driver.main().goto_profile().goto_consignee_address().add_address(consignee, consigneephone,
                                                                                      consigneeaddress,
                                                                                      consigneedetailsaddress) == True

    def test_edit_address(self):
        pass

    def test_delete_address(self):
        pass
