def app():
    import streamlit as st
    import pyzbar.pyzbar as pyzbar
    import webbrowser
    import time
    import cv2
    # st.set_page_config(layout="wide")
    col = st.empty()

    from streamlit_webrtc import (
        AudioProcessorBase,
        RTCConfiguration,
        VideoProcessorBase,
        WebRtcMode,
        webrtc_streamer,
    )
    try:
        from typing import Literal
    except ImportError:
        from typing_extensions import Literal  # type: ignore
    import av

    RTC_CONFIGURATION = RTCConfiguration(
        {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    )
    st.write("Press start to turn on your camera and show it your hands!")


    class OpenCVVideoProcessor(VideoProcessorBase):
        def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
            img = frame.to_ndarray(format="bgr24")

            # font = cv2.FONT_HERSHEY_PLAIN
            barcodes = pyzbar.decode(img)
            for barcode in barcodes:
                x, y, w, h = barcode.rect
                # 1
                data = str(barcode.data).split("'")[1]
                print(barcode)

                if barcode.type == "QRCODE":
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(img, data, (30, 50), font, 0.5, (255, 255, 255), 1)
                    webbrowser.open(data)
                    time.sleep(5)



            return av.VideoFrame.from_ndarray(img, format="bgr24")

    webrtc_ctx = webrtc_streamer(
        key="opencv-filter",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        video_processor_factory=OpenCVVideoProcessor,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
        video_html_attrs={
            "style": {"margin": "0 auto", "border": "5px yellow solid"},
            "controls": False,
            "autoPlay": True,
        },
    )

    # Info Block
    st.write("If camera doesn't turn on, please ensure that your camera permissions are on!")
    with st.expander("Steps to enable permission"):
        st.write("1. Click the lock button at the top left of the page")
        st.write("2. Slide the camera slider to on")
        st.write("3. Reload your page!")

if __name__ == "__main__":
    app()