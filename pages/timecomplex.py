# Load libraries 
import streamlit as st 
import openai
import json 
import os

os.environ = st.secrets["OPENAI_API_KEY"]

def app():
  st.image("https://media1.giphy.com/media/H6bJ3gKixWjFHYscvY/giphy.gif?cid=6c09b952m4j0k0vrp9h9aq20jwgjik9sycvtrv77xtbsn2uj&rid=giphy.gif&ct=ts")

  st.header('Calculate the time complexity of a program')

  txt = st.text_area('Enter the program and press ctrl+Enter to find the complexity', 
  '''
  # Python 3 program for recursive binary search.
  # # Modifications needed for the older Python 2 are found in comments.
 
    # Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1
  ''', height=300,)

  response1 = openai.Completion.create(
  engine="text-davinci-002",
  prompt=txt + "\n\"\"\"\nThe time complexity of this function is",
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
  )

  st.success(response1["choices"][0]["text"])
