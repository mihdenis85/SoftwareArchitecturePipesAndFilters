class Filter:
    def __init__(self):
        self.input_pipe = None
        self.output_pipe = None

    def set_input(self, input_pipe):
        self.input_pipe = input_pipe

    def set_output(self, output_pipe):
        self.output_pipe = output_pipe

    def process(self):
        pass
