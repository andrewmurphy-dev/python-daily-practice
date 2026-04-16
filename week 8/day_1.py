"""
Day 1 Python Practice: Loop Memory (previous/current)

How to use:
1) Solve one question at a time under its section.
2) Run this file with: py day_1.py
3) Compare your output with what you expect.
"""

print("Day 1 practice loaded.")


# ============================================================
# Question 1: Count adjacent equal matches
# List: [1, 1, 2, 2, 3]
# Goal: Count how many times current value equals previous value.
# ============================================================

numbers = [1, 1, 2, 2, 3]
count = 0
previous = numbers[0]

for i in numbers:
    if i == previous:
        count += 1
    previous = i

print("Q1:", count - 1)


# ============================================================
# Question 2: Explain loop order (in comments)
# 1) current gets value
# 2) comparison
# 3) count update (if needed)
# 4) memory update
# ============================================================

# Your explanation:
# The current value is compared to the previous value.
# Then previous is updated to current for the next iteration.


# ============================================================
# Question 3: First number where change happens
# List: [5, 5, 5, 7, 7]
# Goal: Print the first number that is different from the start.
# ============================================================

numbers = [5, 5, 5, 7, 7]
previous = numbers[0]

for i in numbers:
    if i != previous:
        print("Q3:", i)
        break
    previous = i


# ============================================================
# Question 4: Count number of changes
# List: [1, 1, 2, 2, 3]
# Goal: Count how many times value changes left to right.
# ============================================================
numbers = [1, 1, 2, 2, 3]
count = 0
previous = numbers[0]

for i in numbers:
    if i != previous:
        count += 1
    previous = i

print("Q4:", count)



# ============================================================
# Question 5: Predict output first, then verify
# List: [4, 4, 4, 5]
# ============================================================




# ============================================================
# Question 6: Adjacent equal pairs
# List: [1, 1, 2, 2, 2, 3]
# Goal: Count adjacent equal pairs only.
# ============================================================

numbers = [1, 1, 2, 2, 2, 3]
count = 0
previous = numbers[0]

for i in numbers:
    if i == previous:
        count += 1
    previous = i

print("Q6:", count - 1)


# ============================================================
# Question 7: Print every change point
# List: [5, 5, 7, 7, 2, 2, 9]
# Goal: Print values where a new group starts.
# ============================================================
numbers = [5, 5, 7, 7, 2, 2, 9]
previous = numbers[0]
print("Q7:")
for i in numbers:
    if i != previous:
        print(i)
    previous = i


# ============================================================
# Question 8: Count groups
# List: [1, 1, 2, 2, 3, 3, 3, 1]
# Goal: Count how many groups exist.
# ============================================================

numbers = [1, 1, 2, 2, 3, 3, 3, 1]
changes = 0
previous = numbers[0]

for i in numbers:
    if i != previous:
        changes += 1
    previous = i

groups = changes + 1
print("Q8:", groups)


# ============================================================
# Question 9: First index where change happens
# List: [8, 8, 8, 8, 10, 10]
# Goal: Print first index where value changes from the start.
# ============================================================

numbers = [8, 8, 8, 8, 10, 10]
previous = numbers[0]
current = numbers[0]

for current in numbers:
    if current != previous:
        print(current - 1)
        break
    previous = current



#so this is wrong ! 
#the reason being we are not using the index of the list !
#we are using the value of the list !
#so we need to use the index of the list !
#so we need to use the enumerate function !
#so we need to use the enumerate function to get the index of the list !
list = [8, 8, 8, 8, 10, 10]
start = numbers[0]

for index, value in enumerate(numbers):
    if value != start:
        print(index)
        break


# ============================================================
# Question 10: Is list non-decreasing?
# Goal: True if values never go down, else False.
# ============================================================




def is_non_decreasing(numbers):
    """Return True when values never decrease left-to-right."""
    previous = numbers[0]


    for current in numbers:
        if current > previous or current == previous:
            return True
        
    else:
        return False

    previous = current


    

test_1 = [1, 2, 2, 4]

test_2 = [1, 2, 3, 4]


result_1 = is_non_decreasing(test_1)
print(result_1)

result_2 = is_non_decreasing(test_2)
print(result_2)


#grade 6/10 


#below is the correct code for question 10 


def is_non_decreasing(numbers):
    """Return True when values never decrease left-to-right."""
    if not numbers:
        return True  # empty list is considered non-decreasing

    previous = numbers[0]
    for current in numbers[1:]:
        if current < previous:
            return False
        previous = current
    return True


test_1 = [1, 2, 2, 4]
test_2 = [1, 3, 2, 5]

print(is_non_decreasing(test_1))  # True
print(is_non_decreasing(test_2))  # False


#how is an empty list considered non-decreasing ?

#an empty list is considered non-decreasing because there are no values to compare, so it satisfies the condition of never decreasing.
#it is true because there are no values to compare, so it satisfies the condition of never decreasing.
