import pytest
from selenium.webdriver.common.by import By
from appium import webdriver

from page.app import App


@pytest.fixture("class")
def init_driver():
    """
    实例化driver
    :return:
    """
    app = App()
    driver = app.start()
    yield driver
