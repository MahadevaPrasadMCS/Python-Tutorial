print("Hello, World!") #Hello, World!

import sys 
print(sys.version) #Gives the version of Python being used in this environment.

# Variables and Data Types in Python

x = 5 #Python variables doesn't need datatype to be mentioned.

x = "Hello"
print(x) #Hello , Because python assigns second value to x, as it is interprted line by line.

#We can change data type of a variable anytime 

x = int(3) #now the datatype of x is integer
x = float(3) #now the datatype of x is float.
print(x)    #3.0

#If we want to check the datatype of a variable we can use,

x = 5
print(type(x)) #<class 'int'>
y = "Hello"
print(type(y)) #<class 'str'>

#Note 
#In python string can be defined using single quotes or double quotes.
#Variable names are case-sensitive.

y = "Hello"
x = 'world'
print(y + " " + x) #Hello world

a = 10
A = 5
print(a==A) #false