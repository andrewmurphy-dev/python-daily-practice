#so for day 7 we are mainly gonnna do some questions

#username counter
#question 1
username = input("enter a sentence: ").lower().split()

dict = {}

for word in username:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1


for word, value in dict.items():
    print(word, value)




#question 2

#most common username
sentence = input("enter a sentence: ").lower().split()

common = {}

for word in sentence:
    if word in common:
        common[word] += 1

    else:
        common[word] = 1


largest = 0
largest_value = ""


for word, value in common.items():
    if value > largest:
        largest = value
        largest_value = word

print(largest_value, largest)


#exercise 3
sentence_email = input("enter your email: ").lower().split()


for email in sentence_email:
    if "gmail" in email:
        print(email)




#longest word
#question 4

sentence = input("enter a long sentence: ").lower().split()

#print the longest word
largest = len(sentence[0])
largest_name = ""

for word in sentence:
    if len(word) > largest:
        largest = len(word)
        largest_name = word

print(largest_name, largest)


#8/10

#question 5




#question 6

inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}


product_name = input("enter a product name: ").lower()


if product_name in inventory.keys():
    print("stock:", inventory[product_name])
else:
    print("product not found")

