#so i see a problem we are studying from day 1
#in our cli project

#we have this

option = input("Type to choose: ").lower().strip()

#this is for choosing an option !


#this can go wrong if the user input is lets say One. Two,
#we need it to go to value error !


choice_text = input("type to choose: ").strip()

try:
    choose = int(choice_text)
except ValueError:
    print("the number must be a number!")


#so the problem is your program will still run!
#so it is best to use continue , as we are looping !
#it means stop this current loop cycle and go back at the top of the loop !
#we see we change the variable names !



#so we seem we have done alot of error and validation in our project !