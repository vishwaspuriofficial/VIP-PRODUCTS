import streamlit as st


# Define the multipage class to manage the multiple apps in our program
class MultiPage:
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages = []

    def add_page(self, title, func) -> None:
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps

            func: Python function to render this page in Streamlit
        """

        self.pages.append({

            "title": title,
            "function": func
        })

    def run(self):
        try:
            query_params = st.experimental_get_query_params()
            page = query_params['page'][0]
            ind = 0
            if page == "summarizer":
                ind = 1
            elif page == "qr":
                ind = 2
            else:
                ind = 0
        except:
            ind = 0

        format_func = self.pages[ind]
        page = format_func['title']
        function = format_func['function']
        page, function()
