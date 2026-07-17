#questions for understanding


#question 1
def double(x):
    return x * 2

def double_plus_ten(x):
    return double(x) + 10

print(double_plus_ten(10))
print(double_plus_ten(5))




#question 2
def tax(price):
    return price * 0.10

def final_price(price):
    return price + tax(price)

print(final_price(100))

#question 3

def word_length(word):
    return len(word)

def is_long_word(word):
    if word_length(word) > 5:
        return True
    else:
        return False

#question 4

def double(x):
    return x * 2

def double_plus_three(x):
    return double(x) + 3

print(double_plus_three(3))


#question 5

def add_two(x):
    return x + 2


def double_after_add(x):
    return add_two(x) * 2

double_after_add(4)


#question 6

def square(x):
    return x * x

def square_plus_five(x):
    return square(x) + 5

print(square_plus_five(3))


#question 7

def word_length(word):
    return len(word)

def is_long(word):
    if word_length(word) > 6:
        return True

    else:
        return False

print(is_long("elephant"))



#question 8

def count_letters(word):
    return len(word)

def add_two_to_length(word):
    return count_letters(word) + 2

print(add_two_to_length("elephant"))
