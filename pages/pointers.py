# Load libraries 
import streamlit as st 
from streamlit_player import st_player

def app():

  st.header('POINTERS')

  st.sidebar.caption("select the topic to explore")
  topics = st.sidebar.radio("TOPICS",("Intro", "Working with pointers", "Pointer types, pointer arithmetic, void pointer", "pointers to pointers", "Pointers as function arguments - call by ref", "Pointer & Arrays", "arrays as function arguments", "Char array and pointers", "Pointer and 2D arrays","Pointers and multi-D array", "Stack vs heap", "Malloc-Calloc-Realloc-Free", "Pointers as function returns", "Fucntion Pointers", "Function Pointer & callbacks", "Memory leak"))

  if topics == 'Intro':
     st.write('Introduction to pointers')
     st.write('''A Pointer in C language is a variable which holds the address of another variable of same data type.
Pointers are used to access memory and manipulate the address.
Pointers are one of the most distinct and exciting features of C language. It provides power and flexibility to the language. Although pointers may appear a little confusing and complicated in the beginning, but trust me, once you understand the concept, you will be able to do so much more with C language.''')
     st_player("https://youtu.be/zuegQmMdy8M?t=0")

     st.header('Address in C')
     st.write("Whenever a variable is defined in C language, a memory location is assigned for it, in which it's value will be stored. We can easily check this memory address, using the & symbol. If var is the name of the variable, then &var will give it's address. Let's write a small program to see memory address of any variable that we define in our program.")

     st.code('#include<stdio.h>\nvoid main()\n{\nint var = 7;\nprintf("Value of the variable var is: %d\n", var);\nprintf("Memory address of the variable var is: %x\n", &var);\n}')

     st.info("Benefits of using pointers \n - Pointers are more efficient in handling Arrays and Structures.\n - Pointers allow references to function and thereby helps in passing of function as arguments to other functions.\n - It reduces length of the program and its execution time as well.\n - It allows C language to support Dynamic Memory management.")

  elif topics == 'Working with pointers':
     st.write("Working with pointers")
     st.write("Consider the following example to define a pointer which stores the address of an integer.")
     st.code('''int n = 10;\nint* p = &n; // Variable p of type pointer is pointing to the address of the variable n of t''')
     st.write("Declaring a pointer")
     st.markdown("The pointer in c language can be declared using * (**asterisk symbol**). It is also known as indirection pointer used to dereference a pointer")
     st.code('''int *a;//pointer to int\nchar *c;//pointer to char  ''')
     st_player("https://youtu.be/zuegQmMdy8M?t=629")
     st.write("Example")
     st.code('''#include<stdio.h> \n int main(){  
int number=50;    
int *p;      
p=&number;//stores the address of number variable    
printf("Address of p variable is %x \n",p); // p contains the address of the number therefore printing p gives the address of number.     
printf("Value of p variable is %d \n",*p); // As we know that * is used to dereference a pointer therefore if we print *p, we will get the value stored at the address contained by p.    
return 0;  
}    ''')
     st.success("Output\n Address of number variable is fff4\nAddress of p variable is fff4\nValue of p variable is 50")

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
