#some practice question below of day 4

#print each letter of "python"

#question 1
for letter in "Python":
    print(letter)

#question 2
word = "education"
for i in word:
    if i in "aeiou":
        print(i)

#question 3
#count the letters in "programming" using a loop.

word = "programming"
for count in range(1, word + 1):
    print(count)

#so the problem is that i cannot count the range of a string

#second attempt !


#well im not really counting the letters im just counting the letters by myself and generating a variable loop corelated to the count ! if that makes sense !
#so the problem ! range only works with numbers not strings andrew !


##solution##
#so pretty easy solution , so now we know it!


#part 1

word = "programming"
count = 0
for letter in word:
    print(letter)

letter = "p"
letter = "r"
letter = "o"
letter = "g"
...

#next is part 2 !
count = count + 1
print(count)

count = 0
count = 1
count = 2
count = 3
...
count = 11

#confusion here !
#so this might be a confusing question we are creating a variable loop with letter ,
# my confusion why do we see count listed instead of letter


#some practice questions of forward and reverse count chatgpt !


#question 1
count = 1
for i in range(1, 9):
    count = count + 1
    print(count)


#question 2
count = 8
for i in range(8, 0 , -1):
    count = count - 1
    print(count)



#question 3
word = "python"
count = 0

for letter in word:
    count = count + 1
    print(count)


#question 4
word = "python"
count = 6
for letter in word:
    count = count - 1
    print(count)


# so these are all wrong andrew ! to be honest !

    count = count + 1
    print(count)

    #what do this do ?

    #this gives one result ! the total !

# so there is a massive thing i notice ! , where you place the print(count) this tells you the specific result you get !

#there are two forms of results !

#if you only want to find the total ! , you move the print outside the loop !
word = "python"
count = 0

for letter in word:
    count = count + 1

print(count)

#the outside gives the total
