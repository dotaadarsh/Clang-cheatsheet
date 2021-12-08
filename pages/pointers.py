# Load important libraries 
import pandas as pd
import streamlit as st 
from streamlit_player import st_player
import os


def app():

  st.header('POINTERS')
  st.caption("The pointer in C language is a variable which stores the address of another variable. This variable can be of type int, char, array, function, or any other pointer. The size of the pointer depends on the architecture. However, in 32-bit architecture the size of a pointer is 2 byte.")

  topics = st.sidebar.radio("TOPICS",("Intro", "Working with pointers", "Pointer types, pointer arithmetic, void pointer", "pointers to pointers", "Pointers as function arguments - call by ref", "Pointer & Arrays", "arrays as function arguments", "Char array and pointers", "Pointer and 2D arrays","Pointers and multi-D array", "Stack vs heap", "Malloc-Calloc-Realloc-Free", "Pointers as function returns", "Fucntion Pointers", "Function Pointer & callbacks", "Memory leak"))

  if topics == 'Intro':
     st.write('You selected intro')
     st_player("https://youtu.be/zuegQmMdy8M?t=0")

  elif topics == 'Working with pointers':
     st.write("Working with pointers")
     st_player("https://youtu.be/zuegQmMdy8M?t=629")
     
  elif topics == 'Pointer types, pointer arithmetic, void pointer':
     st.write("Pointer types, pointer arithmetic, void pointer")
     st_player("https://youtu.be/zuegQmMdy8M?t=1325")

  elif topics == 'pointers to pointers':
     st.write("pointers to pointers")
     st_player("https://youtu.be/zuegQmMdy8M?t=1981")

  elif topics == 'Pointers as function arguments - call by ref':
     st.write("Pointers as function arguments - call by ref")
     st_player("https://youtu.be/zuegQmMdy8M?t=2541")


  elif topics == 'Pointer & Arrays':
     st.write("Pointer & Arrays")
     st_player("https://youtu.be/zuegQmMdy8M?t=3396")


  elif topics == 'arrays as function arguments':
     st.write("arrays as function arguments")
     st_player("https://youtu.be/zuegQmMdy8M?t=3918")


  elif topics == 'Char array and pointers':
     st.write("Char array and pointers")
     st_player("https://youtu.be/zuegQmMdy8M?t=4690")
     st_player("https://youtu.be/zuegQmMdy8M?t=5569")


  elif topics == 'Pointer and 2D arrays':
     st.write("Pointer and 2D arrays")
     st_player("https://youtu.be/zuegQmMdy8M?t=6169")

  elif topics == 'Pointers and multi-D array':
     st.write("Pointers and multi-D array")
     st_player("https://youtu.be/zuegQmMdy8M?t=6907")


  elif topics == 'Stack vs heap':
     st.write("Stack vs heap")
     st_player("https://youtu.be/zuegQmMdy8M?t=7910")


  elif topics == 'Malloc-Calloc-Realloc-Free':
     st.write("Malloc-Calloc-Realloc-Free")
     st_player("https://youtu.be/zuegQmMdy8M?t=8954")

  elif topics == 'Pointers as function returns':
     st.write("Pointers as function returns")
     st_player("https://youtu.be/zuegQmMdy8M?t=9408")
  
  elif topics == 'Fucntion Pointers':
     st.write("Fucntion Pointers")
     st_player("https://youtu.be/zuegQmMdy8M?t=10921")
  

  elif topics == 'Function Pointer & callbacks':
     st.write("Function Pointer & callbacks")
     st_player("https://youtu.be/zuegQmMdy8M?t=11637")

  elif topics == 'Memory leak':
     st.write("Memory leak")
     st_player("https://youtu.be/zuegQmMdy8M?t=12556")

  else:
     st.write("Choose the Topics in the sidebar")
