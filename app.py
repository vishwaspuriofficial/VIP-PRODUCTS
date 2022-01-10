import streamlit as st
st.set_page_config(layout="wide")
# Custom imports
from pages import MultiPage
from VIP_SUMMARIZER import vip_summarizer
from VIP_QR_DETECTOR import vip_qr_detector
from VIP_QR_GENERATOR import vip_qr_generator
import home

# Create an instance of the app
app = MultiPage()

# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Summarizer", vip_summarizer.app)
app.add_page("QRDetector", vip_qr_detector.app)
app.add_page("QRGenerator", vip_qr_generator.app)

# The main app
app.run()
