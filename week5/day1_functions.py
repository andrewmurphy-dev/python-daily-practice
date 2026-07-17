#question 1

def count_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count


print(count_even([1, 2, 3, 4, 5]))

#return must be outside the if statement !

#10/10


#question 2

#find the largest number

def largest_number(numbers):
    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i
    return largest


#stored
y = largest_number([1, 2, 3, 4, 5])
print(y)

#not stored
print(largest_number([4, 6, 89, 2000]))


#question 3

#count evens

def count_even(x):
    count = 0
    for i in x:
        if i % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 5]))

#question 4

#count odd numbers
def count_odd(x):
    count = 0
    for i in x:
        if i % 2 != 0:
            count += 1
    return count

print(count_odd([1, 2, 3, 4, 5]))


#question 4

def sum_list(list):
    total = 0
    for i in list:
        total += i
    return total
print(sum_list([1, 2, 3, 4, 5]))


