# Load libraries 
import streamlit as st 
from streamlit_player import st_player


def app():

  st.header('EXAMPLES')
  st.caption("An array is defined as the collection of similar type of data items stored at contiguous memory locations. Arrays are the derived data type in C programming language which can store the primitive type of data such as int, char, double, float, etc. It also has the capability to store the collection of derived data types, such as pointers, structure, etc. The array is the simplest data structure where each data element can be randomly accessed by using its index number.")

  st.image("https://i1.faceprep.in/fp/articles/img/29757_1580126593.png", caption="Preferred Approach")

  option = st.sidebar.radio(
            'Topics', ('Basics', 'Loops', 'number Crunching', 'Arrays', 'Pointers', 'Recursion','File and Streams', 'Misc-1', 'Misc-2')
        ) 
  st.write('You selected:', option)
  
  if option == 'Basics':
    st.write("BASICS")

    
    with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.markdown('```Sample testcases```\n > fsfsdf')
     st.image("https://static.streamlit.io/examples/dice.jpg")