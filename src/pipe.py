class Pipe:
    def __init__(self):
        self.data = None

    def send(self, data):
        self.data = data

    def receive(self):
        return self.data
