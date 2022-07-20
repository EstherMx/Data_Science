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



# WHILE LOOP / CONTINUE (Infinite loop)

# Breaking out of a while loop (infinite loop)
# Esther's code
while True: 
    line = input('>') # ('>') means it takes any input by the user
    if line != 'done':
        print(line)
    else: 
        print('DONE!')
        break  #<==== end of the while loop
print('Outside of the loop')

# The code
while True:
    line = input('>')
    if line == 'done':
        print('DONE!')
        break # <=== end of the while loop when break is activated
    print(line)  # <=== part of the while loop while true
print('Outside of the loop') # <=== outside of the while loop. called when the loop is over

#In Python, a loop ends a line before indented, compared to javaScript where everything is aligned



#CONTINUE returns to the beginning of the loop and ignores all the remaining statements in the current iteration of the loop.
# The continue statement can be used in both while and for loops.
# ie:
for letter in 'Python':    
   if letter == 'h':
      continue
   print 'Current Letter :', letter

# This for loop will go through each letter of 'Python', if the current letter is 'h' then the loop will ignore the rest
# of the code and go back up to the beginning of the for loop and move on to the next letter.
# All the letters in 'Python' except 'h' will be printed at the end of the loop. 
# Whereas 'break' will stop the whle process of the loop


#FOR LOOP
for i in [5, 6, 3, 4]:
    print(i)
print('Done!')

# 'i' is a variable that represents each index of the array
# once we're done looping and print each index, we exit the 
# for loop then print 'Done!'


# Difference between == and 'IS' operator in Python
#  _source: https://www.geeksforgeeks.org/difference-operator-python/
# In short, 'IS' checks identity or location of an object, which can be checked with id() function 
# in python which returns the “identity” of an object.

# Python's is keyword compares references (and so is about identity)
# while === does a minimal amount of coercion (and is therefore concerned with equality, 
# at least in the case of primitives) so they are different.

#Does Python use '==='? (answer from StackOverflow)
# Mathematica has an === operator which is a shortcut for the SameQ predicate. But it doesn't make sense in python. – 
# President James K. Polk
#  Jul 17, 2011 at 18:06
# 4
# If you need a ===, you're not writing Python. Python uses duck typing and interfaces rather than types – 
# Humphrey Bogart
#  Sep 16, 2011 at 22:13



list = array
LISTS (check the value of a list in the command line)

>> X = list()
>> type(x)
<type 'list'>
>> dir(x)   //return what is on the list
['append','count','extend','index','insert']


SLICE A LIST
>> t = [9, 41, 12, 55]
>> t[1: 3] //the new list starts at index 1 up to but not including index 3.
[9, 41, 12]
>> t[2:] //the new list starts at index 2 till the end
[12, 55]
>> t[:2] //the first two numbers, not including index 2
[9, 41]
>> t[:] //the whole list
[9, 41, 12, 55]


CONCATENATE LISTS
>> a = [1, 2, 3]
>> b = [4, 5, 6]
>> c = a + b
>> print(c)
[1, 2, 3, 4, 5, 6]


APPEND to add an item at the end of a LISTS
>> stuff = list()  //this list is empty
>> stuff append['book'] //adding the string book at the list stuff
>> stuff append[66]  
>> print(stuff)
['book', 66]


# SPLIT() break a string into indivitual word to save it in an array

>>string = 'with three words'
>>makeList = string.split() #breaks into indexes based on spaces
>>print(makeList)
['with','three','words']
>>print(makeList[0])
with

# If there's no spaces in the string:
>>line = 'first;second;third'
>> thing = line.split(;)  #break words into indexes base on ';'
>> print(thing)
['first','second','third']


R: finish ex above
check if a work is in a list
rstip() to remove the space at the end of a document or line
 the ie with the email address
