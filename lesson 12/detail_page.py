from button import Button
from selenium.webdriver.common.by import By
from driver import Driver


class MainPage:
    def __init__(self):
        driver = Driver.get_driver()
        self.buy_button = Button(driver.find_element(By.XPATH,
                                   "//*[@class='buy-button button button--with-icon button--green button--medium "
                                   "buy-button--tile ng-star-inserted']"))

