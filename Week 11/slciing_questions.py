#question 1
def first_three(text):
    return text[:3]


#question 2

def last_three(text):
    return text[len(text) - 3: len(text): 1]


result = last_three("Steptrace")
print(result)



#question 3

def reverse(text):
    return text[len(text) - 1: len(text) - 1: -1]
#why do we use minus 1?
#revese starts at 1 not 0

#question 4
def middle_text(text):
    return text[2:5:1]


#question 5
def remove_first_two(text):
    return text[2:len(text):1]

#question 6
def remove_last_two(text):
    return text[len(text) - 2: len(text) - 1: -1]

#question 7

def every_second_char(text):
    return text[2:len(text): 2]

#question 8
def every_second_reverse(text):
    return text[len(text): len(text) - 2: -2]


#question 9

def first_half(text):
    return text[0:len(text) // 2 :1]


#question 10

def second_hald(text):
    return text[len(text) // 2:len(text) - 1 :1]

#question 11
def swap_edges(text):
    middle = len(text) // 2
    return text[len(text) - 3: len(text): 1] + text[middle - 1: middle + 2: 1] + text[0:middle: 1]

#question 12

def reverse_last_three(text):
    return text[len(text) -1: -len(text) - 1: -1]

#question 13

def reverse_first_three(text):
    return text[2:-len(text) -1: -1]

#question 14
def remove_middle(text):
    return text[0:3:1] + text[-3:len(text):1]
    
#question 15
def middle_reverse(text):
    middle = len(text) // 2
    return text[middle + 1: -len(text) - 1: -1]



