
#question 1
#list memborship


#question 2
#list memborship (egative)

users = ["anna", "mike", "leo"]

name = input("enter username: ")

if name not in users:
    print("user not found")


#question 3
#dictionary memborship

contacts = {
    "andrew": "andrew@gmail.com",
    "anna": "anna@gmail.com"
}

name = "andrew"

#check if andrew exists

if name in contacts:
    print("user exists")

#mental model you must lock in if key in dictionary


#question 4
#dictionary memborship

contacts = {
    "andrew": "andrew@gmail.com",
    "anna": "anna@gmail.com"
}



username = input("enter a username: ")

if username in contacts:
    print("found")
else:
    print("not found ")


#question 5
#string memborship
#check if "@" exists in the string


contacts = {
    "andrew": "andrew@gmail.com",
    "anna": "anna@gmail.com"
}

email = "andrew@gmail.com"

if "@" in email:
    print("valid email")
else:
    print("invalid email")


#remember

#in ---> search inside something
# == ----> compare two things
#in doesnt have to correlate to container , it can correlate to values too
#because it depends on the question


#question 6
#string memborship

contacts = {
    "andrew": "andrew@gmail.com",
    "anna": "anna@gmail.com"
}


if "@" not in contacts:
    print("invalid email")
else:
    print("valid email")

#question 7
#list memborship search
cities = ["tokyo", "osaka", "kyoto", "nagoya"]

city_ask = input("enter a city: ")

if city_ask in cities:
    print("city found")
else:
    print("city not found")


#question 8
#prevent duplications
users = ["anna", "mike", "leo"]

username = input("please enter a new username: ")

if username in users:
    print("username exists")
else:
    print("account created")

#question 9
users = ["anna", "mike", "leo"]

username = input("please enter a new username: ")

if username not in users:
    users.append(username)

print(users)

#question 10
#dictionary check before access

contacts = {
    "andrew": "123456",
    "anna": "987654"
}

username = input("please enter a username: ")

if username in contacts:
    print(contacts[name])
else:
    print("contact not found")

