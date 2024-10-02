import cv2


class Sink:
    def __init__(self, window_name='Video'):
        self.window_name = window_name
        cv2.namedWindow(self.window_name, cv2.WINDOW_AUTOSIZE)

    def display(self, frame):
        cv2.imshow(self.window_name, frame)

    def wait_key(self, delay=1):
        return cv2.waitKey(int(delay)) & 0xFF

    def close(self):
        cv2.destroyAllWindows()
