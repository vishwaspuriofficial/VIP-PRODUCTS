# def app():
#     import streamlit as st
#     from transformers import pipeline
#     import time
#     #import clipboard
#
#     def summary(text):
#         summarizer = pipeline("summarization")
#
#         summarized = summarizer(text, min_length=25, max_length=300)
#
#         for i in summarized:
#             for j in i:
#                 result = i[j]
#                 return result
#
#     col1, col2 = st.columns(2)
#
#     text = col1.text_area("Enter Text: ",height=200, key="input_placeholder")
#
#     summarize = col1.button("Summarize")
#
#     state = st.session_state
#
#     c2= col2.empty()
#     c1 = col1.empty()
#
#     output = c2.empty()
#
#     b = output.text_area("Summarized Text: ", height=200, key="output_placeholder")
#     if summarize:
#         if text == "":
#             st.error("Error! No text entered.")
#         elif len(text) <=50:
#             st.error("Error! Insufficient text for summary.")
#         else:
#             try:
#                 with st.spinner('Summarizing...'):
#                     result = summary(text)
#                 if result == "":
#                     raise TypeError
#                 state.b = output.text_area("Summarized Text: ", value=result, height=200, key="output_final")
#                 #clipboard.copy(state.b)
#                 #st.success("Output copied to clipboard!")
#             except:
#                 st.error("Error! Text could not be summarized.")
#                 #st.exception(RuntimeError)
#
#     time.sleep(2)
#     c1.write("")
#
# if __name__ == "__main__":
#     app()

def app():
    import streamlit as st
    from gensim.summarization import summarize
    import time
    # import clipboard

    col1, col2 = st.columns(2)

    text = col1.text_area("Enter Text: ",height=200, key="input_placeholder")

    summarizeBtn = col1.button("Summarize")

    state = st.session_state

    c2= col2.empty()
    c1 = col1.empty()

    output = c2.empty()

    b = output.text_area("Summarized Text: ", height=200, key="output_placeholder")
    if summarizeBtn:
        if text == "":
            st.error("Error! No text entered.")
        elif len(text) <=50:
            st.error("Error! Insufficient text for summary.")
        else:
            try:
                with st.spinner('Summarizing...'):
                    result = summarize(text)
                    time.sleep(1)
                if result == "":
                    raise TypeError
                state.b = output.text_area("Summarized Text: ", value=result, height=200, key="output_final")
                # clipboard.copy(state.b)
                # st.success("Output copied to clipboard!")
            except:
                st.error("Error! Text could not be summarized.")


    time.sleep(2)
    c1.write("")

if __name__ == "__main__":
    app()