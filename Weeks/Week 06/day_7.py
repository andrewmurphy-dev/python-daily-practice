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


for user in users:
    user["age"] = user["age"] + 1 
print(users)




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

