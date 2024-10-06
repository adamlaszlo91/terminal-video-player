import sys
import numpy as np
import cv2 as cv
import time
import imutils

value_to_character_map = '█$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\' '[::-1]


def image_to_text(image: np.ndarray) -> str:
    text = ''
    for i in range(image.shape[0]):
        for k in range(image.shape[1]):
            greyscale_value = image[i][k]
            text += value_to_character_map[int(
                (len(value_to_character_map) - 1) * (greyscale_value / 255))]
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
        image = imutils.resize(image, width=80)
        image = cv.resize(image, (80, image.shape[0] // 2))

        image_as_text = image_to_text(image)
        # Repeating frames helps reducing the flickers in terminal
        print(image_as_text, flush=True)
        time.sleep(0.02)
        print(image_as_text, flush=True)
        time.sleep(0.02)

    cap.release()


if __name__ == '__main__':
    main()
