import sys
import numpy as np
import cv2 as cv
import time
import imutils


def image_to_text(image: np.ndarray) -> str:
    text = ''
    for i in range(image.shape[0]):
        for k in range(image.shape[1]):
            text += "█" if image[i][k] > 0 else ' '
        text += '\n'
    return text.rstrip('\n')


def main() -> None:
    if len(sys.argv) < 2:
        print('Please provide the video path.')
        return

    cap = cv.VideoCapture(sys.argv[1])
    if not cap.isOpened():
        print('Please provide a valid video path.')
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            return

        image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        image = cv.threshold(image, 127, 255, cv.THRESH_BINARY)[1]
        image = imutils.resize(image, width=80)
        image = cv.resize(image, (80, image.shape[0] // 2))

        image_as_text = image_to_text(image)
        # Repeating frames helps reducing flickering in terminal
        print(image_as_text, flush=True)
        time.sleep(0.01)
        print(image_as_text, flush=True)
        time.sleep(0.01)
        print(image_as_text, flush=True)
        time.sleep(0.01)
        print(image_as_text, flush=True)
        time.sleep(0.01)

    cap.release()


if __name__ == '__main__':
    main()
