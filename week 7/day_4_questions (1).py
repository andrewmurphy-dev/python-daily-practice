#questions day 4 practice

#question 1
#print the usernames
contacts = {
    "andrew": "123",
    "anna": "456",
    "mike": "789"
}

for user in contacts.keys():
    print(user)



#question 2
#print the phone numbers




#question 3
#print both names and phone numbers

for user in contacts.items():
    print(user)


#question 4
#safe search

contacts = {
    "andrew": "123",
    "anna": "456",
    "mike": "789"
}

ask_username = input("What is your name?: ")

if ask_username in contacts:
    print(contacts.get(ask_username, "contact not found"))


#this is a 8/10

#i mixed two patterns

#membership check

if name in contacts

#and

contacts.get("ask_username", "not found")


#you usually dont use membership search and .get() in the same !



#question 5
#gmail filter

contacts = {
    "andrew": "123",
    "anna": "456",
    "mike": "789"
}


for value in contacts.values():
    if value == "gmail":
        print(value)
#wrong dicitonary
#wrong use of ==
#in is used for paritial match
#== this is used for exact identical match




#correct solution
contacts = {
    "andrew": "andrew@gmail.com",
    "anna": "anna@yahoo.com",
    "mike": "mike@gmail.com"
}

for name, email in contacts.items():
    if "gmail" in email:
        print(name)







