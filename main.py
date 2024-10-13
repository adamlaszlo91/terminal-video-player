import sys
import numpy as np
import cv2 as cv
import time
import imutils

ascii_chars = '█$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\' '[::-1]


def image_to_text(image: np.ndarray) -> str:
    text = ''
    for i in range(image.shape[0]):
        text += '\n'
        for k in range(image.shape[1]):
            greyscale_value = image[i][k]
            char_index = int((greyscale_value / 256) * (len(ascii_chars)))
            text += ascii_chars[char_index]
    return text


def reset_cursor(height: int) -> None:
    print(f'\033[{height}A', flush=True)


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
            cap.release()
            return

        image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Set a correct size and aspect ration for terminal
        image = imutils.resize(image, width=80)
        image = cv.resize(image, (80, image.shape[0] // 2))

        image_as_text = image_to_text(image)
        print(image_as_text, end='', flush=True)
        reset_cursor(height=image.shape[1])

        time.sleep(0.04)


if __name__ == '__main__':
    main()
