#what is this ?

#this is an argument,that gives a paramter a value automaticallty when the caller does not provide one 

#for example 

def greet(name, greeting="Hello"):
    print(greeting, name)


greet("andy")

#Hello andy


#importent rule , parmaters without defaults must come first ! 


def greet(name, greeting="Hello"):
    pass


#above: valid 



#def greet(greeting="Hello", name):
#   pass


#above: invalid 



#practice question


#question 1

def create_player(name, classes, level=1):
    print(name, classes, level)




create_player("andy", "mage")


#andy mage 1
