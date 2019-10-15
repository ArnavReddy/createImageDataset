import cv2
import time
import numpy as np
from PIL import Image
import sys
import os

if os.path.isdir("dataset"):
    print("dataset directory exists")
else:
    print("dataset directory is being created")
    try:
        os.chmod(os.getcwd(), 0o777)
        #original_umask = os.umask(0)
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        i = 0
        while i < len(letters):
            print(letters[i].upper() + " directory is being created")
            os.makedirs("./dataset/"+letters[i].upper(), 0o777)
            i += 1
    except OSError:
        print ("Creation of all of the directories failed")
    else:
       print ("Successfully created all of the directories")

letter = input('What letter are you going to take pictures of: ')
list = os.listdir("./dataset/"+letter) # dir is your directory path
img_counter = len(list)
print("The next image taken will be #"+str(img_counter)+" in the /dataset/"+letter+ " directory" )

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

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
    img_cropped = frame[y1+10:y2-10, x1+10:x2-10]
    cv2.imshow("img", frame)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        #while(img_counter<=4000):
        img_name = letter+"{}.png".format(img_counter)
        cv2.imwrite("dataset/"+letter+"/" + img_name, img_cropped)
        img = Image.fromarray(img_cropped, 'RGB')
        #img.show()
        print("{} written!".format(img_name))
        img_counter += 1
        #wait(img_cropped)

cam.release()

cv2.destroyAllWindows()