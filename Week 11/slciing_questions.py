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


