#questions

#question 1

def square(x):
    return x * x

def square_then_add_three(x):
    return x + 3

def final_function(x):
    return square_then_add_three(square(x))

print(final_function(4))


#question 2

def double(x):
    return x

def minus_five(x):
    return x - 5

def double_then_minus_five(x):
    return minus_five(double(x))



x = double_then_minus_five(6)
print(x)


#question 3
def triple(x):
    return x * 3

def add_two(x):
    return x + 2

def final_function(x):
    return add_two(triple(x))
print(final_function(3))



#question 4
def square(x):
    return x * x

def is_big(x):
    if square(x) > 20:
        return "big"
    else:
        return "small"

x = is_big(4)
print(x)


