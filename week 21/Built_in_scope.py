#what is Built-in scope?

#Built in scope contains the names of all the built-in functions and exceptions in Python. 
#These names are always available for use, regardless of where you are in your code.


# Input and output
print()
input()
open()

# Type creation and conversion
int()
float()
str()
bool()
list()
tuple()
dict()
set()

# Calculations
sum()
min()
max()
abs()
round()
pow()

# Collections and iteration
len()
range()
enumerate()
zip()
sorted()
reversed()
iter()
next()

# Checking objects
type()
isinstance()
id()
callable()

# Logic
all()
any()

# Object-oriented programming
object
property()
super()
classmethod()
staticmethod()

# Help and inspection
help()
dir()
vars()

True
False
None


#Built-in exceptions!


NameError
TypeError
ValueError
IndexError
KeyError




#for example 

names = ["Alice", "Bob", "Charlie"]

print(len(names))



#Python searches for len using LEGB:


#Local     → not found
#Enclosing → not found
#Global    → not found
#Built-in  → found Python's len function


#output:
3


#Built-in scope contains names that Python makes available automatically.


