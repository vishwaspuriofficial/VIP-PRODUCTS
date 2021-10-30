
def app():
    import streamlit as st
    from summarizer import Summarizer
    from threading import Thread
    import time
    import clipboard




    col1, col2 = st.columns(2)

    text = col1.text_area("Enter Text: ",height=200, key="input_placeholder")

    summarize = col1.button("Summarize")

    state = st.session_state

    c2= col2.empty()
    c1 = col1.empty()

    output = c2.empty()

    b = output.text_area("Summarized Text: ", height=200, key="output_placeholder")
    if summarize:
        if text == "":
            col1.error("Error! No text entered.")
        elif len(text) <=50:
            col1.error("Error! Insufficient text for summary.")
        else:
            # try:
            with st.spinner('Summarizing...'):
                model = Summarizer()

                result = model(text, min_length=60)
            if result == "":
                raise TypeError
            state.b = output.text_area("Summarized Text: ", value=result, height=200, key="output_final")
            clipboard.copy(state.b)
            st.success("Output copied to clipboard!")
        # except:
            #     c1.error("Error! Text could not be summarized.")

    time.sleep(2)
    c1.write("")

if __name__ == "__main__":
    app()