import streamlit as st
from streamlit_player import st_player

def app():
  st.sidebar.title("BOOKS")
  st.sidebar.info(
            "[C](https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-langs.md#c)"
            "\n [C++](https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-langs.md#c-1)")

  st.sidebar.info(
            "[Free programming books](https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-langs.md)")

  st.header("C CHEATSHEET", anchor=None)
  st.caption("REVISE ON THE GO")
  st_player("https://youtu.be/U3aXWizDbQ4")
  col1, col2, col3 = st.columns([1,1,1])
  with col1:
    with st.expander("KEYWORDS (32)", expanded = True):
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
