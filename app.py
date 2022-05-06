#import libraries
import streamlit as st 
from streamlit_player import st_player
import streamlit.components.v1 as components
from multipage import MultiPage
from pages import cheat_sheet, learn, problems, timecomplex

# Configures the default settings of the page.
st.set_page_config(
     page_title="ZERONITE | C Programming",
     page_icon="https://cdn-icons-png.flaticon.com/512/2617/2617909.png",
     layout="wide",
     initial_sidebar_state="expanded",
 )

st.sidebar.text("> Pre-Alpha version 1.1.1")
with st.sidebar:
     components.html(
    """<a class="github-button" href="https://github.com/madmax-ak/Clang-cheatsheet" data-color-scheme="no-preference: dark_high_contrast; light: dark_high_contrast; dark: dark_high_contrast;" data-icon="octicon-star" aria-label="Star madmax-ak/Clang-cheatsheet on GitHub">Star</a>
<script async defer src="https://buttons.github.io/buttons.js"></script>
<a href="https://twitter.com/madmax_ak?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-screen-name="false" data-show-count="false">Follow @madmax_ak</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
""",
    height=30,)

app = MultiPage() # Create an instance of the app 

st.title("ZERONITE") 

# Calling all applications
app.add_page("CHEAT SHEET", cheat_sheet.app)
app.add_page("LEARN", learn.app)
app.add_page("PROBLEMS", problems.app)
app.add_page("TIME COMPLEXITY", timecomplex.app)

# The main app
app.run()  
