#question 1

users = ["anna", "mike", "leo"]

users.append("sarah")
print(users)




#question 2
numbers = [10, 20, 30, 40]

numbers.remove(20)
print(numbers)




#question 3




#question 4
#find the index potion

cities = ["tokyo", "osaka", "kyoto", "nagoya"]

cities.index("kyoto")
print(cities)


#we have to store the value !
#correction



cities = ["tokyo", "osaka", "kyoto", "nagoya"]
position = cities.index("kyoto")
print(position)

#or we can do this

cities = ["tokyo", "osaka", "kyoto", "nagoya"]

print(cities.index("nagoya"))

#this is temp storage





#question 5
scores = [55, 78, 90, 66, 88]

print(scores.sort())


#sort does not return a value
#it modies a list directly in memory
#below is the correct solition

scores = [55, 78, 90, 66, 88]

scores.sort()
print(scores)

#question 6
#username search

users = ["anna", "mike", "leo", "sarah"]

search = input("enter username to search: ")

for user in users:
    if search in user:
        print("user found")
        break
else:
    print("user not found")

#we actually didnt need to looop here!



#so solution

if search in users:
    print("user found")
else:
    print("user not found")

#or

for user in users:
    if search == user:
        print("user found")
    break

else:
    print("user not found")






