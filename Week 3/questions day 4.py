
#question 1
word = "education"
count = 0
for letter in word:
    if letter in "aeiou":
        count = count + 1

print(count)


#question 2
x = "computer"
for letter in x:
    if letter in "bcdfghjklmnpqrstvwxyz":
        print(letter)
#you needed to count the total amount

x = "computer"
count = 0
for letter in x:
    if letter in "bcdfghjklmnpqrstvwxyz":
        count = count + 1

print(count)







#question 3
for i in range(1, 11, 1):
    total = total + i

print(total)

#this was my hardest one

#funny you actually got most of it correct ! but the only thing you needed to do was the total was not defined , like count = 0

#question 4
# find the largest number

numbers = [4, 7, 2, 9, 5]
for i in numbers:
    if i in numbers >= 9:
        print(i)
    else:
        print(i)



#so there are two issues here !
#you need a tracking variable we will go over this day 5 !
#solution is below
numbers = [4, 7, 2, 9, 5]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print(largest)









#question 5
#letter counter
count = 0
word = input("enter a word: ")
for i in word:
    if i in "a":
        count = count + 1
print(count)


#you can also write if i == "a"


#question 6
#even number counter
count = 0
for i in range(1, 21, 1):
    if i % 2 == 0:
        count = count + 1

print(count)


#problem 7

word = "python"

for letter in word[::-1]:
    print(letter)

#this works but the question was different , we will learn this in day 5 i.e. tracking variable
#solution below

word = "python"
reverse = ""

for letter in word:
    reverse = letter + reverse

print(reverse)