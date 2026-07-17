#combining functions with lists and loops !
#we are learning nested call ! or nested function call !



#question 1

def square(x):
    return x * x

def add_ten(x):
    return x + 10

def square_then_add(x):
    return  add_ten(square(x))

print(square_then_add(3))


#python executes inside ---> out !


add_ten(square(x))


#so first

square(3)

#output
#9

add_ten(9)
#19

#inner function first
#outer function second !


#question 2

def add_two(x):
    return x + 2

def triple(x):
    return x * 3

def add_then_triple(x):
    return add_two(triple(x))

print(add_then_triple(4))

#this is wrong !


#confusion , based upon the order , how do i know which one is first and decond !

#step 1

#ifnore the name of the fucntion !


#tep 2
#remmeber innner(x) ---> first
#remember outer() -----> runs second !
#outer(inner(x))

#you determine inner vs outer from the wording of the requirement ! not the function anme !

#question 3

def double(x):
    return x * 2

def add_five(x):
    return double(x) + 5


def new_function(x):
    return add_five(double(x))

print(new_function(3))




#question 4

def minus_one(x):
    return x - 1

def square(x):
    return square(minus_one(x))

print(square(5))

#good way to read this well is the 2nd is outer
#the first is inner !



#again

#first function is inner !
#second function is outer
#third function is outer
#and so on !

function_b(function_a(x))


#question 5

def double(x):
    return x * 2

def add_three(x):
    return x + 3

def square(x):
    return x * x

def final_function(x):
    return square(add_three(double(x)))


print(final_function(2))


#correct !


#question 6

def minus_two(x):
    return x - 2

def triple(x):
    return x * 3

def add_1(x):
    return x + 1

def final_function(x):
    return  add_1(triple(minus_two(x)))


print(final_function(5))


#solution is correct !




##function that decides something !

def function(x):
    return x * 2


def final_function(x):
    if function(x) > 10:
        return "big"
    else:
        return "small"



print(final_function(5))


#developers usually name something base upon what they do , sometimes your functions are too genergic !