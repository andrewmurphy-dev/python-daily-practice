#6. Medium

#Given a list of numbers, find the index of the largest value.



list = [1, 2, 3, 4, 5]

#index , 0 , 1 , 2 , 3 , 4

#so we want to find the index of the largest value 

so it will be like , i assume the structure will be like this :

list[0] = 1
list[index] = value



def find_largest_value(list):
    largest_index = 0
    for index, value in enumerate(list):
        if value > list[largest_index]:
            largest_index = value #you do not put value here cause you want to track the index of the largest value
            return index #you do not put the return in the if statement , you put it outside the if statement, because it will stop at the first time it is greater




i am just using the index to track the largest value 
but its index lol 


def find_largest_value(list):
    largest_index = 0
    for index, value in enumerate(list):
        if value > list[largest_index]:
            largest_index = index 

    return largest_index






#question 7 

#7. Medium

#Given a list of numbers, return a new list containing only the elements that are greater than their previous element (you must use the index properly).



numbers = [4, 2, 12, 4, 5]

#so we neeed to return a new list 

#so we need to make a list variable to store the new list 

result = []

#we need to use append()

#i think its asking me to find value, index of the elements that are greater than their previous element 



def find_greater_than_previous(numbers):

    result = []
    previous = 0

    for index, value in enumerate(numbers):
        if value > numbers[previous - 1]:
            result.append(value)



#two things wrong with this code :

#1. we are not using the index properly
#2 no return statement 

def find_greater_than_previous(numbers):

    result = []
   
    for index, value in enumerate(numbers):
        if index > 0 and value > numbers[index - 1]:
            result.append(value)
    return result



#whats the difference bwteen return with append inside the loop and outside the loop ?
# return INSIDE the loop — stops on first match, returns a single value
for index, value in enumerate(numbers):
    if value > numbers[index - 1]:
        result.append(value)
        return result  # ❌ exits after first match

# return OUTSIDE the loop — waits until everything is collected
for index, value in enumerate(numbers):
    if value > numbers[index - 1]:
        result.append(value)  # keeps adding
return result  # ✅ returns the full list at the end



#question 8 

#Given a list of strings, return the index of the longest string.


strings = ["apple", "banana", "cherry", "date"]

#so we need to find the index of the longest string 

#so we need to make a variable to store the longest string 






def find_longest_string(strings):
    shortest_index = 0

    for index, value in enumerate(strings):
        if len(value) > len(strings[shortest_index]):
            shortest_index = index

    return index

#7/10 


#two small mistakes
#name of the tracking variable is not correct 
#return index 

#correct below 

def find_longest_string(strings):
    longest_index = 0

    for index, value in enumerate(strings):
        if len(value) > len(strings[longest_index]):
            longest_index = index

    return longest_index