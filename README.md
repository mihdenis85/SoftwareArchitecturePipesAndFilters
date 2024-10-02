# Software Architecture: Pipes And Filters

This project is a simple video processing pipeline implemented in Python using OpenCV and pipes and filters pattern. It
reads a video file, applies a series of filters to each frame, and displays the processed video in real-time.

## Agenda

* [Demo](#demo)
* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Project Structure](#project-structure)
* [Filters Overview](#filters-overview)
* [Customization](#customization)
* [Contacts](#contacts)

## Demo
https://youtube.com/watch?v=uApwUcxGCiM

## Features

- Blur Filter: Applies Gaussian blur to video frames.
- Grayscale Filter: Converts video frames to grayscale.
- Mirror Filter: Mirrors video frames.
- Resize Filter: Resizes video frames to the given size.

## Prerequisites

- Python 3.10+
- OpenCV (cv2 module)

## Installation

1. Clone the repository:

```shell
git clone https://github.com/mihdenis85/SoftwareArchitecturePipesAndFilters.git
```

2. Install the required packages:

```shell
pip install -r requirements.txt
```

## Usage

1. Place your video file (or keep existing):

   Update the path in main.py:

```python
source = Source('video.mp4')
```

2. Run the script:

```shell
python main.py
```

3. Controls:

    - Press 'q' or just close the window to exit the video playback.

## Project Structure

```
├── src
│   ├── filters
│   │   ├── __init__.py
│   │   ├── blur_filter.py
│   │   ├── grayscale_filter.py
│   │   ├── mirror_filter.py
│   │   └── resize_filter.py
│   ├── __init__.py
│   ├── filter.py
│   ├── pipe.py
│   ├── sink.py
│   └── source.py
├── main.py
├── .gitignore
├── README.md
├── requirements.txt
└── video.mp4
```

## Filters Overview

### GrayscaleFilter

Converts the input frame to grayscale using OpenCV's cv2.cvtColor() function.

### MirrorFilter

Mirrors the input frame horizontally using OpenCV's cv2.flip() function with flip code 1.

### ResizeFilter

Resizes the input frame to specified width and height using OpenCV's cv2.resize() function.

### BlurFilter

Applies a Gaussian blur to the input frame using OpenCV's cv2.GaussianBlur() function with a kernel size of (5, 5).

## Customization

- Adding More Filters:

  You can add more filters by creating new Python files in the filters directory. Each filter should define a class with
  a process(frame) method that takes an input frame and returns the processed frame.

### Example: src/filters/your_filter.py

```python

import cv2
from src.filter import Filter


class BlurFilter(Filter):
    def process(self):
        frame = self.input_pipe.receive()
        if frame is not None:
            # Paste cv2.<some_filter> instead of None
            result = None  # cv2.SomeFilter()
            self.output_pipe.send(result)

```

- Modifying the Filter Pipeline:

  In main.py, you can modify the order in which filters are applied or add/remove filters from the pipeline.

## Contacts

- Denis Mikhailov - d.mikhailov@innopolis.university
- Anton Chulakov - a.chulakov@innopolis.university
- Adel Shagaliev - a.shagaliev@innopolis.iniversity
- Ilya Zubkov - i.zubkov@innopolis.university
