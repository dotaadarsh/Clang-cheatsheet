# Load libraries 
import streamlit as st 
from streamlit_player import st_player
import streamlit.components.v1 as components

def app():

  '''components.html(
    """<div style="width:100%;height:0;padding-bottom:65%;position:relative;"><iframe src="https://giphy.com/embed/hvN3SkNMRSB7mZa8JL" width="50%" height="50%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/working-busy-under-construction-hvN3SkNMRSB7mZa8JL">via GIPHY</a></p>""", height=600,)'''

  option = st.sidebar.radio(
            'LEC #', ('Introduction',
            'Variables and datatypes, operators',
            'Control flow | Part - 1',
            'Control flow | Part - 2',
            'Pointers, Arrays, Strings, Searching and sorting algorithms',
            'User-defined datatypes & Data structure', 
            'Pointers++ + Data Structures++', 
            'Void and function pointers & Hash tables', 
            'External libraries, B-trees & priority queues', 
            'C standard library', 
            'Dynamic memory allocation & garbage collection', 
            'Multithreading & concurrency',
            'Multithreaded programming. Sockets and asynchronous I/O',
            'Linux inter process communication'
            )
            ) 
  
  def option_media():

    option_media = st.selectbox(
     'How would you like view the content?',
     ('TEXT', 'VIDEO', 'PODCAST'))
    return option_media

  def Credit():
    st.markdown('Credit: MIT OpenCourseWare | (Attribution-NonCommercial-ShareAlike 4.0 International CC BY-NC-SA 4.0)[https://creativecommons.org/licenses/by-nc-sa/4.0/]')
  
  # Introduction 
  if option == 'Introduction' :
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/b7f13dd2771c6e8557e0877457d07543_MIT6_087IAP10_lec01.pdf" width="1050" height="800">""", unsafe_allow_html=True)
      Credit()      

    if option_media == 'VIDEO':
      st_player('https://youtu.be/s0g4ty29Xgg', height=500)

    if option_media == 'PODCAST':
      st.info("Will try to work on it")

  # Flow of control
  if option == 'Variables and datatypes, operators' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/ab99b303a22349b7830a31eca6310fee_MIT6_087IAP10_lec02.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      with st.expander('Data types, Constants and Variables'):
        st_player('https://youtu.be/OSyjOvFbAGI', height=400)

      with st.expander('Operators in C'):
        st_player('https://www.youtube.com/playlist?list=PLBlnK6fEyqRhqQV_MzlT8xsPQnsGcMdIo', height=400)

    if option_media == 'PODCAST':
      st.info("Will try to work on it")

  # Control flow | Part - 1
  if option == 'Control flow | Part - 1' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/6ef53f22595564c47c0c377ef8bd5398_MIT6_087IAP10_lec03.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      with st.expander('Conditionals (if-else, Nested if and else if)'):
        st_player('https://youtu.be/Led5aHdLoT4?list=PLBlnK6fEyqRhX6r2uhhlubuF5QextdCSM', height=400)

      with st.expander('Conditionals (Switch)'):
        st_player('https://youtu.be/-JMSaLRqsgo?list=PLBlnK6fEyqRhX6r2uhhlubuF5QextdCSM', height=400)

      with st.expander('for and while Loops'):
        st_player('https://youtu.be/qUPXsPtWGoY?list=PLBlnK6fEyqRhX6r2uhhlubuF5QextdCSM', height=400)

      with st.expander('do-while Loop'):
        st_player('https://youtu.be/TjkJQly2YCw?list=PLBlnK6fEyqRhX6r2uhhlubuF5QextdCSM', height=400)

      with st.expander('Loop Control Statements − break and continue'):
        st_player('https://youtu.be/obJcPlAtGVM?list=PLBlnK6fEyqRhX6r2uhhlubuF5QextdCSM', height=400)

      with st.expander('Functions in C'):
        st_player('https://www.youtube.com/playlist?list=PLBlnK6fEyqRi0Va6znG73P52rFfXD5fhs', height=400)
        st.write('Its a playlist- so play the next videos in oreder to learn all the content')

    if option_media == 'PODCAST':
      st.info("Will try to work on it")
      
  # Control flow | Part - 2
  if option == 'Control flow | Part - 2' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/262cf4e05f039e45c926109c8aa95024_MIT6_087IAP10_lec04.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      with st.expander('Error Handling'):
        st_player('https://youtu.be/rMfp6gKR_kk', height=400)

      with st.expander('Input and Output: Printf and Scanf'):
        st_player('https://youtu.be/xOIVXR35aI4', height=400)

      with st.expander('File I/O: Create, Open, Write and Close a File'):
        st_player('https://youtu.be/e-srF6c3TJ8', height=400)

    if option_media == 'PODCAST':
      st.info("Will try to work on it")

  # Pointers, Arrays, Strings, Searching and sorting algorithms
  if option == 'Pointers, Arrays, Strings, Searching and sorting algorithms' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/d5a4c815a3f931d7efca0f4fb1a7604f_MIT6_087IAP10_lec05.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      
      with st.expander('Understanding Arrays in C'):
        st_player('https://youtu.be/0EgpeYB115s', height=400)

      with st.expander('Understanding Strings in C'):
        st_player('https://youtu.be/l7zI3nswO1g?list=PL98qAXLA6aftD9ZlnjpLhdQAOFI8xIB6e', height=400)

      with st.expander('What is virtual memory?'):
        st_player('https://youtu.be/2quKyPnUShQ', height=400)
 
      with st.expander('Linear search algorithm'):
        st_player('https://youtu.be/EqWpRlZkWNM', height=400)

      with st.expander('Binary search algorithm'):
        st_player('https://youtu.be/MFhxShGxHWc', height=400)
  
      with st.expander('Insertion sort algorithm'):
        st_player('https://youtu.be/i-SKeOcBwko', height=400)

      with st.expander('Quicksort algorithm'):
        st_player('https://youtu.be/COk73cpQbFQ', height=400)




    if option_media == 'PODCAST':
      st.info("Will try to work on it")
      
  # User-defined datatypes & Data structure
  if option == 'User-defined datatypes & Data structure' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/1aa34decd30f336826cd087d2f52035b_MIT6_087IAP10_lec06.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      with st.expander('Structures & Unions'):
        st_player('https://youtu.be/KL65a0TyeYo', height=400)

      with st.expander('Bit fields'):
        st_player('https://youtu.be/3Xxixs3zLUo', height=400)
 
      with st.expander('Introduction to Linked List'):
        st_player('https://youtu.be/B31LgI4Y4DQ?t=1183', height=400)

      with st.expander('Arrays vs Linked Lists'):
        st_player('https://youtu.be/B31LgI4Y4DQ?t=2230', height=400)

      with st.expander('Linked List - Implementation in C/C++'):
        st_player('https://youtu.be/vcQIFT79_50', height=400)

      with st.expander('Single Linked List (Inserting a Node at the Beginning)'):
        st_player('https://youtu.be/jgqg6Qw68_Q', height=400)
 
      with st.expander('Single Linked List (Inserting a Node at a Certain Position)'):
        st_player('https://youtu.be/0hGxILnKvJk', height=400)

      with st.expander('Delete a node at nth position'):
        st_player('https://youtu.be/Y0n86K43GO4', height=400)
  
      with st.expander('Reverse a linked list - Iterative method'):
        st_player('https://youtu.be/sYcOK51hl-A', height=400)

      with st.expander('Reverse a linked list - Recursion method'):
        st_player('https://youtu.be/B31LgI4Y4DQ?t=7937', height=400)
 
      with st.expander('Binary Tree'):
        st_player('https://youtu.be/H5JubkIy_p8', height=400)

    if option_media == 'PODCAST':
      st.info("Will try to work on it")
     
  # Pointers++ + Data Structures++
  if option == 'Pointers++ + Data Structures++' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/afdb632076595f216692b04cafae216c_MIT6_087IAP10_lec07.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      with st.expander('Introduction to Stacks'):
        st_player('https://youtu.be/I37kGX-nZEI', height=400)
     
      with st.expander('Array implementation of stacks'):
        st_player('https://youtu.be/sFVxsglODoo', height=400)

      with st.expander(' Linked List implementation of stacks'):
        st_player('https://youtu.be/MuwxQ2IB8lQ', height=400)
 
      with st.expander('Queues in C '):
        st_player('https://youtu.be/p-oNr0Z4PcM', height=400)

      with st.expander('Array implementation of Queue'):
        st_player('https://youtu.be/okr-XE8yTO8', height=400)

      with st.expander('Linked List implementation of Queue'):
        st_player('https://www.youtube.com/watch?v=A5_XdiK4J8A', height=400)

      with st.expander('Infix, Prefix and Postfix'):
        st_player('https://youtu.be/jos1Flt21is', height=400)

    if option_media == 'PODCAST':
      st.info("Will try to work on it")
      
  # Void and function pointers & Hash tables
  if option == 'Void and function pointers & Hash tables' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/02aef29b821a0258e53ba95a648207f9_MIT6_087IAP10_lec08.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      with st.expander('Understanding the Void Pointers'):
        st_player('https://www.youtube.com/watch?v=ij2jrsUmwCI', height=400)
     
      with st.expander('Callback Functions'):
        st_player('https://youtu.be/Hm1OjzTa_MY', height=400)

      with st.expander('Application of Function Pointers'):
        st_player('https://youtu.be/wQ-gWwKKeP4', height=400)
 
      with st.expander('Understanding and implementing a Hash Table'):
        st_player('https://youtu.be/2Ti5yvumFTU', height=400)


    if option_media == 'PODCAST':
      st.info("Will try to work on it")
      
  # External libraries, B-trees & priority queues
  if option == 'External libraries, B-trees & priority queues' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/4b9152a12a01274abfaf5a3c2686564b_MIT6_087IAP10_lec09.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      with st.expander('Static and Dynamic linking'):
        st_player('https://youtu.be/eW5he5uFBNM', height=400)
     
      with st.expander('Binary search tree'):
        st_player('https://youtu.be/COZK7NATh4k', height=400)

      with st.expander('Stack vs Heap Memory'):
        st_player('https://youtu.be/gRwfHzeS-GM', height=400)
 
      with st.expander('Priority Queue Introduction'):
        st_player('https://www.youtube.com/watch?v=wptevk0bshY', height=400)

    if option_media == 'PODCAST':
      st.info("Will try to work on it")
    
  # C standard library
  if option == 'C standard library' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/2d7ce9e81c1ce03c8c93a12c9d21d0dd_MIT6_087IAP10_lec10.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      with st.expander('C Standard Library Functions'):
        st_player('https://youtu.be/OJvwk3pLK34', height=400)
     
      with st.expander('time.h'):
        st_player('https://youtu.be/Qoed2uBwF_o', height=400)

      with st.expander('stdarg.h'):
        st_player('https://youtu.be/3iX9a_l9W9Y', height=400)

    if option_media == 'PODCAST':
      st.info("Will try to work on it")
    
  # Dynamic memory allocation & garbage collection
  if option == 'Dynamic memory allocation & garbage collection' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/626730575787751a6468f681d95ecb9f_MIT6_087IAP10_lec11.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      with st.expander('Allocating memory with malloc, calloc, realloc, and free'):
        st_player('https://youtu.be/P6oqhAxV0dA', height=400)
   
      with st.expander("Cheney's GC algorithm"):
        st_player('https://youtu.be/S1xvtHsarbI', height=400)
     
      with st.expander('Mark-Sweep GC algorithm'):
        st_player('https://www.youtube.com/watch?v=lXj6j9hVGLQ', height=400)
  
    if option_media == 'PODCAST':
      st.info("Will try to work on it")
    
  # Multithreading & concurrency
  if option == 'Multithreading & concurrency' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/40d5984d819aaa72e55aa10376b73bde_MIT6_087IAP10_lec12.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      with st.expander('Difference Between Process and Thread'):
        st_player('https://youtu.be/O3EyzlZxx3g', height=400)
     
      with st.expander('Multi-Threading Programming in C'):
        st_player('https://youtu.be/QbFM0YroaF0', height=400)

    if option_media == 'PODCAST':
      st.info("Will try to work on it")
    
  # Multithreaded programming. Sockets and asynchronous I/O
  if option == 'Multithreaded programming. Sockets and asynchronous I/O' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/9433ec97b59ad1ceb135708210141796_MIT6_087IAP10_lec13.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':
      with st.expander('What is a Race Condition (Computer Programming)?'):
        st_player('https://youtu.be/KF8dF1QS8Go', height=400)
     
      with st.expander('What is Semaphores'):
        st_player('https://youtu.be/XDIOC2EY5JE', height=400)

      with st.expander('Everything you should know about thread safety'):
        st_player('https://youtu.be/6Y0NF85cUvk', height=400)
     
      with st.expander('Everything you should know about deadlock'):
        st_player('https://www.youtube.com/watch?v=oEbXlSH8hyE', height=400)

      with st.expander('Socket Programming'):
        st_player('https://youtu.be/LtXEMwSG5-8', height=400)

      with st.expander('Asynchronous I/O with AIO'):
        st_player('https://youtu.be/TdWkejSSfro', height=400)


    if option_media == 'PODCAST':
      st.info("Will try to work on it")
    
  # Linux inter process communication
  if option == 'Linux inter process communication' :
    
    option_media = option_media()

    if option_media == 'TEXT' :
      st.markdown("""<embed src="https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/d819f17f7632a8622af911360f42796f_MIT6_087IAP10_lec14.pdf" width="1000" height="800">""", unsafe_allow_html=True)
      Credit()

    if option_media == 'VIDEO':

      with st.expander('<signals.h>'):
        st_player('https://youtu.be/rggw61JtGz0', height=400)
   
      with st.expander("Practical use case for fork and pipe in C"):
        st_player('https://youtu.be/6u_iPGVkfZ4', height=400)
     
      with st.expander('Introduction to FIFOs (aka named pipes)'):
        st_player('https://youtu.be/2hba3etpoJg', height=400)

    if option_media == 'PODCAST':
      st.info("Will try to work on it")
    
