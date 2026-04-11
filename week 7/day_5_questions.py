#question 1

username = input("Enter your username: ").strip().lower()

print(username)



#question 2
#safe contact search
contacts = {
    "andrew": "123",
    "anna": "456"
}

username_ask = input("Enter your username: ").strip().lower()

phone = contacts.get(username_ask, "contact not found")
print(phone)



#question 3
#gmail filter

contacts = {
    "andrew": "andrew@gmail.com",
    "anna": "anna@yahoo.com",
    "mike": "mike@gmail.com"
}


for username, email in contacts.items():
    if "gmail" in email:
        print(username)


#question 4
#gmail counter


gmail_count = 0
for username, email in contacts.items():
    if "gmail" in email:
        gmail_count += 1
print(gmail_count)


#question 5
#word counter
word_count = 0
sentence = input("Enter your sentence: ").split()

for word in sentence:
    word_count += 1

print(word_count)



