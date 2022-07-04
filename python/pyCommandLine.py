print("Welcome", input("What's your name?"));
# Comments on Python are introduced with a hastag
#  'print' is the Python 'console.log' and can be read in the command line by typing 'py' then the name of the file.
# 'input' is a function that prompt the user to answer a question and the answer is always a string. 
# The command line will print: "What's your name " with a space for the user to type. Then it will say "Welcome Bob"

x = 5;
print( 5 + (int(input("What's your favorite number?"))));
# the command line will first ask "What's your favorite number?", take the user's answer, convert it into an number integer,
#then add that written number to 5 and print the final result. ie: 12, if the user typed 7.
# To run the code on the command line, write "py pyCommandLIne"
# py pyCommandLine.py
# What's your name?Justin Cavell
# Welcome Justin Cavell
# What's your favorite number?21
# 26


if x == 5:
    if x <= 10:
        print('Yes')
else: print('dommage!')

# In Python, if and for statement ends with a colon (:)
if x > 3:
    print('greater than 3')
else:
    print('smaller than 3')
print('All done!')


# TRY and EXCEPT are used when we know the result might return an error.
# Meaning: 'try' this code and if there's a traceback then execute 'except' followed by (:)
astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
except:
    istr = -1
print ('Done', istr)
# Usually used when the user has to enter a number, if the input is not an integer, execute 'except' than return 'not a number'


# Breaking out of a While loop

while True: 
    Line = input('>')
    if line != 'done':
        print(line)
    else: 
        print('DONE!')
        break