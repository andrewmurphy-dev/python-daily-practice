#practice questions !


def find_largest_number(nums):
    if not nums:
        return None

    largest_number = float("-inf")

    for i in nums:
        if i > largest_number:
            largest_number = i


    return largest_number



print(find_largest_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


#just correction !
#the float() needs to be a parenthesis not dicitonary !
#return needs to be outisde the loop !




#question 2

def find_smallest_positive(nums):
    smallest_number = None

    for num in nums:

        #question 1
        if num <= 0:
            continue


        #now we do our conditions !

        #per loop iteration
        #question 2

        if smallest_number is None:
            smallest_number = num
        elif smallest_number < num:
            num = smallest_number

    return smallest_number



print(find_smallest_positive([7, -2, 0, 4, 1, 9]))