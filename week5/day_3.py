#today we strengthen 3 things

#1 comparisons inside functions
#2 using len()
#3 combining multiple conditions !


#question 1
def longest_word(word1, word2):
    if len(word1) > len(word2):
        return len(word1)
    elif len(word2) > len(word1):
        return len(word2)
    else:
        print("they are both the same length")


print(longest_word("cat", "elephant"))

#7/10


#what is the differrence between thee longest word and the length

#len()
#this measures size


##longest word , returns the word not the length

#so correction maybe would be !


def longest_word(word1, word2):
    if len(word1) > len(word2):
        return (word1)
    elif len(word2) > len(word1):
        return (word2)
    else:
        print("they are both the same length")


print(longest_word("cat", "elephant"))



#9/10

#see this programme if they are the same lenth it will aut say none !
#so you must put a return , ("they are both the same length") then it will work !













#question 2

#list length check !



def long_list(first):
    if len(first) > 5:
        return True
    else:
        return False

print(long_list([1,2,3,4,5,6]))


#a




#question 3
#count short words

def count_short_words(word):
    count = 0
    for letter in word:
        if len(letter) < 5:
            count += 1
    return count

print(count_short_words("cat"))

#a


#question 4 !
#password strentgh

def password_strength(password):
    if len(password) < 6:
        return "weak"
    elif len(password) < 10:
        return "medium"
    else:
        return "strong"


print(password_strength("anjdaaaf"))


#10/10