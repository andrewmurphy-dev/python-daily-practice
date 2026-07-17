
def delete_contacts(contact):
    if not contact:
        print("no contacts found!")

    print()
    print("Delete Contacts")
    print("-" * 30)
    email_delete = input("please enter the email address of the user in which you want to delete: ").lower().strrip()

    if email_delete == "":
        print("the input cannot be blank!")
        return

    for name, value in contact.items():
        if email_delete == value["email"]:
            del value["email"]
            print("contact has been deleted!")


