"""
Week 10 Basics Revision - Day 1
Topic: Largest Number and Second Largest Number
"""

# 1) Write a program that takes a list of integers and prints only the largest number.
#    Example input: [4, 9, 2, 15, 7]

def largest_number(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    # return should be outside the for-loop, so loop checks all numbers first
    return largest


question_1 = largest_number([4, 9, 2, 15, 7])
print(question_1)

# 2) Write a program that takes a list of integers and prints the second largest number.
#    Example input: [4, 9, 2, 15, 7]

def second_Largest(numbers):
   largest = numbers[0]
   second_largest = numbers[0] 

   for i in numbers:
      if i > largest:
      largest = i 
   
   else: 
      if i != largest 
      second_largest = i 

print(second_largest)

#missing : after both if conditions ! 
#else indentation is wrong ! it became a for-else, instead if-else 
#print(second_largest) this is outside the function scope ! 
#logic does not update second_largest when new largest is found ! 
#noi return from the function ! 


def second_largest(numbers):
    if len(numbers) < 2:
        return None

    largest = float("-inf")
    second = float("-inf")

    for n in numbers:
        if n > largest:
            second = largest
            largest = n
        elif largest > n > second:  # keeps second distinct
            second = n

    return None if second == float("-inf") else second


nums = [4, 9, 2, 15, 7]
print(second_largest(nums))  # 9



numbers = [1, 3, 4, 5]

largest_number = numbers[0]

for i in numbers:
    if i > largest_numbers:
        largest_mumbers = i 

    return largest_number



# 3) Write a program that finds both the largest and second largest numbers in one pass (single loop).
#    Example input: [10, 3, 8, 21, 6]

numbers = [10, 3, 8, 21, 6]



def largest_number(numbers):

    if not numbers:
        return None

    largest = float("-inf")
    second_largest = float("-inf")

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num

        elif largest > num and num > second_largest:
            second_largest = num

    return largest, second_largest








#
# 4) Write a program that works when the list contains negative numbers.
#    Example input: [-10, -3, -50, -1, -7]
#    Print largest and second largest


#so its largest , anf second largest

#so the further right the bigger

#so i would like to sort this, would help me understand visually

#so it stil works the same way, because we are working backwards
#hence why -1 is > -50

#-50 ---- -20 ---- -1 ---- 0


#-1 > -50

#and so on


def negative_list_largest(numbers):
    if not numbers:
        return None

    largest = float("-inf")
    second_largest = float("-inf")

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num

        elif largest > num and num > second_largest:
            second_largest = num

    return largest, second_largest



# 5) Write a program that handles duplicate values.
#    Example input: [5, 12, 12, 9, 3]
#    Decide and print the second largest DISTINCT number.

def negative_list_second_largest(numbers):
    if not isinstance(numbers, list):
        return None

    if not numbers:
        return None

    if len(numbers) < 2:
        return None

    unique_values = set(numbers)

    if len(set(unique_values)) < 2:
        return None


    largest = float("-inf")
    second_largest = float("-inf")


    for num in unique_values:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num and num > second_largest:
            second_largest = num

    return largest, second_largest




# 6) Write a program that takes numbers from user input (space-separated), converts them to integers,
#    and prints the largest and second largest numbers.

user = int(input("Enter a number: ")).strip().split()

user_integer = int(user)


def user_integer_largest(user_integer):
    if not isinstance(user_integer, list):
        return None

    if not user_integer:
        return None

    if len(user_integer) < 2:
        return None

    largest = float("-inf")
    second_largest = float("-inf")

    for num in user_integer:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num and num > second_largest:
            second_largest = num

    return largest, second_largest

#
# 7) Write a function largest_and_second_largest(nums) that returns a tuple:
#    (largest, second_largest).
#    Test it with at least 3 different lists.

test_1 = [5, 10, 3, 8]
test_2 = [-10, -3, -50, -1]
test_3 = [7, 7, 2, 9, 9, 4]

def user_integer_second_largest(test_1):
    if not isinstance(test_1, list):
        return None

    if not numbers:
        return None

    if not len(test_1) < 2:
        return None

    largest = float("-inf")
    second_largest = float("-inf")


    for num in test_1:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num and num > second_largest:
            second_largest = num
    return largest, second_largest




# 8) Write a program that validates edge cases:
#    - empty list
#    - list with one element
#    - list where all numbers are equal
#    Print meaningful messages for each case.

if not numbers:
    return None

if len(numbers) < 2:
    return None


if len(set(numbers)) < 2:
    return None



