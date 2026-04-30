#questions
from week_10_basics_revision.week_1 import largest_number

#question 1
if not nums:
    return None

#question 2




#what is nums[i]? this gives the value !
#index:  0   1   2
#value:  4  10   3

#nums[0]  # 4
#nums[1]  # 10
#nums[2]  # 3


#question 3
#index of the first negative nums !

def index_of_negative_nums(nums):
    if not nums:
        return None


    for i in range(len(nums)):
        if nums[i] < 0:
            return i
    return None





#question 4

def count_even_numbers(nums):
    if not nums:
        return None


    count = 0

    for i in nums:
        if i % 2 == 0:
            count += 1

    return count


#question 5

def sum_list(nums):
    if not nums:
        return None

    total = 0

    for i in nums:
        total += i
    return total



#questin 6
def count_positive_nums(nums):
    if not nums:
        return None


    count = 0

    for num in nums:
        if num < 0:
            continue
        if num > 0:
            count += 1

    return count



#question 7

def posotive_numsbers(nums):
    if not nums:
        return None


    for i in nums:
        if i >= 0:
            return False
    return True






#question 8


def has_duplicate_nums(nums):
    if not nums:
        return None

    for i in nums:
        for j in nums:
            if i == j:
                return False

    return True


#this logic is wrong

#we need to do range(len(nums))
#because we need to compare two different positions on the list !


#first position

for i in range(Len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            return True #finding the first true duplicate

return False


