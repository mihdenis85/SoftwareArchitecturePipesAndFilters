import cv2
from src.filter import Filter


class ResizeFilter(Filter):
    def __init__(self, width, height):
        super().__init__()
        self.size = (width, height)

    def process(self):
        frame = self.input_pipe.receive()
        if frame is not None:
            resized = cv2.resize(frame, self.size, interpolation=cv2.INTER_AREA)
            self.output_pipe.send(resized)
