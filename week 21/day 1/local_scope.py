#what is local scope ?

#this is the area inside the function where the variables exist 

#for example 1


def greet():
    message = "Hello, World!"  # This variable is in local scope
    print(message)  # Accessing the local variable


greet()  # Calling the function to see the output

#output: Hello, World!




def greet(name): #name is local 
    message = f"Hello, {name}!"  # message is also in local 
    print(message)  # Accessing the local variable


greet("Alice")  # Calling the function with an argument



#confusion ! 
#isnt name a parameter?

#yes , it is a parameter , but it is a parameter that acts as a local variable within the function

#what is a variable ?

#this is a name that refers to a value stored in memory 

#a parameter is a special variable that recieves a value when the function is called !



#when it is called , i.e, the function 


def greet(name): #name is local 
    message = f"Hello, {name}!"  # message is also in local 
    print(message)  # Accessing the local variable


greet("Alice")  # Calling the function with an argument



name = "Alice"

#the local name dissapears after the function is called , but the global name still exists


#what makes a variable local ?


def inner():
    name = "I am local"  # This variable is in local scope
    print(name)  # Accessing the local variable


inner()  # Calling the function to see the output


#when inner() is called , python creates a private local namespace for that call !

inner() local scope
└── name → "Local"




#Parameters also become local when the function is called:

def greet(name):
    print(name)

greet("Alice")





name = "Global"

def example():
    name = "Local"  # local because this function assigns it




def greet(name):
    print(name)

greet("Alice")  # one local scope: name → "Alice"
greet("Bob")    # a new local scope: name → "Bob"


