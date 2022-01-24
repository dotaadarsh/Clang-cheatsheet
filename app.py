import streamlit as st
from streamlit_player import st_player

# Custom imports 
from multipage import MultiPage
from pages import cheat_sheet, keywords, pointers, arrays, data_structures, problems

st.set_page_config(
     page_title="ZERONITE | C Cheatsheet",
     page_icon="https://zer02infinity.com/assets/images/logo.gif",
     layout="wide",
     initial_sidebar_state="expanded",
 )

st.sidebar.text("> Pre-Alpha version 1.1.1")

# Create an instance of the app 
app = MultiPage()
st.image("/workspace/test-streamlit/asserts/logo.gif")

# Add all your application here
app.add_page("CHEAT SHEET", cheat_sheet.app)
app.add_page("KEYWORDS", keywords.app)
app.add_page("ARRAYS", arrays.app)
app.add_page("POINTERS", pointers.app)
app.add_page("DATA STRUCTURES", data_structures.app)
app.add_page("PROBLEMS", problems.app)

# The main app
app.run()  


