#the biggest problem in understanding was outer vs inner dictionary ! 
#choosing the right field for conditions ! 



#how to solve this ! 
#1 what is my variable right now?

#2 which key matches the question ! 

for student_id, info in students.items():
    name = info["name"]
    age = info["age"]
    grade = info["grade"]

    # then do logic using name/age/grade


#question 1 
school = {
    "classA": {"teacher": "Ms Lee", "room": 101},
    "classB": {"teacher": "Mr Kim", "room": 202},
}

print(school["classB"]["room"])

#question 2
users = {
    "u1": {"name": "Ana", "role": "admin"},
    "u2": {"name": "Ben", "role": "guest"},
    "u3": {"name": "Cara", "role": "admin"},
}

print(users["u1"]["name"])
print(users["u2"]["name"])
print(users["u3"]["name"])



#question 3 
users = {
    "u1": {"name": "Ana", "role": "admin"},
    "u2": {"name": "Ben", "role": "guest"},
    "u3": {"name": "Cara", "role": "admin"},
}


for user_id, values in users.items():
    print(user_id, users[user_id]["name"])


#question 4 
#filter by inner value !

#question 5 

scores = {
    "s1": {"team": "A", "points": 10},
    "s2": {"team": "B", "points": 7},
    "s3": {"team": "A", "points": 12},
    "s4": {"team": "C", "points": 9},
}

count = 0 

for score in scores.values():
    if score["team"] == "A":
        count += 1
print(count)
