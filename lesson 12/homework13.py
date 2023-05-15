from driver import Driver
from selenium.webdriver.common.keys import Keys
from detail_page import DetailPage
from search_result_page import SearchResultPage
from main_page import MainPage


class TestSwabberRozetka:

    def setup_class(self):
        self.driver = Driver.get_driver()
        self.search_result_page = SearchResultPage()
        self.main_page = MainPage()
        self.detail_page = DetailPage()

    def setup_method(self):
        self.driver.get("https://rozetka.com.ua/ua/")
        self.driver.implicitly_wait(2)

    def test_swabber_buy_button_rozetka(self):
        self.main_page.search_field_main().send_keys(f"швабра {Keys.ENTER}")
        self.search_result_page.text_element().click()
        assert self.detail_page.buy_button_detail().is_displayed()

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.driver.quit()


