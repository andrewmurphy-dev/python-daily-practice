#lets solidify tracking variable


#question 1

word = "mississippi"
count = 0

for i in word:
    if i in "aeiou":
        count = count + 1

print(count)
# a


#question 2
count = 0
for i in range(1, 51, 1):
    if i % 5 == 0:
        count = count + 1

print(count)
# a

#question 3
word = "education"
new_string = ""

for i in word:
    if i not in "aeiou":
        new_string = new_string + i
        print(new_string) #this is inside the loop and this creates a list

#this should be outside the loop !
#so we just get the result !


#more questions not correlated to count tracking variable

#question 4
word = "strength"
x = 0

for i in word:
    if i == "a":
        x = x + 1

print(x)



### largest number confusion ### 



#question 5
#largest number
numbers = [4, 12, 7, 3, 18, 5]
x = [0]

for i in numbers:
    if
#yeah i am confused with this one

# what i am confused about is !
#why do we need the tracking variable like this in the beginning , x = numbers[0]
#im confused about this if n > largest:
#largest = n
#but in previous version with count we used count = 0 how is this any different


#here we are , step 1

largest = numbers[0]

#we use this as a comparison that correlates to the list, we are assuming this is the largest number !
#numbers[0] = 4
#so the programme has something to compare aginst !

numbers = [4, 12, 7, 3, 18, 5]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print(largest)

#so its constantly comparing against the largest ,
# i.e. 4 and if n > largest we change it i.e. largest = n




#step 2 how does this compare to count = 0
count = 0

for i in "banana":
    if i == "a":
        count = count + 1

#loop → get value
#compare → check condition
#tracker → update if condition is True