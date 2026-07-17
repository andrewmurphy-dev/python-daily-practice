
#week 6 day 1
#today we will focus on lists !


#basic list loop
#create a list called numbers
#problem 1

numbers = []

numbers.append(3)
numbers.append(7)
numbers.append(10)
numbers.append(4)

print(numbers)

#problem 2

def double(x):
    return x * 2


numbers = [2, 5, 8, 3]

for i in numbers:
    result = double(i)
    print(result)


#problem 3

def double(x):
    return x * 2


numbers = [2,4,6,8]
results = []

for i in numbers:
    results.append(double(i))
    print(results)


#question 4
numbers = [1,5,8,2,9]
greater_than_five = []
for i in numbers:
    if i > 5:
        greater_than_five.append(i)
    print(greater_than_five)


#question 5

def double(x):
    return x * 2

def add_three(x):
    return x + 3

numbers = [2,4,6]

for i in numbers:
    result = add_three(double(i))
    print(result)


#question 6
#filter + score

numbers = [3, 10, 5, 8, 1, 12]
large_numbers = []

for i in numbers:
    if i > 6:
        large_numbers.append(i)
    print(large_numbers)

#so here we are making a new list based upon if conditions !

#question 7
#transform a list

def square(x):
    return x * x

numbers = [2,4,6,8]
squares = []

for i in numbers:
    squares.append(square(i))
    print(squares)


#question 8

numbers = [1,5,8,3,9,2,10]
count = 0

for i in numbers:
    if i > 5:
        count += 1
print(count)


# question 9
numbers = [2,5,7,3]

def double(x):
    return x * 2

def square(x):
    return x * x

for i in numbers:
    result = square(double(i))
    print(result)


