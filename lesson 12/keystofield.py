class KeysToField:
    def __init__(self, input_element):
        self.element = input_element

    def send_keys(self):
        self.element.send_keys()
