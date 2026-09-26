def greet(name):
    return "Hello " + name

result = greet("Andrew")
print(result)


def add_numbers(a, b):
    return a + b


result_1 = add_numbers(10, 5)
print(result_1)


def is_adult_age(age):
    if age >= 18:
        return True

    else:
        return False


age = is_adult_age(200)
print(age)



def check_number(number):
    if number > 0:
        return "Positive"

    elif number < 0:
        return "Negative"


    else:
        return "zero"




check = check_number(-2)
print(check)




def even_or_odd(number):
    if number %2 == 0:
        return "Even"

    else:
        return "Odd"

result = even_or_odd(7)
print(result)


def count_to_n(n):
    count = 0
    for i in range(5):
        count += 1 
        print(count)
    

result = count_to_n(5)
print(result)



def find_largest_number(largest):
    largest_num = float("-inf")


    for num in largest:
        if num > largest_num:
            largest_num = num 

        return largest_num 



    




