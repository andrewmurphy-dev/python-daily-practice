#questions




#question 1

#access a dictionary in a list

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30}
]


print(users[1]["age"])



#question 2

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30}
]

#loop though the list
#print every name

for i in users:
    print(i["username"])

#question 3

#access multiple fields



users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30}
]


for i in users:
    print(i["username"], i["age"])


#question 4
#increase every user:s age by 1

users = [
 {'username': 'andrew', 'age': 27},
 {'username': 'anna', 'age': 25},
 {'username': 'mike', 'age': 31}
]



for i in users:
    i["age"] = i["age"] + 1

print(users)





#question 5

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30}
]


users.append({"username": "john", "age": 22})

print(users)


