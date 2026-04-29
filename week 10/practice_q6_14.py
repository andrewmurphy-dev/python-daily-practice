# Practice: Questions 6-14
# Write your code under each question.


# 6. Write a function that shows what return does to the rest of a function.
def return_practice(nums):
    for i in nums:
        if i == 2:
            return i 

    return "2 was not found"
    



# 7. Write a function that has two different return paths.

def return_practice(nums):
    for i in nums:
        if i > 4:
            return i 
        elif i < 4:
            return i 


#better way to do it is 

def return_practice(nums):
    if nums > 4:
        return "big"

    else:
        return "small"
    


# 8. Write a function named second_largest(nums).
# Return None for [8] and for [2, 2, 2].
def second_largest(nums):
    if nums == 8:
        return None
    
    elif nums == [2, 2, 2]:
        return None


#8 should be [8] , beacuae it is a  list 
#better way to do it is to not do hardcoding those list ! 


def second_largest(nums):
    if len(nums) < 2:
        return none 

# 9. Write code for a < b < c using two comparisons with and.

if a < b and b < c:
    print("b is between a and c")



# 10. Write code using this condition:
# elif largest > n > second:

def return_understanding(nums):
    if nums < 2:
        return none


    largest = float("-inf")
    second = float("-inf")

    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif largest > n > second:
            second = n 

    return largest, second




# 11. Write code that uses float("-inf") as a starting max or second max value.

def return_understanding(nums):

    largest = nums[0]
    second = float("-inf")

    for n in nums:
        if n > largest:
            second = largest
            largest = n 
        elif largest > n and n > second:
            second = n 
    return largest, second 


# 12. Write one ternary expression using:
# x if condition else y

if x > 5:
    return "big"
else:
    return "small"


x if > 5 return "big" else "small"




#you where close !



def ternary_understanding(x):
    return "big" if x > 5 else "small"


# 13. Write one normal if/else version and one ternary version that choose between two values.

def normal_understandign(nums):
    if nums > 50:
        return "very old"
    elif nums < 49 and nums > 18:
        return "young adult"






def tenerary_understanding(nums):
    return "very old" if nums > 50 else "young adult"

#this was basically correct

return "very old" if age > 50 else "young adult" if age > 18 and age < 49 else "other"




 else "young adult" if age > 18 and age < 49 else "other"

# 14. Write code showing dict.get(k) vs d[k] when the key is missing.


print(dict.get("andrew"))

print(dict["andrew"])
