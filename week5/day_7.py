#day 7

#questions

#question 1


def double(x):
    return x * 2

numbers = [2, 5, 8, 3]

for i in numbers:
    if double(i) > 10:
        print(double(i))



#question 2
numbers = [1,2,3,4]

def add_three(x):
    return x + 3
def square(x):
    return x * x


for i in numbers:
    print(square(add_three(i)))





#question 3

def minus_two(x):
    return x - 2

def check_value(x):
    result = minus_two(x)
    if result > 5:
        return "big"
    else:
        return "small"


numbers = [4, 7, 10]

for i in numbers:
    print(check_value(i))




#lets do some more questions of this !
#practice 1
def minus_two(x):
    return x - 2

def check_value(x):
    if minus_two(x) > 6:
        return "big"
    else:
        return "small"

numbers = [3, 7, 10]

for i in numbers:
    print(check_value(i))

#practice 2

def minus_four(x):
    return x - 4
def check(x):
    if minus_four(x) > 3:
        return "high"
    else:
        return "low"

numbers = [2, 5, 8]

for i in numbers:
    print(check(i))




#question 4

def double(x):
    return x * 2

def add_five(x):
    return x + 5

def square(x):
    return x * x


numbers = [2, 5, 8]

for i in numbers:
    print(square(add_five(double(i))))


#question 5
def double(x):
    return x * 2

def add_three(x):
    return x + 3


#process make a nested call
def process(x):
    result = add_three(double(x))
    if result > 10:
        return "large"
    else:
        return "small"


numbers = [2, 4, 6]
for i in numbers:
    print(process(i))



