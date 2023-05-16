
class Button:
    def __init__(self, button_element):
        self.element = button_element

    def click(self):
        self.element.click()

    def is_displayed(self):
        self.element.is_displayed()

