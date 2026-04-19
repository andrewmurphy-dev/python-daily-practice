#question 1

nums = [5, 5, 5]

def average():
    count = 0
    for i in len(nums):
        count += i
        average = count / i + 1
        print(average)
        
        if i > average:
            print("i is greater than average")
        else:
            print("i is less than average")



#this is wrong ! 


def count_above_running_avg(nums):
    running_sum = 0
    count = 0

    for i, num in enumerate(nums):
        running_sum += num
        avg = running_sum / (i + 1)

        if num > avg:
            count += 1

    return count

#or 

def count_above_running_avg(nums):
    count = 0
    running_sum = 0

    for i in range(len(nums)):
        running_sum += nums[i]
        avg = running_sum / (i + 1)

        if nums[i] > avg:
            count += 1

    return count



#what does range() do ?

#it generates a sequence of numbers !
#range(start, stop, step)

#start default is 0
#step default is 1


#what does len do ? 
#how many elements are in the list ?



#so what does range(len(nums)) do ?
#this gives me all the valid indexes for the list !

#range needs a integer ! 
#numns is a list! 

#for example 

nums = [10, 20, 30]

print(nums)        # [10, 20, 30]
print(len(nums))   # 3



