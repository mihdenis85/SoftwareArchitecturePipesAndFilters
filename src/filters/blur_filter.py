import cv2

from src.filter import Filter


class BlurFilter(Filter):
    def process(self):
        frame = self.input_pipe.receive()
        if frame is not None:
            result = cv2.GaussianBlur(frame, (15, 15), 0)
            self.output_pipe.send(result)
