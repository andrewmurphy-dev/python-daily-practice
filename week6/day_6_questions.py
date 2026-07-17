#question 1

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19}
]



for user in users:
    print(user["username"])

#loop → access key → output value


#question 2

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19}
]


ages = []

for user in users:
    ages.append(user["age"])

print(ages)


#question 3

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19}
]


older_users = []


for user in users:
    older_users.append(user["username"], user["age"])
print(older_users)

#append only adds one object to the list , not two !


#so the solution is

for user in users:
    older_users.append(user)

print(older_users)



#question 4

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19}
]


older_users = []

for user in users:
    if user["age"] > 25:
        older_users.append(user)

print(older_users)


#question 5
users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19}
]


x = []

for user in users:
    if user["age"] < 25:
        x.append(user["username"])

print(x)


#question 6

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19}
]


older_users = []

for o_user in users:
    if o_user["age"] > 25:
        older_users.append(o_user["username"])

print(older_users)




#question 7

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19}
]


x = []


for user in users:
    if user["age"] > 25:
        x.append(user)

print(x)
