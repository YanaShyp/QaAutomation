from selenium.webdriver.common.by import By
from driver import Driver
from text import Text


class SearchResultPage:
    def __init__(self):
        self.driver = Driver.get_driver()
        driver = Driver.get_driver()
        self.xiaomi_swabber: Text = None

    def text_element(self):
        self.xiaomi_swabber = Text(self.driver.find_element(By.XPATH, "//*[@class='lite-tile']"))
        return self.xiaomi_swabber
