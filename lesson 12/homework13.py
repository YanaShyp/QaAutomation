from driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_swabber_buy_button_rozetka():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("https://rozetka.com.ua/ua/")
    driver.find_element(By.XPATH, "//input[@placeholder='Я шукаю...']").send_keys(f"швабра {Keys.ENTER}")
    driver.find_element(By.XPATH,
                        "//*[text()=' Миюча Швабра Xiaomi Deerma Spray Mop White (TB500) (З розпилювачем для "
                        "вологого прибирання) ']").click()
    buy_icon = driver.find_element(By.XPATH,
                                   "//*[@class='buy-button button button--with-icon button--green button--medium "
                                   "buy-button--tile ng-star-inserted']")
    assert buy_icon.is_displayed()


test_swabber_buy_button_rozetka()
