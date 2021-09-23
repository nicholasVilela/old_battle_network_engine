class Publisher:
    def __init__(self, broker):
        self.broker = broker

    def publish(self, data):
        self.broker.route(data)

class PublisherData:
    def __init__(self, data, data_type):
        self.data = data
        self.data_type = data_type