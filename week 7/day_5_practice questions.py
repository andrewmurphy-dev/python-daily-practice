#question 1
products = ["apple juice", "orange juice", "milk", "bread"]
product_name = input("enter product name: ").strip().lower()

if product_name in products:
    print("product available")
else:
    print("product not found")




#question 2
#email domain counter




#question 3
#detect duplicate words


sentence = input("enter a sentence: ").lower().split()

#how can i find a duplicate

#we need two tracking variables


previous = sentence[0]
count_words = 0


for present in sentence:
    if present == previous:
        count_words = count_words + 1
        print(count_words - 1, "duplicates found")
        break
else:
    print("no duplicates")


#the correct version

#i needed to add a seen tracker
#also the question specficially asked does a duplicate exist , again read the question

seen = []
sentence = input("enter a sentence: ").lower().split()

for user in sentence:
    if user in seen:
        print("duplicate found!")
        break
    seen.append(user)
else:
    print("no duplication found")


#question 4

sentence = input("input a sentence: ").lower().split()

print(sentence)


len

for word in sentence:
    if len(word) >



#so we know we need to do len(words)
sentence = input("enter a sentence: ").split()

longest_word = sentence[0]

for word in sentence:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)



#question 5
#order counter

#ask the user to enter food orders seperated by spaces

user_ask = input("enter food order please!: ").split()
count = 0
for user in user_ask:
    if user == "burger":
        count = count + 1
print(count)

#question 6
#username validation

username = input("enter a username: ")

if " " not in username and username == username.lower():
    print("valid username")
else:
    print("invalid username")
