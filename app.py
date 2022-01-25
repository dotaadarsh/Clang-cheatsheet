import streamlit as st
from streamlit_player import st_player
import streamlit.components.v1 as components


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
with st.sidebar:
     components.html(
    """<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/madmax-ak/Clang-cheatsheet" data-color-scheme="no-preference: dark_high_contrast; light: dark_high_contrast; dark: dark_high_contrast;" data-icon="octicon-star" aria-label="Star madmax-ak/Clang-cheatsheet on GitHub">Star</a>
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>""",
    height=30,)
    
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Create an instance of the app 
app = MultiPage()
st.image("asserts/logo.gif")

# Add all your application here
app.add_page("CHEAT SHEET", cheat_sheet.app)
app.add_page("KEYWORDS", keywords.app)
app.add_page("ARRAYS", arrays.app)
app.add_page("POINTERS", pointers.app)
app.add_page("DATA STRUCTURES", data_structures.app)
app.add_page("PROBLEMS", problems.app)

# The main app
app.run()  


