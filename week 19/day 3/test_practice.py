#qyestion 1 

def add_numbers(a, b):
    return a + b



def test_add_numbers():
    result = add_numbers(2, 3)

    assert result == 5 


#you can also have a variable that can say u expect the answer to be ! 
#for example 


def test_add_numbers():
    result = add_numbers(2, 3)
    expected = 5

    assert result == expected



#question 2 

def double_number(x):
    return x * 2



def test_double_number():
    result = double_number(4)
    expected = 8 

    assert result == expected 





#so for example finding the largest number 

list = [1,3,4,55]

def largest_number(list):
    largest_num = float("-inf")


    for num in list:
        if num > largest_num:
            largest_num = num 

    return largest_num 



def test_largest_number():
    result = largest_number(list)
    expected = 55

    assert result == expected



#same thing ! 



#hard python question 

numbers = [4, 2, 4, 3, 2, 4, 5]

def most_frequent_number(numbers):
    

    counts = {}

    for num in numbers:
        if num in counts:
            counts[num] += 1

        else:
            counts[num] = 1



#= store this value 

{4: 3, 2: 2, 3: 1, 5: 1}

#num is the key , so we use use count to see how many tie it appears 



#next we use counts[num] which finds value to find the most common one that turned up 


for num in counts:
    if counts[num] > largest_count:
        largest_count = counts[num]




    


    

        

    