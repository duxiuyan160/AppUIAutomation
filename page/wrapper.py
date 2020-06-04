import logging

from selenium.webdriver.common.by import By


def handle_black(func):
    def wrapper(*args, **kwargs):
        from page.base_page import BasePage
        # 黑名单列表
        _back_list = [
            (By.ID, "com.tojoy.huzhugou:id/btn_pos")  # 主页面弹出的条款框中的同意按钮
        ]
        # 计数器
        _max_num = 3
        _error_num = 0
        instance: BasePage = args[0]  # 到取self的传值
        try:
            logging.info("run " + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0
            #隐式等待回复原来的等待
            instance._driver.implicitly_wait(10)
            return element
        except Exception as e:
            logging.error("element not found, handle black list")
            # 出现异常，将隐式等待设置小一点
            instance._driver.implicitly_wait(1)
            # 判断异常处理次数
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for black in instance._back_list:
                elements = instance.finds(*black)
                if len(elements) > 0:
                    elements[0].click()
                    # 处理完黑名单后，再次找原来的元素
                    return wrapper(*args, **kwargs)
            raise e
    return wrapper
