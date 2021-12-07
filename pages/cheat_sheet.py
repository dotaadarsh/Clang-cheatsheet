import streamlit as st
from streamlit_player import st_player

def app():
  st.sidebar.title("Contribute")
  st.sidebar.info(
            "This is an open source project and you are very welcome to contribute your "
            "comments, questions, resources and apps as "
            "[issues](https://github.com/giswqs/streamlit-geospatial/issues) or "
            "[pull requests](https://github.com/giswqs/streamlit-geospatial/pulls) "
            "to the [source code](https://github.com/giswqs/streamlit-geospatial). ")

  st.header("C CHEATSHEET", anchor=None)
  st.caption("REVISE ON THE GO")
  st_player("https://soundcloud.com/c-programming-podcast/introduction-to-c-programming-language-by-ddsry")
  with st.expander("KEYWORDS (32)", expanded = False):
    st.write("""
                - auto
                - break 
                - case
                - char
                - const
                - continue
                - default
                - do
                - double
                - else
                - enum
                - extern
                - float
                - for
                - goto
                - if
                - int
                - long
                - register
                - return
                - short
                - signed
                - sizeof
                - static
                - struct
                - switch
                - typedef
                - union
                - unsigned
                - void
                - volatile
                - while
                - double
                <br/><br/>
                """,
             unsafe_allow_html=True)
             
  with st.expander("OPERATORS (45)", expanded=False):
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

  with st.expander("IDENTIFIERS", expanded=False):
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
   
  with st.expander("ESCAPE SEQUENCES (15) - starting with backslash \ ",
                 expanded=False):
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

  with st.expander("CONSTANTS - const keyword (or) #define preprocessor",
                 expanded=False):
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

  with st.expander("FORMAT SPECIFIER", expanded=False):
    st.write("""
                - **%d or %i** -	It is used to print the signed integer value where signed integer means that the variable can hold both positive and negative values.
                - **%u**	It is used to print the unsigned integer value where the unsigned integer means that the variable can hold only positive value.
                - **%o**	It is used to print the octal unsigned integer where octal integer value always starts with a 0 value.
                - **%x**	It is used to print the hexadecimal unsigned integer where the hexadecimal integer value always starts with a 0x value. In this, alphabetical characters are printed in small letters such as a, b, c, etc.
                - **%X**	It is used to print the hexadecimal unsigned integer, but %X prints the alphabetical characters in uppercase such as A, B, C, etc.
                - **%f**	It is used for printing the decimal floating-point values. By default, it prints the 6 values after '.'.
                - **%e/%E**	It is used for scientific notation. It is also known as Mantissa or Exponent.
                - **%g**	It is used to print the decimal floating-point values, and it uses the fixed precision, i.e., the value after the decimal in input would be exactly the same as the value in the output.
                - **%p**	It is used to print the address in a hexadecimal form.
                - **%c**	It is used to print the unsigned character.
                - **%s**	It is used to print the strings.
                - **%ld**	It is used to print the long-signed integer value.
                <br/><br/>
                """,
             unsafe_allow_html=True)

  with st.expander("PRE-PROCESSER DIRECTIVES - starts with hash # ",
                 expanded=False):
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
             
  st.code('for i in range(8): foo()')
  code = '''#include <stdio.h>
  int main() {
   /* my first program in C */
   printf("Hello, World! \n");
   
   return 0;
   }'''

  st.code(code, language='c')

  left_column, right_column = st.columns(2)
 # You can use a column just like st.sidebar:
  left_column.code('for i in range(8): foo()')

 # Or even better, call Streamlit functions inside a "with" block:
  with right_column:
    chosen = st.radio('Sorting hat',
                      ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
  import time
  my_bar = st.progress(0)
  for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)