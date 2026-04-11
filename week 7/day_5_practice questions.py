#question 1
products = ["apple juice", "orange juice", "milk", "bread"]
product_name = input("enter product name: ").strip().lower()

if product_name in products:
    print("product available")
else:
    print("product not found")




#question 2
#email domain counter
employees = {
    "andrew": "andrew@gmail.com",
    "anna": "anna@company.com",
    "mike": "mike@gmail.com",
    "alex": "alex@company.com"
}

count_email = 0

for user, email in employees:
    if "gmail" in email:
        count_email = count_email + 1

print(count_email)



#question 3
#detect duplicate words
seen = []
sentence = input("enter a sentence: ").lower().split()

for user in sentence:
    if user in seen:
        print("duplicate found!")
        break
    seen.append(user)
else:
    print("no duplication found")



#question 4



#question 5
#order counter

#ask the user to enter food orders seperated by spaces

user_ask = input("enter food order please!: ").split()
count = 0
for user in user_ask:
    if user == "burger":
        count = count + 1
print(count)

#question 6
#username validation

username = input("enter a username: ")

if " " not in username and username == username.lower():
    print("valid username")
else:
    print("invalid username")
