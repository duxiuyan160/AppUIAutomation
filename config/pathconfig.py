import os

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取购物主流程的测试数据文件所在路径
CONFIG_DIR = os.path.join(BASE_DIR, "test_case/data")
MAIN_SHOPPING_FLOW_DATA_PATH = os.path.join(CONFIG_DIR, "main_shopping_flow_data.yaml")

# 获取我的->收货地址->新增收货地址测试数据文件所在路径
TESTCASE_DATA_DIR = os.path.join(BASE_DIR, "test_case/data")
ADD_ADDRESS_DATA_PATH = os.path.join(TESTCASE_DATA_DIR, "add_address_data.yaml")
