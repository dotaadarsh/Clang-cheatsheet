import streamlit as st
from streamlit_player import st_player
import streamlit.components.v1 as components
import pandas as pd

def app():

  st.sidebar.title("Resources")
  with st.sidebar:
     st.download_button(label="The C Prog language by K & R", data="https://kremlin.cc/k&r.pdf", file_name="The C Prog language by K & R")
     st.download_button(label="Beej’s Guide to C Programming", data="https://beej.us/guide/bgc/pdf/bgc_a4_bw_2.pdf", file_name=None)
     st.download_button(label="The Basics of C Programming", data="https://www.phys.uconn.edu/~rozman/Courses/P2200_13F/downloads/TheBasicsofCProgramming-draft-20131030.pdf", file_name=None)
     st.markdown('> Join my discord community.')
     components.html(
    """<iframe src="https://discord.com/widget?id=818551736809422848&theme=dark" width="280" height="380" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>""",
    height=400,)

  st.caption("Revise on the go")
  st_player("https://youtu.be/U3aXWizDbQ4")

  with st.expander("Roadmap", expanded=True): 
    st.image("asserts/TIMELINE.jpg")

  col1, col2, col3 = st.columns([1,1,1])
  with col1:
    with st.expander("Keywords", expanded = True):
      st.write("""
                - auto - extern
                - break - continue
                - char
                - const
                - do...while
                - double - float
                - enum
                - for
                - goto
                - if - else
                - int
                - register
                - return
                - short - long - signed - unsigned
                - sizeof
                - static
                - struct
                - switch - case - default
                - typedef
                - union
                - void
                - volatile
                <br/><br/>
                """,
             unsafe_allow_html=True)

    with st.expander("Constants - const keyword (or) #define preprocessor",
                 expanded=True):
                 st.write("""
                - Decimal Constant - 10, 20, 450 etc.
                - Real or Floating-point Constant	10.3, 20.2, 450.6 etc.
                - Octal Constant	021, 033, 046 etc.
                - Hexadecimal Constant	0x2a, 0x7b, 0xaa etc.
                - Character Constant	'a', 'b', 'x' etc.
                - String Constant	"c", "c program", "ZERONITE" etc.
                <br/><br/>
                """,
             unsafe_allow_html=True)

    with st.expander("Escape sequences - starting with backslash \ ",
                 expanded=True):
                 st.write("""
                - a - Alarm or Beep
                - b - Backspace
                - f - Form Feed
                - n - New Line
                - r - Carriage Return
                - t - Tab (Horizontal)
                - v - Vertical Tab
                - \ - Backslash
                - ' - Single Quote
                - " - Double Quote
                - ? - Question Mark
                <br/><br/>
                """,
             unsafe_allow_html=True)

    with st.expander("Comments",
                 expanded=True):
                 st.write("""Comments are used to indicate something to the person reading the code. There are two syntaxes used for commentsin C, the original /* */ and the slightly newer //
                <br/><br/>
                """,
             unsafe_allow_html=True)


  with col2:
    with st.expander("Operators", expanded=True):
      st.text("Arithmetic Operators")
      st.write("""
               - Addition or unary plus (+)
               - Subtraction or unary minus (-)
               - Multiplication (*)
               - Division (/)
               - Modulo Division-Gives remainder (%)
                <br/><br/>
                """,
             unsafe_allow_html=True)

      st.text("Relational Operators")
      st.write("""
                - Equals "=="
                - Not equals "!="
                - Not "!"
                - Greater than ">"
                - Less than "<"
                - Greater than or equal ">="
                - Less than or equal "<="
                <br/><br/>
                """,
             unsafe_allow_html=True)
      st.text("Conditional/Ternary Operator")
      st.write("""
                - a = b ? c : d;
                <br/><br/>
                """,
             unsafe_allow_html=True)
      st.caption("exp1 ? exp2 : exp3 ? exp4 : exp5")
     
      st.text("Logical Operators")
      st.write("""
               - && - logical AND
               - || - logical OR
               - !  -	logical NOT
                <br/><br/>
                """,
             unsafe_allow_html=True)

      st.text("Increment and Decrement Operators")
      st.write("""
               - ++ - Increment
               - -- - Decrement
                <br/><br/>
                """,
             unsafe_allow_html=True)
      st.text("Bitwise Operator")
      st.write("""
      - & - bitwise AND
      - | - bitwise inclusive OR
      - ^ - bitwise exclusive OR (XOR)
      - ~ - bitwise not (one's complement)
      - << - logical left shift
      - << - logical right shift
      <br/><br/>
                """,
             unsafe_allow_html=True)

    with st.expander("Pre-Processer Directives - starts with hash # ",
                 expanded=True):
                 st.caption("Syntax: ")
                 st.code('#define token value')
                 st.write("""
                - #include
                - #define
                - #undef
                - #ifdef
                - #ifndef
                - #if
                - #else
                - #elif
                - #endif
                - #error
                - #pragma
                <br/><br/>
                """,
             unsafe_allow_html=True)

  with col3:
    with st.expander("Identifiers", expanded=True):
      st.write("""
                - An identifier can only have alphanumeric characters (a-z , A-Z , 0-9) (i.e. letters & digits) and underscore( _ ) symbol.
                - Identifier names must be unique
                - The first character must be an alphabet or underscore.
                - You cannot use a keyword as identifiers.
                - Only the first thirty-one (31) characters are significant.
                - It must not contain white spaces.
                - Identifiers are case-sensitive.
                <br/><br/>
                """,
             unsafe_allow_html=True)

    with st.expander("Format specifier", expanded=True):
      st.write("""
                - **%d or %i** -	signed integer value 
                - **%u** - unsigned integer value 
                - **%o** - octal unsigned integer
                - **%x**/**%X** - hexadecimal unsigned integer 
                - **%f** - decimal floating-point values
                - **%e**/**%E** - scientific notation
                - **%g** - decimal floating-point values, and it uses the fixed precision
                - **%p** - address in a hexadecimal form
                - **%c** - unsigned character
                - **%s** - strings
                - **%ld** -	long-signed integer value
                <br/><br/>
                """,
             unsafe_allow_html=True)

    with st.expander("Integer types and Constants", expanded = True):
      df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSJ5B9E5p6MbKot2HBwAwkGGr_YxVJWgUdTgUVvamEtI6Vo2IdsqcjUq-MCdVoJD7dYpawtaHxgfSNO/pub?output=csv") 
      st.dataframe(df)

  
    with st.expander("Library functions", expanded = True):
      st.write("""
                - <assert.h> - Program assertion functions
                - <ctype.h>	- Character type functions
                - <locale.h>	- Localization functions
                - <math.h>	- Mathematics functions
                - <setjmp.h>	- Jump functions
                - <signal.h>	- Signal handling functions
                - <stdarg.h>	- Variable arguments handling functions
                - <stdio.h>	- Standard Input/Output functions
                - <stdlib.h> - Standard Utility functions
                - <string.h> - String handling functions
                - <time.h> - Date time functions
                <br/><br/>
                """,
             unsafe_allow_html=True)
      
  st.subheader("Order of Precedence")
  df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSJ5B9E5p6MbKot2HBwAwkGGr_YxVJWgUdTgUVvamEtI6Vo2IdsqcjUq-MCdVoJD7dYpawtaHxgfSNO/pub?gid=600762557&single=true&output=csv") 
  st.dataframe(df)

  st.subheader("Functions")
  st.caption("Functions are used to divide the code and to avoid repetitive task. It provides reusability and readability to code.")
  st.code('''return_type function_name(data_type-parameters){
    //code
}
//  Example of function to add two numbers

int add(int a, int b){
    return a+b;
}''')

  col1, col2, col3 = st.columns([1,1,1])
  with col1:
    with st.expander("Pointers", expanded = True):
      st.write("""Pointer is a variable that contains the address of another variable.
                """,
             unsafe_allow_html=True)
      st.code('''datatype *var_name;
''')
    with st.expander("Strings", expanded = True):
      st.write("""It is basically 1D character array. It character of string is null character (\0)
                """,
             unsafe_allow_html=True)
      st.code('''char string_name[size];
''')
   
  with col2:
    with st.expander("Recursion", expanded = True):
      st.write("""Recursion is the process of repeating items in a self-similar way.If a program allows you to call a function inside the same function, then it is called a recursive call of the function.
                """,
             unsafe_allow_html=True)
      st.code('''void myFunction(){
    myFunction();   
    //Function calling itself
}
''')

  with col3:
    with st.expander("Arrays", expanded = True):
      st.write("""Array is an collection of data of same data-type.
                """,
             unsafe_allow_html=True)
      st.code('''//Declaration
data_type array_name[array_size];
''')
      st.code('''//Fetching Array Element
//Array index starts from 0.
data_type variable_name = arr[index]''')

  st.subheader("Structures")
  st.caption("A structure creates a data type that can be used to group items of possibly different types into a single type.")
  st.code('''//Declaration 
  struct student
{
    char name[50];
    int class;
    float percentage;
    char college[50];
};      //Notice the semicolon  ''')

  st.subheader("Dynamic Memory Allocation")
  st.markdown('>  **malloc() function** - Stands for Memory allocation and reserves a block of memory with the given amount of bytes.')
  st.markdown('>  **calloc() function** - Stands for “contiguous allocation” method in C is used to dynamically allocate the specified number of blocks of memory of the specified type.')
  st.markdown('>  **realloc() function** - If the allocated memory is insufficient, then we can change the size of previously allocated memory using this function for efficiency purposes.')
  st.markdown('>  **free() function** - “free” method in C is used to dynamically de-allocate the memory. ')

  st.subheader("File handling")
  st.write("Creating file pointer")
  st.code('''FILE *file''')
  st.write("Opening a file")
  st.code('''file = fopen(file_name.txt,w)''')
  st.write("fscanf() function")
  st.caption("Used to read file content")
  st.code('''fscanf(FILE *stream, const char *format, ..);''')
  st.write("fprintf() function")
  st.caption("Used to write the file content")
  st.code('''fprintf(FILE *var, const char *str,..);''')
  st.write("Closing a File")
  st.code('''fclose(file);''')


  col1, col2 = st.columns([1.5,1])
  with col1:
    st.subheader("Summary")
    st.write("- ‘C’ was developed by Dennis Ritchie in 1972.\n- It is a robust language.\n- It is a low programming level language close to machine language \n- It is widely used in the software development field. \n- It is a procedure and structure oriented language. \n- It has the full support of various operating systems and hardware platforms. \n- Many compilers are available for executing programs written in ‘C’. \n- A compiler compiles the source file and generates an object file.\n- A linker links all the object files together and creates one executable file.")
  with col2: 
    st.image("https://c.tenor.com/_DOBjnGspYAAAAAM/code-coding.gif", width=350)
  st.markdown('***')
  st.markdown(
        "Thanks for visiting. I'd love feedback on this, so if you want to reach out you can find me on [Twitter] (https://twitter.com/madmax_ak), [GitHub] (https://github.com/madmax-ak), [LinkedIn] (https://www.linkedin.com/in/aadarsh-k/) or in Discord - MADMAX#4441")

        