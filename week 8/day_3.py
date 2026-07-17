#today we are gonna learn about the enumerate function examples 


#question 1 

numbers = [10, 20, 30, 40, 50]

for index, value in enumerate(numbers):
    print(index, value)




#question 2 
strings = ["apple", "banana", "cherry", "date"]

for index, value in enumerate(strings):
    if value == "apple":
        print(index)

#question 3 



def count_even_numbers(numbers):
    count = 0
    for index, value in enumerate(numbers):
        if value % 2 == 0:
            count += 1
    return count, index


    
test = count_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(test)

#this attempt is a 8/10 

#the only issue in the question they asked for the index too 


def count_even_numbers(numbers):
    count = 0
    positions = []
    for index, value in enumerate(numbers):
        if value % 2 == 0:
            count += 1
            positions.append(index)
    return count, positions


#apprach 1 
#accumulator pattern

def count_even_numbers(numbers):
    count = 0
    positions = []
    for index, value in enumerate(numbers):
        if value % 2 == 0:
            count += 1
            positions.append(index)
    return {"count": count, "positions": positions}


#apprach 2
#you can also make this into a dicitonary to make it more readable  
def count_even_numbers(numbers):
    result = {}
    for index, value in enumerate(numbers):
        if value % 2 == 0:
            result[index] = value
    return result

#question 4 

target = 5


def find_first_occurrence(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index
    else:
        return -1


test = find_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print(test)

#9/10 

#there is one small issue in the question they asked for the index too 
#you actually do not need to use else 

#your beginner mindset always thinks to use else

for ...:
    ...
else:
    # runs when the loop finishes WITHOUT a break
    # has nothing to do with your if condition

#It's confusing because it looks like it means "if not found" but it actually means "if no break happened". In your case it worked by accident, but it's not the right tool — and it would break if you ever used break in your loop.

#So the rule of thumb: if you're using return inside a loop, you don't need else


#question 5 

def print_greater_than_index(numbers):

    for index, value in enumerate(numbers):
        if value > index:
            return value

        

test = print_greater_than_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(test)


#6/10 

#1 bugs in the code 

return value  # ❌ stops after first match
print(value)  # ✅ continues through the whole loop



#question 6 

def find_largest_value(numbers):
    largest = numbers[0]
    result = {}

    for index, value in enumerate(numbers):
        if value > largest:
            largest = value
            result[index] = largest
    return result

#6/10 

#What went wrong:

#Used a dictionary when the question just wants a single index returned
#The dictionary stored every new largest found, not just the final one
#return result gives back a dict instead of a number

        
#solution below 

def find_largest_value(numbers):
    largest_index = 0
    for index, value in enumerate(numbers):
        if value > numbers[largest_index]:
            largest_index = index
    return largest_index



#question 7 

def find_greater_than_previous(numbers):
    previous = 0 
    result = []

    for index, value in enumerate(numbers):
        if value > numbers[previous]:
            result.append(value)  
    numbers[previous] = value

#5/10 

#What went wrong:

#numbers[previous] = value — updates the list itself instead of moving the tracker forward, this corrupts your data
#Update line was outside the loop — only runs once after everything is done, so previous never actually moves during the loop
#Missing return result at the end
#Index 0 never gets skipped — comparing numbers[0] to itself on the first iteration

#solution below 

def find_greater_than_previous(numbers):
    previous = 0 
    result = []
    for index, value in enumerate(numbers):
        if value > numbers[previous]:
            result.append(value)

#question 8 


def longest_string(strings):

    for index, value in enumerate(strings):
        if len(value) > len(strings[index]):
            return value


#[] → access
#len() → measure
#Combined → measure something you accessed
#solution below 

def longest_string(strings):
    longest_index = 0
    for index, value in enumerate(strings):
        if len(value) > len(strings[longest_index]):
            longest_index = index
    return longest_index


#this pattern is called tracking the best so far 