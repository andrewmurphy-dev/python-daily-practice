#just practice questions !

#question 1 
user = input("Enter your name: ")

print(user.lower())



#above is temporary storage

#below is storage in memory reference

user_name = user.lower()
print(user_name)

#question 2

make_sentence = input("make a sentence: ")

sentence = make_sentence.split()
print(sentence)

['hello', 'nice', 'to', 'meet', 'you', 'my', 'name', 'is', 'andrew']


#question 3

email_make = input("enter your email address: ")

email_made = email_make.split()
print(email_made)

if "@" in email_made:
    print("Email address is valid")
else:
    print("Email address is invalid")

#question 4
text_make = input("make a sentence containing the word python: ")


change_text = text_make.replace("python", "coding")

print(change_text)




#question 5
sentence_create = input("enter your sentence here: ")

sentence_created = sentence_create.split()
print(sentence_created)

count = 0

for word in sentence_created:
    count = count + 1

print(count)




#question 6


#ask user for a sentence

user_ask_1 = input("enter your sentence here: ")

#converts the sentence to lower case

lower_case = user_ask_1.lower()


#splits the ssentence into words
words_lower = lower_case.split()
print(words_lower)





