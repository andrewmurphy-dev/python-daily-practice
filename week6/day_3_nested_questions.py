#so lets practice some questions !


#question 1
users = {
    "andrew": {"age": 26, "country": "Japan"},
    "anna": {"age": 24, "country": "Germany"}
}

print(users["andrew"]["country"])


#question 2
users = {
    "andrew": {"age": 26, "country": "Japan"},
    "anna": {"age": 24, "country": "Germany"}
}

print(users["anna"]["age"])


#question 3
#update nested data !

users = {
    "andrew": {"age": 26, "country": "Japan"},
    "anna": {"age": 24, "country": "Germany"}
}


#update andrew age to 27
users["andrew"]["age"] = 27
print(users)

#question 4
#add a new field for andrew
#"job": "developer"

users = {
    "andrew": {"age": 26, "country": "Japan"},
    "anna": {"age": 24, "country": "Germany"}
}


users["andrew"]["job"] = "developer"
print(users)


#question 5

users = {
    "andrew": {"age": 26, "country": "Japan"},
    "anna": {"age": 24, "country": "Germany"}
}


for key, value in users.items():
    print(key)


#question 6
#access nested data in a loop !

users = {
    "andrew": {"age": 26, "country": "Japan"},
    "anna": {"age": 24, "country": "Germany"},
    "mike": {"age": 30, "country": "Canada"}
}


for i, j in users.items():
    print(i)


#question 7
#mmodify nested data in a loop
users = {
 'andrew': {'age': 26, 'country': 'Japan'},
 'anna': {'age': 24, 'country': 'Germany'},
 'mike': {'age': 30, 'country': 'Canada'}
}


for i, j in users.items():
    users[i]["age"] = j["age"] + 1

print(users)


#next day lets understand

for user in users


for value in users


for key, value in users.items()
