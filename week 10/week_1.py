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



#
# 3) Write a program that finds both the largest and second largest numbers in one pass (single loop).
#    Example input: [10, 3, 8, 21, 6]
#
# 4) Write a program that works when the list contains negative numbers.
#    Example input: [-10, -3, -50, -1, -7]
#    Print largest and second largest.
#
# 5) Write a program that handles duplicate values.
#    Example input: [5, 12, 12, 9, 3]
#    Decide and print the second largest DISTINCT number.
#
# 6) Write a program that takes numbers from user input (space-separated), converts them to integers,
#    and prints the largest and second largest numbers.
#
# 7) Write a function largest_and_second_largest(nums) that returns a tuple:
#    (largest, second_largest).
#    Test it with at least 3 different lists.
#
# 8) Write a program that validates edge cases:
#    - empty list
#    - list with one element
#    - list where all numbers are equal
#    Print meaningful messages for each case.
#
# 9) Write a program without using built-in max() or sorting.
#    Use only loops and conditions to find largest and second largest.
#
# 10) Write a program that reads N numbers one by one and updates largest/second largest as input arrives,
#     then prints final largest and second largest at the end.

