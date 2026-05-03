#questions
from week_10_basics_revision.week_1 import largest_number

#question 1
if not nums:
    return None

#question 2

def index_largest(nums):
    largest = nums[0]
    largest_index = 0

    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]
            largest_index = i

    return largest_index, largest



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

# question 9
def second_largest(nums):
    if not nums:
        return None

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:




    return False

#this is a bad approach , but u had sort of the right idea !
#we use min , max !

def second_largest2(nums):
    if not nums:
        return None

    if min(nums) == max(nums):
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num < second_largest:
            second_largest = num
    return second_largest



#question 10


#list length

#below is asserted expected by hand !
[]
[1]
[2, 3]



def second_largest(nums):
    if not nums:
        return None

    if len(nums) <= 1:
        return None

    largest = float('-inf')
    second_largest = float('-inf')


    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num and num > second_largest:
            second_largest = num
    return second_largest



#question 11
#find the second largest and largest mixed with postives and negatives

numbers = [-5, -1, -10, 5, 23]

#so the first is we need to organize the funtion !

def find_largest(numbers):
    if not numbers:
        return None


    #my question is , how do we organize a list
    #so we use the built in function called sorted !

    #i am also worried how would we find the largest for the negatives

    #

def find_largest(numbers):
        if not numbers:
            return None
        ordered = sorted(numbers)

        largest = float("-inf")
        second_largest = float("-inf")

        for order in ordered:
            if order > largest:
                second_largest = largest
                largest = order
            elif largest > order and order > second_largest:
                second_largest = order
        return largest, second_largest

#question 12


nums = [-5, 0, 3, 10, 99]
lo = 0
hi = 10



def clamp_list(nums, lo, hi):
    if not nums:
        return None


    lo = 0
    hi = 10
    new_list = []


    for num in nums:
        if num < lo:
            num = lo
        elif num > hi:
            num = hi
        elif num >= lo and num <= hi:
             hi = num
             lo = num

    return new_list.append(num)

#you where pretty close !




    elif num >= lo and num <= hi:
             hi = num
             lo = num

    #why do this ?
#to make changes right ?
#why do we need to change it ? if we need to leave it alone !
#just dont include it !
#    return new_list.append(num)
#this part here is wrong sadly!

#have no return !

new_list.append(num)

#return new_list

#then u call it !




#solution below !

nums = [-5, 0, 3, 10, 99]
lo = 0
hi = 10

def clamp_list(nums, lo, hi):
    if not nums:
        return []

    new_list = []

    for num in nums:
        if num < lo:
            num = lo
        elif num > hi:
            num = hi

        new_list.append(num)

    return new_list


result = clamp_list(nums, lo, hi)
print(result)



#question 13



user = input("enter numbers: ").strip().split()


def find_fixed(user):
    if not user:
        return None

    user_integers = int(user)

    if not user_integers.isdigit():
        return None

    largest_number = float('-inf')
    second_largest = float('inf')

    for i in user_integers:
        if i > largest_number:
            second_largest = largest_number
            largest_number = i
        elif largest_number > i and i > second_largest:
            second_largest = i

    return second_largest







#simple quick practice


# question 1
def zero_to_zone(x):
    if x == 0:
        return None

    return x




#return None if x == 0 else x



#question 2




if result is None:
    print("result cannot be None")

#question 3

def name_is_none(name):
    if name is None:
        return None
    return name

#return None if name == "" else name






#question 4



def hard_question(nums, k):
    if not nums:
        return None

    sorted_nums = sorted(nums, reverse=True)
    count = 0

    for num in sorted_nums:



#we want to have largest to smallest !

#this was so hard i was so confused !



def nth_largest(nums, k):
    if not nums:
        return None

    unique_nums = set(nums)
    sorted_nums = sorted(unique_nums, reverse=True)

    if k < 1 or k > len(sorted_nums):
        return None

    return sorted_nums[k - 1]


#unique_nums = set(nums)
#this means take nums and remove duplicates !

#my only confusion is here !
#sorted_nums[k - 1]

#this emans , give me the item at the correct python index for rank k

#so hence why we doen error and validation what evr number user outs in for k we get that as a result  !





