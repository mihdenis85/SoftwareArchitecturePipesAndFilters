import cv2
from src.filter import Filter


class MirrorFilter(Filter):
    def process(self):
        frame = self.input_pipe.receive()
        if frame is not None:
            mirrored = cv2.flip(frame, 0)
            self.output_pipe.send(mirrored)
