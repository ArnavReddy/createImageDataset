import cv2
import time
import numpy as np
from PIL import Image


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0


def wait(image_cropped):
    time.sleep(1)
    cv2.imshow("test", img_cropped)

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    x1, y1, x2, y2 = 100, 100, 500, 500
    k = cv2.waitKey(1)
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (100, 100), (500, 500), (0, 20, 200), 10)
    img_cropped = frame[y1:y2, x1:x2]
    cv2.imshow("img", frame)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        #while(img_counter<=4000):
        img_name = "A{}.png".format(img_counter)
        cv2.imwrite("dataset/A/" + img_name, img_cropped)
        img = Image.fromarray(img_cropped, 'RGB')
        #img.show()
        print("{} written!".format(img_name))
        img_counter += 1
            #wait(img_cropped)

cam.release()

cv2.destroyAllWindows()