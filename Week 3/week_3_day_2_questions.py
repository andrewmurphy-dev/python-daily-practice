# we are doing questions from week 1 , 2 and week 3 upon day 2


#question 1
for i in range(1, 11):
    print(i)

# 10/10


#question 2
for i in range(2, 22, 2):
    print(i)
# 10/10

#question 3
#reverse movement
for i in range(10, 11, 1):
     print(i)


#this is wrong 2/10
#this is not reverse !

#the solution is below !
for i in range(10, 0, -1):
    print(i)

10 → 9 → 8 → 7 → 6 → 5 → 4 → 3 → 2 → 1
#key rule if the numbers go down the steps must be negative !
#If numbers go down → step must be negative


#question 4
for i in range(1, 21):
    print(i)
    if i % 2 == 0:
        print("even")
# 7/10
#you needed to include an else statement or the python will write the word "even" on the loop

#question 5
for i in range(3, 33, 3):
    print(i)

# 10/10

#question 6
user = int(input("Enter a number: "))
for user in range(1, user + 1): #what is the point of doing user + 1 if the default python interpreter "step" is 1
    #now i get it andrew! the user is the stop , and we add + 1 cause thats how the python interpreter will now !
    print(user)

# 8/10
#some correction andrew ! the variable in the for loop should be different ! thats all !




