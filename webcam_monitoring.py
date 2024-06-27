import cv2
import time
from emailing import send_emails

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
first_frame = None
status_list: list = []
status = 0
motion_detected = False  # Flag to track motion state
time.sleep(2)
while True:
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # vai colocar em gray, pois para comparar é + q suficiente!!
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    # vamos colocar blur, pois não precisamos tanta precisão!!!

    # print(check)  # True
    # print(frame)
    # print(gray_frame_gau)
    # cv2.imshow('My Video', frame)
    # cv2.imshow('My Video', gray_frame_gau)

    if first_frame is None:
        first_frame = gray_frame_gau.copy()
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)  # Dá um contraste nos pixes 'novos'!!
    # cv2.imshow('My Video', delta_frame)
    thresh_value: int = 70
    thresh_frame = cv2.threshold(delta_frame, thresh_value, 255, cv2.THRESH_BINARY)[1]
    # basicamente, se existir algum valor de pelo menos 75, coloca em 255, para tornar-se branco
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # cv2.imshow('My Video', dil_frame)

    counters, _ = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for counter in counters:
        if cv2.contourArea(counter) < 5500:
            continue
        x, y, w, h = cv2.boundingRect(counter)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, h+y), (0, 255, 0), 3)
        motion_detected = True

    # Update status list for motion detection history
    status_list.append(int(motion_detected))
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        message: str = ''
        send_emails(message)
        motion_detected = False  # Reset motion flag

    cv2.imshow('Video', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
