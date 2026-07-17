#these questions are more realistic

#question 1
contacts = {
    "andrew": "andrew@email.com",
    "anna": "anna@email.com",
    "mike": "mike@email.com"
}


name = input("Enter your name: ")

if name in contacts:
    print("contact exists")
else:
    print("contact does not exist")


#question 2
#prevent duplicate account


users = ["andrew", "anna", "mike"]


create_username = input("Enter your username: ")

if create_username in users:
    print("username already exists")

else:
    print("account created")


#question 3
#game inventory

inventory = ["sword", "shield", "potion", "armor"]

item_ask = input("Enter your item: ")
if item_ask in inventory:
    print("item available")

else:
    print("item does not exist")

    

