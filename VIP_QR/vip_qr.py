# import streamlit as st
# import cv2
# import mediapipe as mp
# import time
# import numpy as np
#
#
# try:
#     detector = cv2.QRCodeDetector()
#
#     from streamlit_webrtc import (
#         AudioProcessorBase,
#         RTCConfiguration,
#         VideoProcessorBase,
#         WebRtcMode,
#         webrtc_streamer,
#     )
#     try:
#         from typing import Literal
#     except ImportError:
#         from typing_extensions import Literal  # type: ignore
#     import av
#
#     RTC_CONFIGURATION = RTCConfiguration(
#         {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
#     )
#     st.write("Press start to start scanning for QR code")
#     st.write("If camera doesn't turn on, click the select device button and change the camera input!")
#
#     def handDetector():
#         class OpenCVVideoProcessor(VideoProcessorBase):
#             type: Literal["hand"]
#
#             def __init__(self) -> None:
#                 self.type = "hand"
#
#             def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
#
#                 img = frame.to_ndarray(format="bgr24")
#
#                 data, bbox, straight_qrcode = detector.detectAndDecode(img)
#                 if bbox is not None:
#                     print(f"QRCode data:\n{data}")
#                     # display the image with lines
#                     # length of bounding box
#                     n_lines = len(bbox)
#                     for i in range(n_lines):
#                         # draw all lines
#                         point1 = tuple(bbox[i][0])
#                         point2 = tuple(bbox[(i + 1) % n_lines][0])
#                         cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
#                 else:
#                     print("QR Code not detected")
#                 st.write(data)
#
#                 return av.VideoFrame.from_ndarray(img, format="bgr24")
#
#         webrtc_ctx = webrtc_streamer(
#             key="opencv-filter",
#             mode=WebRtcMode.SENDRECV,
#             rtc_configuration=RTC_CONFIGURATION,
#             video_processor_factory=OpenCVVideoProcessor,
#             media_stream_constraints={"video":True,"audio": False},
#             async_processing=True,
#             video_html_attrs={
#                 "style": {"margin": "0 auto", "border": "5px yellow solid"},
#                 "controls": False,
#                 "autoPlay": True,
#             },
#         )
#         if webrtc_ctx.video_processor:
#             webrtc_ctx.video_processor.type = "hand"
#
# except:
#     st.error("Unknow Error Encountered!")
# if __name__ == "__main__":
#     handDetector()


import cv2

image = cv2.imread('QR.png')

qrCodeDetector = cv2.QRCodeDetector()

decodedText, points, _ = qrCodeDetector.detectAndDecode(image)

if points is not None:

    nrOfPoints = len(points)

    for i in range(nrOfPoints):
        nextPointIndex = (i + 1) % nrOfPoints
        cv2.line(image, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255, 0, 0), 5)

    print(decodedText)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


else:
    print("QR code not detected")