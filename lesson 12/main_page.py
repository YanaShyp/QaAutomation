from selenium.webdriver.common.by import By
from driver import Driver
from keystofield import KeysToField


class MainPage:
    def __init__(self):
        self.driver = Driver.get_driver()
        driver = Driver.get_driver()
        self.__search_field: KeysToField = None

    def search_field_main(self):
        self.__search_field = KeysToField(self.driver.find_element(By.XPATH, "//input[@placeholder='Я шукаю...']"))

        return self.__search_field
