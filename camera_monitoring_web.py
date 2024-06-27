# camera_monitoring_web.py
import streamlit as st
import cv2
from datetime import datetime

st.title('Motion Detector')
start = st.button('Start Camera')

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        data = datetime.now().strftime('%A')
        time = datetime.now().strftime('%X')

        cv2.putText(img=frame, text=f'{data}', org=(20, 40), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=f'{time}', org=(20, 75), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)
