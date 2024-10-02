import cv2
from src.filter import Filter

class GrayscaleFilter(Filter):
    def process(self):
        frame = self.input_pipe.receive()
        if frame is not None:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.output_pipe.send(gray)
