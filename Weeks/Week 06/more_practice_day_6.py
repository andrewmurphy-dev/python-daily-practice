#question 1
users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19},
    {"username": "john", "age": 40},
]



for user in users:
    print(user["username"])



#question 2

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19},
    {"username": "john", "age": 40},
]


for user in users:
    if user["age"] > 25:
        print(user["username"])



#question 3
users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19},
    {"username": "john", "age": 40},
]



for user in users:
    if user["age"] < 25:
        print(user["username"])


#question 4
users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19},
    {"username": "john", "age": 40},
]

total = 0

for user in users:
    if user["age"] % 2 == 0:
        total = total + user

print(total)

#this is wrong

#solution below

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 19},
    {"username": "john", "age": 40},
]

total_age = 0

for user in users:
    total_age = total_age + user["age"]

average_age = total_age / len(users)

print(average_age)





