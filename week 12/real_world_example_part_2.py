#another real world example



def get_age():
    while True:
        age_input = input("enter your age: ").strip()

        if age_input == "":
            print("age cannot be empty")
            continue


        try:
            option = int(age_input)
        except ValueError:
            print("error, must be a valid number input!")
            continue

        if option <= 0:
            print("age cannot be negative")
            continue

        elif option >= 120:
            print("age needs to be realistic")
            continue

        return option


result = get_age()
print(result)


#the only problem is two !

#the variable name for option !

#and option <= 0
