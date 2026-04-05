#questions


#question 1

users = [
    {"username": "andrew", "age": 26, "country": "Ireland"},
    {"username": "anna", "age": 24, "country": "Germany"},
    {"username": "mike", "age": 30, "country": "USA"},
    {"username": "sarah", "age": 19, "country": "Ireland"},
    {"username": "leo", "age": 27, "country": "France"}
]

for user in users:
    print(user["username"])


#question 2


users = [
    {"username": "andrew", "age": 26, "country": "Ireland"},
    {"username": "anna", "age": 24, "country": "Germany"},
    {"username": "mike", "age": 30, "country": "USA"},
    {"username": "sarah", "age": 19, "country": "Ireland"},
    {"username": "leo", "age": 27, "country": "France"}
]

ages = []


for user in users:
    ages.append(user["age"])
print(ages)




#question 3
users = [
    {"username": "andrew", "age": 26, "country": "Ireland"},
    {"username": "anna", "age": 24, "country": "Germany"},
    {"username": "mike", "age": 30, "country": "USA"},
    {"username": "sarah", "age": 19, "country": "Ireland"},
    {"username": "leo", "age": 27, "country": "France"}
]


for user in users:
    print(user["username"], user["age"])



#question 4

#increase every user age by 1

users = [
    {"username": "andrew", "age": 26, "country": "Ireland"},
    {"username": "anna", "age": 24, "country": "Germany"},
    {"username": "mike", "age": 30, "country": "USA"},
    {"username": "sarah", "age": 19, "country": "Ireland"},
    {"username": "leo", "age": 27, "country": "France"}
]



for key, value in users.items():
    user["age"] + 1
    print(user)


for key, value in users.items():

#this is invalid , this is a dictionary method

user["age"] + 1
##this calculates the value but does not store it




#lets try again

for user in users:

    #above is loop through the list !
    user["age"] = user["age"] + 1 #
    #see this is where i get confused , the access key !
    #i want to access age ! so hpw do i do that ?
    #i assume its value["age"]
    #there is no variable called value , there is a variable called user

    #WE PRINT USERS HERE !

    #WHY ?
    #we are not making a new list


#question 5



users = [
    {"username": "andrew", "age": 26, "country": "Ireland"},
    {"username": "anna", "age": 24, "country": "Germany"},
    {"username": "mike", "age": 30, "country": "USA"},
    {"username": "sarah", "age": 19, "country": "Ireland"},
    {"username": "leo", "age": 27, "country": "France"}
]


countries = []

for user in users:
    countries.append(user["country"])

print(countries)
