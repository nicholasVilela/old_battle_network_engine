class Broker:
    def __init__(self):
        self.subscribers = []

    def attach(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def detach(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def route(self, data):
        for subscriber in self.subscribers:
            if data.data_type in subscriber.types:
                subscriber.receive(data)