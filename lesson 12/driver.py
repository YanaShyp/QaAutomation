from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Driver:

    driver = None

    @staticmethod
    def get_driver() -> WebDriver:
        if Driver.driver is None:
            Driver.driver = webdriver.Chrome()
            return Driver.driver
        else:
            return Driver.driver
