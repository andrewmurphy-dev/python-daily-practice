#question 11

def first_three(text):
    return text[0:3:1]


#question 12

def last_three(text):
    return text[-3:len(text):1]


result = last_three("steptrace")

print(result)


#quewstion 13

def middle_three(text):
    middle = len(text) // 2
    return text[middle - 1: middle + 2: 1]

result = middle_three("steptrace")
print(result)

#problem here we need to use len of text , how can we divide a text by 2 ?

#question 14
def remove_first_last(text):
    middle = len(text) // 2
    return text[middle - 1: middle + 2: 1]


#question 15

def count_leter(text, letter):
    count = 0
    for num in text:
        if letter in num:
            count += 1

    return count

#question 16

def find_longest_word(words):
    longest_word = words[0]

    for num in words:
        if len(num) > len(longest_word):
            longest_word = num

    return longest_word

words = ["apple", "river", "cloud", "stone", "dragon", "shadow", "silver", "winter", "forest", "rocket"]
result = find_longest_word(words)
print(result)


#question 17

def login(username, password, users):
    if password == users[username]:
        return "success"
    else:
        print("no dictionary found!")
        return





#question 18

def add_user(username, password, users):
    username = input("enter a username to signup!: ").lower().strip()

    if username in users:
        print("username is already taken! Try Again!")
        return

    password = input("enter a password to signup: ").lower()

    if not password.isdigit():
        return None

    users[username] = password
    save_users()


#question 19

def total_expenses(expenses):
    total = 0
    for amount in expenses.values()
        total += amount

    print(total)


#question 20

def save_line(filename, text):
        with open("filename", "a", encoding="utf-8") as f:
            f.write("this is a new line\n")



