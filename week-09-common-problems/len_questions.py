#questions for len()

#Q1 — Write a function longer_word(a, b) that takes two strings and returns whichever is longer.

def longer_word(a, b):
    if len(a) > len(b):
        return a
    else:
        return b


  

#question 2 

def count_long_words(words):
    if len(words) > 5:
        return True
    else:
        return False

#two problems 

#problem 1 
#you are not returning the count of the long words !
#you are returning a boolean value !

def count_long_words(words):
    count = 0
    for word in words:
        if len(word) > 5:
            count += 1
    return count



#question 3 

def all_words(words):
    for word in words:
        if len(word) > 4:
            return False
    return True



#question 4 

def find_shortest(words):
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

#question 5 

def shortest_word(words):
    shortest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
    return shortest_word
    
#question 6 

def word_longer_than(words, n):
    list = []

    for word in words:
        if len(word) > n:
            list.append(word)
    return list

    