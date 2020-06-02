from config.pathconfig import STEP_QUICK_ENTER_PAGE_YAML
from page.base_page import BasePage


class QuickEnterPage(BasePage):
    _step_url = STEP_QUICK_ENTER_PAGE_YAML  # 要操作的页面元素的地址

    # 根据quicktype去跳转到不同的类别页面，并且根据quicktype操作不同的页面元素行为。
    def quickentertype(self, quicktype):
        self._params["name"] = quicktype
        self.steps(self._step_url)

    # 公共的加入购物车、添加数量、结算、提交订单方法
    def common(self, quickitem):
        self._params["name"] = quickitem
        return self.steps(self._step_url)
