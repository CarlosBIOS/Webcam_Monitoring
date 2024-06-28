import cv2
import time

video = cv2.VideoCapture(0)
# check1, frame1 = video.read()
# time.sleep(1)
#
# print(frame1)
#
# check2, frame2 = video.read()
# time.sleep(1)
#
# print(frame2)
#
# check3, frame3 = video.read()
# time.sleep(1)
#
# print(frame3)
time.sleep(1)
while True:
    check, frame = video.read()

    # print(check)  # True
    print(frame)
    cv2.imshow('My Video', frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
