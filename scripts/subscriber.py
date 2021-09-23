class Subscriber:
    def __init__(self, broker, types=[]):
        broker.attach(self)
        self.types = types
        self.data = None

    def receive(self, data):
        self.data = data

    def clear(self):
        self.data = None