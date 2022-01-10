def app():
    import streamlit as st
    # import qrcode
    from PIL import Image
    import numpy as np
    from MyQR import myqr as mq


    text = st.text_input('Make a QR code of:')
    a = st.button("Create QR Code")
    if a:
        try:
            mq.run(text, save_name='qr.png')
            # img = qrcode.make(text)
            # img.save("qr.png")
            st.subheader("Your QR Code is ready!")
            st.image("qr.png")

            # st.download_button('Download QR Code', img)
            st.write('To Save, right-click on the QR code and click "save image as"')

        except Exception as e:
            st.exception(e)
            st.error("Error Occured! Your QR Code could not be made!")

        st.balloons()

if __name__ == "__main__":
    app()