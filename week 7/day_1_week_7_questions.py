#questions
#question 1
users = ["andrew", "anna", "mike", "leo"]
name = input("Enter your name: ")

print(name in users)



#to make it better !

#what would i do ?

users = ["andrew", "anna", "mike", "leo"]

name = input("Enter your name: ")

if name in users:
    print("user exists")
else:
    print("user does not exist")



#question 2
word = "programming"
letter = input("Enter your letter: ")

if letter in word:
    print("letter found")
else:
    print("letter not found")


#question 3



email = input("Enter your email: ")

if "@" in email:
    print("valid email")
else:
    print("invalid email")


#question 4

taken_usernames = ["admin", "root", "test"]

username = input("Enter your username: ")

if username not in taken_usernames:
    print("username available")
else:
    print("username taken")

#question 5


country = input("Enter your country: ")

allowed_countries = ["Japan", "USA", "Germany", "France"]

if country in allowed_countries:
    print("country found")
else:
    print("country not found")


