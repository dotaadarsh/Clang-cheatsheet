import streamlit as st
from streamlit_player import st_player
import pandas as pd

def app():
  st.sidebar.title("RESOURCES")
  st.sidebar.info(
            "- [The Basics of C Programming - Marshall Brain](https://www.phys.uconn.edu/~rozman/Courses/P2200_13F/downloads/TheBasicsofCProgramming-draft-20131030.pdf)"
            "\n- [C Programming - Wikibooks](https://en.wikibooks.org/wiki/C_Programming)"
            "\n- [Beej’s Guide to C ProgrammingBrian “Beej Jorgensen” Hal](https://beej.us/guide/bgc/pdf/bgc_a4_bw_2.pdf)")

  st.header("C CHEATSHEET", anchor=None)
  st.caption("REVISE ON THE GO")
  st_player("https://youtu.be/U3aXWizDbQ4")
  col1, col2, col3 = st.columns([1,1,1])
  with col1:
    with st.expander("KEYWORDS (32)", expanded = True):
      st.write("""
                - auto
                - break - continue
                - char
                - const
                - do...while
                - double - float
                - enum
                - extern
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
                - double
                <br/><br/>
                """,
             unsafe_allow_html=True)
  
    with st.expander("LIBRARY FUNCTIONS (11)", expanded = True):
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
  with col2:
    with st.expander("ESCAPE SEQUENCES (15) - starting with backslash \ ",
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

    with st.expander("OPERATORS (45)", expanded=True):
      st.write("""
                - Arithmatic 
                - Relational
                - Logical
                - Bitwise
                - Assignment
                - Misc
                <br/><br/>
                """,
             unsafe_allow_html=True)

    with st.expander("PRE-PROCESSER DIRECTIVES - starts with hash # ",
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
    with st.expander("IDENTIFIERS", expanded=True):
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
    with st.expander("CONSTANTS - const keyword (or) #define preprocessor",
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

    with st.expander("FORMAT SPECIFIER", expanded=True):
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
    with st.expander("OPERATORS", expanded=True):
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

             
  st.code('for i in range(8): foo()')
  code = '''#include <stdio.h>
  int main() {
   /* my first program in C */
   printf("Hello, World! \n");
   
   return 0;
   }'''

  st.code(code, language='c')
  st.text("COMMENTS")
  st.caption("Comments are used to indicate something to the person reading the code. Comments are treated like a blank bythe compiler and do not change anything in the code's actual meaning. There are two syntaxes used for commentsin C, the original /* */ and the slightly newer //")
  
  df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSJ5B9E5p6MbKot2HBwAwkGGr_YxVJWgUdTgUVvamEtI6Vo2IdsqcjUq-MCdVoJD7dYpawtaHxgfSNO/pub?output=csv") 
  #Method 1
  st.dataframe(df)
