#lets do some more questions !


#question 1

def double(x):
    return x * 2

def square(x):
    return x * x


numbers = [1, 3, 5]

for i in numbers:
     print(square(double(i)))


#question 2

def add_four(x):
    return x + 4

def triple(x):
    return x * 3

def process(x):
    x = triple(add_four(x))
    if x > 20:
        return "large"
    else:
        return "small"

z = [2, 5, 7]

for j in z:
    print(process(j))

#practice 3

def minus_one(x):
    return x - 1

def square(x):
    return x * x


numbers = [2, 4, 6, 8]

for i in numbers:
    print(square(minus_one(i)))