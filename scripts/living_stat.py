class Stat:
    def __init__(self, _type, value):
        self.type = _type
        self.value = value

    def change(self, target_value):
        self.value += target_value