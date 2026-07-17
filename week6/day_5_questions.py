#question 1

#find a specfic user

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 28}
]


for i in users:
    if i["username"] == "anna":
        print(i)


#we can also write
print(user["username"], user["age"])



#question 2

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 28}
]

#print only users > 25

for i in users:
    if i["age"] > 25:
        print(i)

#correction
#you need this below

print(i["username"])

# or

print(user["username"], user["age"])



#question 3

#count how many users exist

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 28}
]


count = 0
for i in users:
    count = count + 1
print(count)


#question 4
users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 28}
]

for i in users:
    search = "mike"
if i["username"] == search:
    print(i)


#i am confused why can we not use in

#for example

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 28}
]


for i in users:
    search = "mike"
    if search in users:
        print(search)


#these are both wrong sadly

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 28}
]
search = "mike" #needs to be outside
for i in users:
    if i["username"] == search:
        print(i["username"], i["age"])



#question 5

users = [
    {"username": "andrew", "age": 26},
    {"username": "anna", "age": 24},
    {"username": "mike", "age": 30},
    {"username": "sarah", "age": 28}
]


older = []

for i in users:
    if i["age"] > 25:
        older.append(i)
print(older)


