class KeysToField:
    def __init__(self, input_element):
        self.element = input_element

    def send_keys(self, text_to_fill):
        self.element.send_keys(text_to_fill)
