from page.base_page import BasePage
from page.shopping_mall.quick_enter_page import QuickEnterPage


class ShoppingMallPage(BasePage):

    def goto_quick_enter(self):
        return QuickEnterPage(self._driver)