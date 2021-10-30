import streamlit as st
st.set_page_config(layout="wide")
# Custom imports
from pages import MultiPage
from VIP_PRODUCTS import VIP_SUMMARIZER
from VIP_SUMMARIZER import vip_summarizer
from VIP_QR import vip_qr
import home

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Multi-page Application")

# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Summarizer", vip_summarizer.app)
app.add_page("QR", vip_qr.app)

# The main app
app.run()
