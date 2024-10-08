import cv2

from src.source import Source
from src.pipe import Pipe
from src.sink import Sink

from src.filters.blur_filter import BlurFilter
from src.filters.grayscale_filter import GrayscaleFilter
from src.filters.mirror_filter import MirrorFilter
from src.filters.resize_filter import ResizeFilter


def main():
    source = Source('video.mp4')
    delay = 1000 / source.fps

    pipe1 = Pipe()
    pipe2 = Pipe()
    pipe3 = Pipe()
    pipe4 = Pipe()
    pipe5 = Pipe()

    grayscale_filter = GrayscaleFilter(pipe1, pipe2)
    mirror_filter = MirrorFilter(pipe2, pipe3)
    resize_filter = ResizeFilter(pipe3, pipe4, 1280, 720)
    blur_filter = BlurFilter(pipe4, pipe5)

    sink = Sink()

    try:
        while True:
            frame = source.read()
            if frame is None:
                break

            pipe1.send(frame)

            grayscale_filter.process()
            mirror_filter.process()
            resize_filter.process()
            blur_filter.process()

            processed_frame = pipe5.receive()

            sink.display(processed_frame)

            key = sink.wait_key(delay)
            if key == ord('q'):
                break

            if cv2.getWindowProperty(sink.window_name, cv2.WND_PROP_VISIBLE) < 1:
                break

    finally:
        source.release()
        sink.close()


if __name__ == '__main__':
    main()
