# Load libraries 
import streamlit as st 
from streamlit_player import st_player

def app():

  st.header('KEYWORDS')
  st.caption("Keywords are predefined, reserved words used in programming that have special meanings to the compiler. Keywords are part of the syntax and they cannot be used as an identifier.")

  st.info('Click on the keywords to explore about it')

  col1, col2, col3 = st.columns([0.5,0.5,2])
  
  with col1: 
    a = st.button('auto & extern')
    b = st.button('break & continue')
    c = st.button('switch - case - default')
    d = st.button('char')
    e = st.button('const')
    h = st.button('do - while')
    i = st.button('float - double - long')
    j = st.button('else')
    k = st.button('enum')
    n = st.button('for')
    o = st.button('goto')
    p = st.button('if')

  with col2: 
    q = st.button('int')
    r = st.button('long')
    s = st.button('register')
    t = st.button('return')
    u = st.button('short')
    v = st.button('signed')
    w = st.button('sizeof')
    x = st.button('static')
    y = st.button('struct')
    z = st.button('switc')
    aa = st.button('typedef')
    bb = st.button('union')
    cc = st.button('unsigned')
    dd = st.button('void')
    ee = st.button('volatile')

  with col3: 
    if (a == True):
      st.write("Auto is a storage class/ keyword in C Programming language which is **used to declare a local variable**. A local variable is a variable which is accessed only within a function, memory is allocated to the variable automatically on entering the function and is freed on leaving the function. \n GNU C has extended auto to allow forward declaration of nested functions as well.")
      st.caption("Syntax: ")
      st.code('auto <data_type> <variable_name>;')
      st_player("https://youtu.be/1Dkfmf4PmvQ")
      st.write("Key points regarding auto keyword:\n- auto is used to define local variables (also by default)\n - auto is used for forward declaration of nested functions \n -auto can result in non-contiguous memory allocation")
      code = '''#include<stdio.h>
      int main()
      {
        auto int number = 5;
        {
          auto int number = 25;
          printf("%d, number);
          }
          printf("%d", number);
          return 0;
          }'''

    elif(b==True):
      st.write("break - continue")
      st.caption("Syntax for break: ")
      st.code('//loop or switch case \n  break;')
      st.caption("Syntax for continue: ")
      st.code('continue;')

      st_player("https://youtu.be/obJcPlAtGVM")
      code = '''// C program to illustrate the
// break statement
#include <stdio.h>

// Driver Code
int main()
{

	int i = 0, j = 0;

	// Iterate a loop over the
	// range [0, 5]
	for (int i = 0; i < 5; i++) {

		printf("i = %d, j = ", i);

		// Iterate a loop over the
		// range [0, 5]
		for (int j = 0; j < 5; j++) {

			// Break Statement
			if (j == 2)
				break;

			printf("%d ", j);
		}

		printf("n");
	}

	return 0;
}
'''
      st.code(code, language='c')
      st.write('how break works?')
      st.image("https://cdn.programiz.com/sites/tutorial2program/files/c-break-statement-works.jpg")
      st.write('how continue work?')
      st.image("https://cdn.programiz.com/sites/tutorial2program/files/c-continue-statement-works.jpg")
    
    elif(c==True):
      st.write("switch...case...default")
      st.caption("Syntax: ")
      st.code('switch (expression)\n​{\ncase constant1: // statements \nbreak;\ncase constant2: // statements \nbreak;\n.\n.\n. \ndefault:\n// default statements \n}')

      st_player("https://youtu.be/-JMSaLRqsgo")
      code = '''// Program to create a simple calculator
#include <stdio.h>

int main() {
    char operator;
    double n1, n2;

    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &operator);
    printf("Enter two operands: ");
    scanf("%lf %lf",&n1, &n2);

    switch(operator)
    {
        case '+':
            printf("%.1lf + %.1lf = %.1lf",n1, n2, n1+n2);
            break;

        case '-':
            printf("%.1lf - %.1lf = %.1lf",n1, n2, n1-n2);
            break;

        case '*':
            printf("%.1lf * %.1lf = %.1lf",n1, n2, n1*n2);
            break;

        case '/':
            printf("%.1lf / %.1lf = %.1lf",n1, n2, n1/n2);
            break;

        // operator doesn't match any case constant +, -, *, /
        default:
            printf("Error! operator is not correct");
    }

    return 0;
}
'''
      st.code(code, language='c')
      st.write('How break work?')
      st.image("https://cdn.programiz.com/sites/tutorial2program/files/flowchart-switch-statement.jpg")

    elif(d==True):
      st.write("char")
      st_player("https://youtu.be/QncEuobXjvw")

    elif(e ==True):
      st.write("const")
      st_player("https://youtu.be/jdrUQc2zlyg")
    
    elif(h==True):
      st.write("do - while")
      st_player("https://youtu.be/TjkJQly2YCw")
    
    elif(i==True):
      st.write("thi  is const")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
      
    elif(j ==True):
      st.write("thi  iscaseh")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
    
    elif(k==True):
      st.write("thi  is brak")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
    
 
    else: 
      st.write('A keyword is a reserved word. You cannot use it as a variable name, constant name, etc. There are only 32 reserved words (keywords) in the C language.')

      st.info("Keywords are the words whose meaning has already been explained to the C compiler and their meanings cannot be changed. Hence keywords are also called ‘Reserved words’. \n- Keywords can be used only for their intended purpose.\n- Keywords serve as basic building blocks for program statements.\n- Keywords can’t be used as programmer defined identifier.\n- The keywords can’t be used as names for variables.\n- All keywords must be written in lowercase.\n- 32 keywords available in C.")
    