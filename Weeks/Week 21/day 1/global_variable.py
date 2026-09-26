#what is a global variable?

#this is a variable that is defined outside of any function and can be accessed from anywhere in the code


#for example 


name = "Alice"  # This is a global variable



def greet():  
    print(f"Hello, {name}!")  # Accessing the global variable


greet()  # Calling the function to see the output


#how does python find name ?


#name refers to the string object "Alice". Python looks up the name in its scopes and retrieves the object it refers to.

#remember 


#name ──────> "Alice"



# name ────────┐
#             ├────> string object "Alice"
#other_name ──┘


#global names can refer to any object in memory , including other names , functions , classes , etc.

#name = "Alice"       # refers to a string
#age = 25             # refers to an integer
#items = ["Alice"]    # refers to a list
#greet = some_function  # can even refer to a function


#the same spelling can exist in different scopes , but they refer to different objects in memory

#for example 

name = "Alice"  # global

def greet():
    name = "Bob"  # local
    print(name)

greet()
print(name)


#Global namespace:  "name" ──> "Alice"
#Local namespace:   "name" ──> "Bob"

#python uses 

#Local → Enclosing → Global → Built-in



#Python uses LEGB to decide which entry applies:

