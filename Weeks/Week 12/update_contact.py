
def update_contact(contact):
    while True:
        print("Update contact!")
        print("what do you want to update?\n")
        print("press 1: \tto update username")
        print("press 2: \tto update email")
        print("press 3: \tto update phone")

        choice = input("please enter your choice: ").strip()

        if choice == "":
            print("it must not be blank!")
            continue

        email = input("type the email address associated with user: ").strip()

        if email == "":
            print("email cannot be blank!")
            continue

        if not email in contact:
            print("no email found!")

        for name, value in contact.items:
            if email == value["email"]:
                print("username:\t", name)
                print("email:\t", value["email"])
                print("phone:\t", value["phone"])

        if choice == "1":
            new_username = input("please enter new username: ")
            contact[new_username] = contact[name]
            del contact[name]
            print("contact updated")

        elif choice == "2":
                new_email = input("please enter new email: ").strip()
                #this follows a different structure
                value["email"] = new_email
                print("email updated")

        elif choice == "3":
                new_phone = input("please enter new phone number: ").lower().strip()
                value["phone"] = new_phone
                print("phone updated")
