import streamlit as st
from streamlit_player import st_player

# Custom imports 
from multipage import MultiPage
from pages import cheat_sheet, keywords, pointers

st.set_page_config(
     page_title="ZERONITE",
     page_icon="https://zer02infinity.com/assets/images/logo.gif",
     layout="wide",
     initial_sidebar_state="expanded",
 )

# Create an instance of the app 
app = MultiPage()
st.image("https://zer02infinity.com/assets/images/logo.gif")
st.title("ZERONITE")

# Add all your application here
app.add_page("CHEAT SHEET", cheat_sheet.app)
app.add_page("KEYWORDS", keywords.app)
app.add_page("POINTERS", pointers.app)


# The main app
app.run()  


