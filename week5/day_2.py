#day 2 is about combining functions with decisions !

#week 2 , we used if , decisions !

#lets wrap this logic into functions !

#question 1

def even_or_odd(numbers):
    count = 0

    for i in numbers:
        if i % 2 == 0:
            count += 1

    return count


even = even_or_odd([1, 2, 3, 4, 5])
print(even)


#naming matters !


#question 1 (slightly harder)

def even_or_odd(numbers):
    count = 0
    if numbers % 2 == 0:
        return "even"

    else:
        return "odd"



#question 2


def number_sign(number):

    if number >= 1:
        return "positive"
    elif number == 0:
        return "zero"
    else:
        return "negative"


print(number_sign(-1))


#grade machine
#question 3


def grade(score):

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    else:
        return "F"

print(grade(85))

#grade b
#the problem is that u use mmultiple if statements!


if
elif
elif
elif
else


#below is the solution

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"



#why is elif better!?

#if the previous version failed , try this one !





#question 4

#password validator

def password_valid(password):

    for i in password:
        if len(password) >= 8:
            return "true"
        else:
            return "false"


print(password_valid("andrewqqqq"))


#this is a good attempt !
#the problem is that these are strings not booleans for true , false , so u dont need quotes


#below is correct version

def password_valid(password):

    if len(password) >= 8:
        return True
    else:
        return False


print(password_valid("andrewqqqq"))



#question 5
#tax calculator


def tax(income):
    if income < 2000:
        return "10%"
    elif income < 5000:
        return "20%"
    else:
        return "30%"



print(tax(2000))

6.5/10


#solution below !
def tax(income):

    if income < 20000:
        return income * 0.10
    elif income < 50000:
        return income * 0.20
    else:
        return income * 0.30


print(tax(30000))

