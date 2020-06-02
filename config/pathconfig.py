import os

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取购物主流程的测试数据文件所在路径
CONFIG_DIR = os.path.join(BASE_DIR, "test_case/data")
MAIN_SHOPPING_FLOW_DATA_PATH = os.path.join(CONFIG_DIR, "main_shopping_flow_data.yaml")

# 获取我的->收货地址->新增收货地址测试数据文件所在路径
ADD_ADDRESS_DATA_PATH = os.path.join(CONFIG_DIR, "test_add_address_data.yaml")

# 获取商城->quickenter测试用例所用数据文件所在路径
TEST_SHOPPING_MALL_QUICKENTER_DATA = os.path.join(CONFIG_DIR, "test_shopping_mall_quickenter_data.yaml")

#获取商城quickenter页面元素行为的文件所在路径
STEP_QUICK_ENTER_PAGE_YAML = os.path.join(BASE_DIR, "page/shopping_mall/quick_enter_page.yaml")
