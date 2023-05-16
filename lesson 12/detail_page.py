from button import Button
from selenium.webdriver.common.by import By
from driver import Driver


class DetailPage:
    def __init__(self):
        self.driver = Driver.get_driver()
        driver = Driver.get_driver()
        self.buy_button: Button = None

    def buy_button_detail(self):
        self.buy_button = Button(self.driver.find_element(By.XPATH,
                                   "//*[@class='buy-button button button--with-icon button--green button--medium"
                                   " buy-button--tile ng-star-inserted']"))

        return self.buy_button



