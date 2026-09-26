#lets do some real world examples


def get_menu_choice():

    while True:
        choose_option = input("enter a option: ").strip()


        if choose_option == "":
            print("error, input cannot be empty!")
            continue

        try:
            option = int(choose_option)

        except ValueError:
            print("choice must be a number")
            continue


        if option < 1 or option > 4:
            print("invalid option, please choose 1, 2, 3 or 4.")
            continue

        return option



result = get_menu_choice()
print(result)

