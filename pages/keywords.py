# Load important libraries 
import pandas as pd
import streamlit as st 
from streamlit_player import st_player
import os


def app():

  st.header('KEYWORDS')
  st.caption("Keywords are predefined, reserved words used in programming that have special meanings to the compiler. Keywords are part of the syntax and they cannot be used as an identifier.")

  st.info('Click on the keywords on the left to explore about it')

  col1, col2, col3 = st.columns([0.5,0.5,2])
  
  with col1: 
    a = st.button('auto')

    b = st.button('break & continue')
    if (b == True):
      st.caption("Syntax for break: ")
      st.code('//loop or switch case \n  break;')
      st.caption("Syntax for continue: ")
      st.code('continue;')

    c = st.button('switch...case')
    if (c == True):
      st.caption("Syntax: ")
      st.code('switch (expression)\n​{\ncase constant1: // statements \nbreak;\ncase constant2: // statements \nbreak;\n.\n.\n. \ndefault:\n// default statements \n}')

    d = st.button('char')
    if (d == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')
   
    e = st.button('const')
    if (e == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')



    g = st.button('default')
    if (g == True):
      st.caption("Syntax: ")
      st.code('//loop or switch case \n  break;')

    h = st.button('do')
    if (h == True):
      st.caption("Syntax: ")
      st.code('switch (n){ case 1: // code to be executed if n = 1;break; case 2: // code to be executed if n = 2; break; default: // code to be executed if n doesnt match any cases }')

    i = st.button('double')
    if (i == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')
    j = st.button('else')
    if (j == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')

    k = st.button('enum')
    if (k == True):
      st.caption("Syntax: ")
      st.code('auto <data_type> <variable_name>;')

    l = st.button('extern')
    if (l == True):
      st.caption("Syntax: ")
      st.code('//loop or switch case \n  break;')

    m = st.button('float')
    if (m == True):
      st.caption("Syntax: ")
      st.code('switch (n){ case 1: // code to be executed if n = 1;break; case 2: // code to be executed if n = 2; break; default: // code to be executed if n doesnt match any cases }')

    n = st.button('for')
    if (n == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')
   
    o = st.button('goto')
    if (o == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')


    p = st.button('if')
    if (p == True):
      st.caption("Syntax: ")
      st.code('auto <data_type> <variable_name>;')
 
  with col2: 
    q = st.button('int')
    if (q == True):
      st.caption("Syntax: ")
      st.code('//loop or switch case \n  break;')

    r = st.button('long')
    if (r == True):
      st.caption("Syntax: ")
      st.code('switch (n){ case 1: // code to be executed if n = 1;break; case 2: // code to be executed if n = 2; break; default: // code to be executed if n doesnt match any cases }')

    s = st.button('register')
    if (s == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')
    t = st.button('return')
    if (t == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')

    u = st.button('short')
    if (u == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')

    v = st.button('signed')
    if (v == True):
      st.caption("Syntax: ")
      st.code('auto <data_type> <variable_name>;')

    w = st.button('sizeof')
    if (w == True):
      st.caption("Syntax: ")
      st.code('//loop or switch case \n  break;')

    x = st.button('static')
    if (x == True):
      st.caption("Syntax: ")
      st.code('switch (n){ case 1: // code to be executed if n = 1;break; case 2: // code to be executed if n = 2; break; default: // code to be executed if n doesnt match any cases }')

    y = st.button('struct')
    if (y == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')
   
    z = st.button('switc')
    if (z == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')


    aa = st.button('typedef')
    if (aa == True):
      st.caption("Syntax: ")
      st.code('auto <data_type> <variable_name>;')

    bb = st.button('union')
    if (bb == True):
      st.caption("Syntax: ")
      st.code('//loop or switch case \n  break;')

    cc = st.button('unsigned')
    if (cc == True):
      st.caption("Syntax: ")
      st.code('switch (n){ case 1: // code to be executed if n = 1;break; case 2: // code to be executed if n = 2; break; default: // code to be executed if n doesnt match any cases }')

    dd = st.button('void')
    if (dd == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')
    ee = st.button('volatile')
    if (ee == True):
      st.caption("Syntax: ")
      st.code('int variable_name1 [= value1];')

  with col3: 
    if (a == True):
      st.write("Auto is a storage class/ keyword in C Programming language which is **used to declare a local variable**. A local variable is a variable which is accessed only within a function, memory is allocated to the variable automatically on entering the function and is freed on leaving the function. \n GNU C has extended auto to allow forward declaration of nested functions as well.")
      st.caption("Syntax: ")
      st.code('auto <data_type> <variable_name>;')
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
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
      st.code(code, language='c')

    elif(b==True):
      st.write("BREAK AND CONTINUE")
      st_player("https://youtu.be/obJcPlAtGVM")
      code = '''// Program to calculate the sum of numbers (10 numbers max)
      // If the user enters a negative number, the loop terminates
      #include <stdio.h>
      int main() {
        int i;
        double number, sum = 0.0;
        for (i = 1; i <= 10; ++i) {
          printf("Enter n%d: ", i);
          scanf("%lf", &number);
          // if the user enters a negative number, break the loop
          if (number < 0.0) 
          {
            break;
            }
          sum += number; // sum = sum + number;
          }
          printf("Sum = %.2lf", sum);
          return 0;
          }'''
      st.code(code, language='c')
      st.write('how break work?')
      st.image("https://cdn.programiz.com/sites/tutorial2program/files/c-break-statement-works.jpg")
      st.write('how continue work?')
      st.image("https://cdn.programiz.com/sites/tutorial2program/files/c-continue-statement-works.jpg")
    
    elif(c==True):
      st.write("SWITCH...CASE...deafult")
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
      st.write('how break work?')
      st.image("https://cdn.programiz.com/sites/tutorial2program/files/flowchart-switch-statement.jpg")

    elif(d==True):
      st.write("thi  is const")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
      
    elif(e ==True):
      st.write("thi  iscaseh")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")

    elif(g==True):
      st.write("thi  is brak")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
    
    elif(h==True):
      st.write("thi  ischar")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
    
    elif(i==True):
      st.write("thi  is const")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
      
    elif(j ==True):
      st.write("thi  iscaseh")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
    
    elif(k==True):
      st.write("thi  is brak")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
    
    elif(l==True):
      st.write("thi  ischar")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
    
    elif(m==True):
      st.write("thi  is const")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
      
    elif(n ==True):
      st.write("thi  iscaseh")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
    
    elif(o==True):
      st.write("thi  idefaucltsh")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")

    elif(p==True):
      st.write("thi  is brak")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
    
    elif(q==True):
      st.write("thi  ischar")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
    
    elif(r==True):
      st.write("thi  is const")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
      
    elif(s ==True):
      st.write("thi  iscaseh")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")
        
    elif(t==True):
      st.write("thi  is brak")
      st_player("https://www.youtube.com/watch?v=2vOPEuiGXVo&t=714s")

    else: 
      st.write('A keyword is a reserved word. You cannot use it as a variable name, constant name, etc. There are only 32 reserved words (keywords) in the C language.')

      st.info("Keywords are the words whose meaning has already been explained to the C compiler and their meanings cannot be changed. Hence keywords are also called ‘Reserved words’. \n- Keywords can be used only for their intended purpose.\n- Keywords serve as basic building blocks for program statements.\n- Keywords can’t be used as programmer defined identifier.\n- The keywords can’t be used as names for variables.\n- All keywords must be written in lowercase.\n- 32 keywords available in C.")
    