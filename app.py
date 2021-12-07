import streamlit as st
from streamlit_player import st_player

# Custom imports 
from multipage import MultiPage
from pages import cheat_sheet, keywords
st.set_page_config(layout="wide")
    
# Create an instance of the app 
app = MultiPage()
st.image("https://zer02infinity.com/assets/images/logo.gif")
st.title("ZERONITE")

# Add all your application here
app.add_page("CHEAT SHEET", cheat_sheet.app)
app.add_page("KEYWORDS", keywords.app)


# The main app
app.run()  


