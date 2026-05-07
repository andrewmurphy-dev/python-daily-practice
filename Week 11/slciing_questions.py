#question 1
def first_three(text):
    return text[:3]


#question 2

def last_three(text):
    return text[len(text) - 3: len(text): 1]


result = last_three("Steptrace")
print(result)




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
